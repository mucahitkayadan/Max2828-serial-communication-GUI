"""
This module contains the main functionality for controlling the RF device.
It includes functions for checking the device status, establishing a serial connection,
and saving/retrieving data from a SQLite database.
"""
import sys
import serial
import struct
import sqlite3
from PyQt5 import QtWidgets
import Max2828Window as myWindow
from Max2828Window import MainWindow


class MainController(object):
    """
    This class represents the main controller for the RF device.
    It provides methods for checking the device status, establishing a serial connection,
    and saving/retrieving data from a SQLite database.
    """

    def __init__(self):
        self.max_value = None
        self.theCursor = None
        self.con = None
        self.starter_byte = 0xAA
        self.Max2828_command = 0x02
        self.Max5866_command = 0x03
        self.rf_command = 0x01
        self.padac_command = 0x02
        self.rx_command = 0x03
        self.tx_command = 0x04
        self.lna_command = 0x05
        self.gain_command = 0x06
        self.max_command = 0x07
        self.zero_byte = 0x00
        self.source_byte = 0x01
        self.destination_byte = 0x02
        self.value_change_max = 2
        self.counter_of_save_db = 1
        self.com_port = 'COM3'
        self.globalnameDB = 'db\\LastPowerDown.db'
        self.check_package_list = True
        self.ctr = 0
        print("RF     PAD-AC    RX     TX    LNA   GAIN    M2828    M5866")

    def check_lock(self, ui):
        """
        Checks the lock status and enables/disables UI elements accordingly.
        """
        try:
            if ui.lock_check_box.isChecked():
                self.disable_controls(ui)
            else:
                self.enable_controls(ui)
        except Exception as e:
            print("Error with Lock:", str(e))

    def disable_controls(self, ui):
        """
        Disables UI controls.
        """
        ui.rf_frequency_line.setEnabled(False)
        ui.padac_output_bias_line.setEnabled(False)
        ui.rxvga_gain_line.setEnabled(False)
        ui.txvga_gain_line.setEnabled(False)
        ui.com_port_line.setEnabled(False)
        ui.rxlna_gain_combobox.setEnabled(False)
        ui.tx_baseband_gain_combo_box.setEnabled(False)
        ui.setups_combo_box.setEnabled(False)
        ui.max2828_combo_box.setEnabled(False)
        ui.max5866_combo_box.setEnabled(False)
        ui.del_button.setEnabled(False)
        ui.rf_frequency_scroll_bar.setEnabled(False)
        ui.padac_output_bias_scroll_bar.setEnabled(False)
        ui.rxvga_gain_scroll_bar.setEnabled(False)
        ui.txvga_gain_scroll_bar.setEnabled(False)

    def enable_controls(self, ui):
        """
        Enables UI controls.
        """
        ui.rf_frequency_line.setEnabled(True)
        ui.padac_output_bias_line.setEnabled(True)
        ui.rxvga_gain_line.setEnabled(True)
        ui.txvga_gain_line.setEnabled(True)
        ui.com_port_line.setEnabled(True)
        ui.rxlna_gain_combobox.setEnabled(True)
        ui.tx_baseband_gain_combo_box.setEnabled(True)
        ui.setups_combo_box.setEnabled(True)
        ui.max2828_combo_box.setEnabled(True)
        ui.max5866_combo_box.setEnabled(True)
        ui.del_button.setEnabled(True)
        ui.rf_frequency_scroll_bar.setEnabled(True)
        ui.padac_output_bias_scroll_bar.setEnabled(True)
        ui.rxvga_gain_scroll_bar.setEnabled(True)
        ui.txvga_gain_scroll_bar.setEnabled(True)

    def check_device(self, ui):
        if self.con.is_open:
            ui.connection_label.setText(self.con.name + " Connected")
        else:
            ui.connection_label.setText("Disconnected")

    def serial_connection(self, ui):
        try:
            self.com_port = ui.com_port_line.text()
            self.con = serial.Serial(self.com_port, 9600, timeout=1)
        except serial.SerialException:
            print("No Port Found")
            ui.connection_label.setText("Disconnected")
            ui.close_application()
            raise
        except Exception as e:
            print("Communication Port Error:", str(e))
            ui.connection_label.setText("Disconnected")
            ui.close_application()

    def print_db(self):
        try:
            result = self.theCursor.execute(
                'SELECT ID,RF, PADAC, RXVGA, TXVGA, TXLNA, RXGAIN, MAX, PORT, CBI, CBT FROM DB')
            for row in result:
                print("ID     :", row[0])
                print("RF     :", row[1])
                print("PADAC  :", row[2])
                print("RXVGA  :", row[3])
                print("TXVGA  :", row[4])
                print("RXLNA  :", row[5])
                print("TXGAIN :", row[6])
                print("MAX    :", row[7])
                print("PORT   :", row[8])
                print("Index  :", row[9])
                print("Text   :", row[10])
                print("        ")
        except sqlite3.OperationalError:
            print("The Table Doesn't Exist")
        except Exception as e:
            print("Couldn't Retrieve Data From Database:", str(e))

    def save_db(self, ui, name_of_db):
        db_conn = sqlite3.connect(name_of_db)
        self.theCursor = db_conn.cursor()
        try:
            rf_value = int(ui.rf_frequency_line.text())
            padac_value = int(ui.padac_output_bias_line.text())
            rxvga_value = int(ui.rxvga_gain_line.text())
            txvga_value = int(ui.txvga_gain_line.text())
            lna_value = ui.rxlna_gain_combobox.currentIndex()
            gain_value = ui.tx_baseband_gain_combo_box.currentIndex()
            max_value = self.value_change_max
            port_value = ui.com_port_line.text()
            cb_i_value = ui.setups_combo_box.currentIndex()
            cb_t_value = ui.setups_combo_box.currentText()
            params = (
                rf_value, padac_value, rxvga_value, txvga_value, lna_value, gain_value, max_value, port_value,
                cb_i_value,
                cb_t_value)
            db_conn.execute("DROP TABLE IF EXISTS DB")
            db_conn.commit()
            db_conn.execute('''CREATE TABLE DB
            (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,RF INT,PADAC INT,RXVGA INT,TXVGA INT,TXLNA INT,RXGAIN INT,MAX INT,PORT TEXT, CBI INT, CBT TEXT);''')
            db_conn.commit()
            db_conn.execute("INSERT INTO DB VALUES (NULL,?,?,?,?,?,?,?,?,?,?)", params)
            db_conn.commit()
            print("Table Created")
            print("Database Created")
            db_conn.close()
            self.counter_of_save_db += 1
            return True
        except Exception as e:
            print("Couldn't save data to the database:", str(e))
            return False

    def send_receive(self, package_list):
        try:
            self.send(package_list)
            self.receive_ack(package_list)
        except serial.SerialException as e:
            print("Error in send-receive:", str(e))
            raise
        except Exception as e:
            print("Error occurred:", str(e))

    def receive_db(self, ui, nameofDB):
        rcv_db = sqlite3.connect(nameofDB)
        cur = rcv_db.cursor()
        result = cur.execute("SELECT ID,RF, PADAC, RXVGA, TXVGA, TXLNA, RXGAIN, MAX, PORT, CBI, CBT FROM DB")
        try:
            for row in result:
                ui.rf_frequency_line.setText(str(row[1]))
                ui.padac_output_bias_line.setText(str(row[2]))
                ui.rxvga_gain_line.setText(str(row[3]))
                ui.txvga_gain_line.setText(str(row[4]))
                ui.rxlna_gain_combobox.setCurrentIndex(int(row[5]))
                ui.tx_baseband_gain_combo_box.setCurrentIndex(int(row[6]))
                self.max_value = int(row[7])
                ui.com_port_line.setText(str(row[8]))
        # ui.setups_combo_box.insertItem(1,str(row[10]))
        except sqlite3.OperationalError:
            print("Operational Error")
        except Exception as e:
            print("Couldn't Retrieve Data From Database when receiving"
                  + "Error: " + str(e))

    def send(self, package_list):
        try:
            self.con.write(package_list)
        except serial.SerialException as e:
            print("Error sending data:", str(e))
            self.try_3_times(package_list)
            raise
        except Exception as e:
            print("Error occurred:", str(e))

    def try_3_times(self, package_list):
        try:
            for i in range(3):
                self.ctr += 1
                print(f"Trying again... {i + 1}. time")
                if self.ctr >= 3:
                    print("Couldn't succeed")
                    break
                self.send_receive(package_list)
                if self.check_package_list:
                    print(f"Succeed in {i + 1}. time")
                    break
            print("========================================================")
        except Exception as e:
            print("Communication Error:", str(e))

    def receive(self, PackageList):
        try:
            our_buffer = []
            counter = 0
            while counter < len(PackageList):
                msg = self.con.read()
                msg = msg.hex()
                msg = int(msg, 16)
                our_buffer.append(msg)
                print(msg)
                counter = counter + 1
            print(PackageList)
            print(our_buffer)
            if our_buffer == PackageList:
                print("Package received successfully")
            else:
                for i in range(3):
                    print("Trying again... " + str(i + 1) + ". time ")
                    self.send_receive(PackageList)
                print("Package could not be transferred")
            print("========================================================")
        except serial.SerialException:
            print("No connection found")
            raise
        except Exception as e:
            print("Error occurred: " + str(e))

    def receive_ack(self, package_list):
        try:
            ack = self.con.read(len(package_list))
            if ack == package_list:
                print("Transmission complete")
                self.check_package_list = True
            else:
                print("Not Successful Transmission")
                self.check_package_list = False
        except serial.SerialException as e:
            print("Error receiving acknowledgment:", str(e))
            raise
        except Exception as e:
            print("Error occurred:", str(e))

    def des2828(self):
        self.destination_byte = 0X02
        self.max_value = 2

    def des5866(self):
        self.destination_byte = 0X03
        self.max_value = 3

    def check_destination(self):
        if self.max_value == 2:
            self.send_receive(self.Max2828_Package)
        elif self.max_value == 3:
            self.send_receive(self.Max5866_Package)
        else:
            pass

    def value_to_hex(self, ui):
        value_rf_frequency = ui.rf_frequency_scroll_bar.value()
        value_padac_output_bias = ui.padac_output_bias_scroll_bar.value()
        value_rxvga_gain = ui.rxvga_gain_scroll_bar.value()
        value_txvga_gain = ui.txvga_gain_scroll_bar.value()
        value_lna = ui.rxlna_gain_combobox.currentIndex()
        value_gain = ui.tx_baseband_gain_combo_box.currentIndex()
        value_max2828 = ui.max2828_combo_box.currentIndex()
        value_max5866 = ui.max5866_combo_box.currentIndex()
        rf = struct.pack('>h', value_rf_frequency)
        rf = rf.hex()
        rf1 = int(rf[:2], 16)
        rf2 = int(rf[-2:], 16)
        padac = struct.pack('>h', value_padac_output_bias)
        padac = padac.hex().zfill(4)
        padac1 = int(padac[:2], 16)
        padac2 = int(padac[-2:], 16)
        rx = struct.pack('>h', value_rxvga_gain)
        rx = rx.hex().zfill(4)
        rx1 = int(rx[:2], 16)
        rx2 = int(rx[-2:], 16)
        tx = struct.pack('>h', value_txvga_gain)
        tx = tx.hex().zfill(4)
        tx1 = int(tx[:2], 16)
        tx2 = int(tx[-2:], 16)
        lna = struct.pack('>h', value_lna)
        lna = lna.hex().zfill(4)
        lna1 = int(lna[:2], 16)
        lna2 = int(lna[-2:], 16)
        gain = struct.pack('>h', value_gain)
        gain = gain.hex().zfill(4)
        gain1 = int(gain[:2], 16)
        gain2 = int(gain[-2:], 16)
        max2828 = struct.pack('>h', value_max2828)
        max2828 = max2828.hex()
        max28281 = int(max2828[:2], 16)
        max28282 = int(max2828[-2:], 16)
        max5866 = struct.pack('>h', value_max5866)
        max5866 = max5866.hex()
        max58661 = int(max5866[:2], 16)
        max58662 = int(max5866[-2:], 16)
        print(
            rf + "    " + padac + "   " + rx + "   " + tx + "   " +
            lna + "  " + gain + "    " + max2828 + "    " + max5866)

        self.RF_Package = [self.starter_byte, self.source_byte, self.destination_byte, self.rf_command,
                           rf1, rf2, self.zero_byte, self.zero_byte,
                           self.zero_byte, self.zero_byte, self.zero_byte, self.zero_byte]
        self.PADAC_Package = [self.starter_byte, self.source_byte, self.destination_byte, self.padac_command,
                              padac1, padac2, self.zero_byte, self.zero_byte,
                              self.zero_byte, self.zero_byte, self.zero_byte, self.zero_byte]
        self.RX_Package = [self.starter_byte, self.source_byte, self.destination_byte, self.rx_command,
                           rx1, rx2, self.zero_byte, self.zero_byte,
                           self.zero_byte, self.zero_byte, self.zero_byte, self.zero_byte]
        self.TX_Package = [self.starter_byte, self.source_byte, self.destination_byte, self.tx_command,
                           tx1, tx2, self.zero_byte, self.zero_byte,
                           self.zero_byte, self.zero_byte, self.zero_byte, self.zero_byte]
        self.LNA_Package = [self.starter_byte, self.source_byte, self.destination_byte, self.lna_command,
                            lna1, lna2, self.zero_byte, self.zero_byte,
                            self.zero_byte, self.zero_byte, self.zero_byte, self.zero_byte]
        self.GAIN_Package = [self.starter_byte, self.source_byte, self.destination_byte, self.gain_command,
                             gain1, gain2, self.zero_byte, self.zero_byte,
                             self.zero_byte, self.zero_byte, self.zero_byte, self.zero_byte]
        self.Max2828_Package = [self.starter_byte, self.source_byte, self.destination_byte, self.max_command,
                                max28281, max28282, self.zero_byte, self.zero_byte,
                                self.zero_byte, self.zero_byte, self.zero_byte, self.zero_byte]
        self.Max5866_Package = [self.starter_byte, self.source_byte, self.destination_byte, self.max_command,
                                max58661, max58662, self.zero_byte, self.zero_byte,
                                self.zero_byte, self.zero_byte, self.zero_byte, self.zero_byte]

    def main_loop(self):
        app = QtWidgets.QApplication(sys.argv)
        ui = myWindow.Window()
        main_window = MainWindow()
        ui.setup_ui(main_window)
        main_window.show()
        self.serial_connection(ui)
        self.value_to_hex(ui)
        self.check_device(ui)

        ui.lock_check_box.stateChanged.connect(lambda: self.check_lock(ui))
        ui.com_port_top_label.editingFinished.connect(lambda: self.serial_connection(ui))
        # Menu Side
        ui.action_exit.triggered.connect(ui.close_application)
        # ScrollBar Side
        ui.rf_frequency_scroll_bar.valueChanged.connect(
            lambda: ui.scroll_bar_value(ui.rf_frequency_scroll_bar, ui.rf_frequency_line))
        ui.padac_output_bias_scroll_bar.valueChanged.connect(
            lambda: ui.scroll_bar_value(ui.padac_output_bias_scroll_bar, ui.padac_output_bias_line))
        ui.rxvga_gain_scroll_bar.valueChanged.connect(
            lambda: ui.scroll_bar_value(ui.rxvga_gain_scroll_bar, ui.rxvga_gain_line))
        ui.txvga_gain_scroll_bar.valueChanged.connect(
            lambda: ui.scroll_bar_value(ui.txvga_gain_scroll_bar, ui.txvga_gain_line))

        ui.rf_frequency_line.editingFinished.connect(
            lambda: ui.rf_frequency_scroll_bar.setSliderPosition(int(ui.rf_frequency_line.text())))
        ui.padac_output_bias_line.editingFinished.connect(
            lambda: ui.padac_output_bias_scroll_bar.setSliderPosition(int(ui.padac_output_bias_line.text())))
        ui.rxvga_gain_line.editingFinished.connect(
            lambda: ui.rxvga_gain_scroll_bar.setSliderPosition(int(ui.rxvga_gain_line.text())))
        ui.txvga_gain_line.editingFinished.connect(
            lambda: ui.txvga_gain_scroll_bar.setSliderPosition(int(ui.txvga_gain_line.text())))

        # Button Side
        def removeCombobox():
            if ui.setups_combo_box.currentText() == "LastPowerDown" or ui.setups_combo_box.currentText() == "":
                pass
            else:
                ui.setups_combo_box.removeItem(ui.setups_combo_box.currentIndex())

        ui.del_button.clicked.connect(lambda: removeCombobox())
        #  Combobox Side

        # Line Edit Side
        ui.rf_frequency_line.setText(str(ui.rf_frequency_scroll_bar.value()))
        ui.padac_output_bias_line.setText(str(ui.padac_output_bias_scroll_bar.value()))
        ui.rxvga_gain_line.setText(str(ui.rxvga_gain_scroll_bar.value()))
        ui.txvga_gain_line.setText(str(ui.txvga_gain_scroll_bar.value()))

        ui.rf_frequency_line.editingFinished.connect(
            lambda: ui.checking_lines(ui.rf_frequency_scroll_bar, ui.rf_frequency_line))
        ui.padac_output_bias_line.editingFinished.connect(
            lambda: ui.checking_lines(ui.padac_output_bias_scroll_bar, ui.padac_output_bias_line))
        ui.rxvga_gain_line.editingFinished.connect(
            lambda: ui.checking_lines(ui.rxvga_gain_scroll_bar, ui.rxvga_gain_line))
        ui.txvga_gain_line.editingFinished.connect(
            lambda: ui.checking_lines(ui.txvga_gain_scroll_bar, ui.txvga_gain_line))
        # Communication Side

        ui.rf_frequency_scroll_bar.valueChanged.connect(lambda: self.value_to_hex(ui))
        ui.padac_output_bias_scroll_bar.valueChanged.connect(lambda: self.value_to_hex(ui))
        ui.rxvga_gain_scroll_bar.valueChanged.connect(lambda: self.value_to_hex(ui))
        ui.txvga_gain_scroll_bar.valueChanged.connect(lambda: self.value_to_hex(ui))
        ui.rxlna_gain_combobox.currentIndexChanged.connect(lambda: self.value_to_hex(ui))
        ui.tx_baseband_gain_combo_box.currentIndexChanged.connect(lambda: self.value_to_hex(ui))
        ui.max2828_combo_box.currentIndexChanged.connect(lambda: self.des2828())
        ui.max2828_combo_box.currentIndexChanged.connect(lambda: self.value_to_hex(ui))
        ui.max5866_combo_box.currentIndexChanged.connect(lambda: self.des5866())
        ui.max5866_combo_box.currentIndexChanged.connect(lambda: self.value_to_hex(ui))

        # Database&Combobox
        # indexOfSetupsCombobox

        def ComboboxDB():
            if ui.setups_combo_box.currentText() != '':
                self.globalnameDB = ui.setups_combo_box.currentText() + '.db'
                self.save_db(ui, self.globalnameDB)
            print(self.globalnameDB + " created")

        ui.setups_combo_box.currentIndexChanged.connect(lambda: ComboboxDB())

        ui.rf_frequency_scroll_bar.sliderReleased.connect(lambda: self.save_db(ui, self.globalnameDB))
        ui.padac_output_bias_scroll_bar.sliderReleased.connect(lambda: self.save_db(ui, self.globalnameDB))
        ui.rxvga_gain_scroll_bar.sliderReleased.connect(lambda: self.save_db(ui, self.globalnameDB))
        ui.txvga_gain_scroll_bar.sliderReleased.connect(lambda: self.save_db(ui, self.globalnameDB))
        ui.rxlna_gain_combobox.currentIndexChanged.connect(lambda: self.save_db(ui, self.globalnameDB))
        ui.tx_baseband_gain_combo_box.currentIndexChanged.connect(lambda: self.save_db(ui, self.globalnameDB))
        ui.max2828_combo_box.currentIndexChanged.connect(lambda: self.save_db(ui, self.globalnameDB))
        ui.max5866_combo_box.currentIndexChanged.connect(lambda: self.save_db(ui, self.globalnameDB))
        ui.setups_combo_box.activated.connect(lambda: self.receive_db(ui, self.globalnameDB))

        ui.send_all_button.clicked.connect(lambda: self.send_receive(self.RF_Package))
        ui.send_all_button.clicked.connect(lambda: self.send_receive(self.PADAC_Package))
        ui.send_all_button.clicked.connect(lambda: self.send_receive(self.RX_Package))
        ui.send_all_button.clicked.connect(lambda: self.send_receive(self.TX_Package))
        ui.send_all_button.clicked.connect(lambda: self.send_receive(self.LNA_Package))
        ui.send_all_button.clicked.connect(lambda: self.send_receive(self.GAIN_Package))
        ui.send_all_button.clicked.connect(lambda: self.check_destination())

        ##############
        ##############
        sys.exit(app.exec_())


if __name__ == "__main__":
    main_controller = MainController()
    main_controller.main_loop()
