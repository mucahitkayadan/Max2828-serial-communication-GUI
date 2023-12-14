# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Max.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Window(object):

    def __init__(self):
        self.padac_output_bias_layout = None
        self.spacer_item2 = None
        self.lock_label = None
        self.connection_status_label = None
        self.connection_label = None
        self.menubar = None
        self.menu_exit = None
        self.max2828_combo_box = None
        self.max5866_top_label = None
        self.max2828_top_label = None
        self.max5866_combo_box = None
        self.spacer_item = None
        self.rf_frequency_label = None
        self.rf_vertical_layout_1 = None
        self.spacer_item1 = None
        self.setups_label = None
        self.grid_layout = None
        self.central_widget = None
        self.padac_output_bias_label = None
        self.padac_output_bias_scroll_bar = None
        self.top_side_horizontal_layout = None
        self.send_all_button = None
        self.com_port_line = None
        self.padac_output_bias_line = None
        self.vertical_layout_2 = None
        self.tx_baseband_gain_combo_box = None
        self.rf_frequency_layout = None
        self.rf_frequency_scroll_bar = None
        self.tx_baseband_gain_label = None
        self.tx_baseband_gain_layout = None
        self.rf_frequency_line = None
        self.rf_frequency_top_label = None
        self.padac_output_bias_top_label = None
        self.tx_baseband_gain_top_label = None
        self.txvga_gain_line = None
        self.txvga_gain_top_label = None
        self.rxvga_gain_scroll_bar = None
        self.rxvga_gain_line = None
        self.txvga_gain_scroll_bar = None
        self.setups_combo_box = None
        self.rxvga_gain_top_label = None
        self.rxlna_gain_combobox = None
        self.rxlna_gain_top_label = None
        self.action_exit = None
        self.del_button = None
        self.com_port_top_label = None
        self.lock_check_box = None

    def scroll_bar_value(self, scroll_bar_name, line_edit_name):
        scrollbar_value = str(scroll_bar_name.value())
        line_edit_name.setText(scrollbar_value)

    def checking_lines(self, scroll_bar_name, line_edit_name):
        if int(line_edit_name.text()) < scroll_bar_name.minimum():
            line_edit_name.setText(str(scroll_bar_name.minimum()))
            scroll_bar_name.setSliderPosition(scroll_bar_name.minimum())
            scroll_bar_name.setValue(scroll_bar_name.minimum())
        elif int(line_edit_name.text()) > scroll_bar_name.maximum():
            line_edit_name.setText(str(scroll_bar_name.maximum()))
            scroll_bar_name.setSliderPosition(scroll_bar_name.maximum())
            scroll_bar_name.setValue(scroll_bar_name.maximum())
        else:
            pass

    def call_main(self):
        return QtWidgets.QMainWindow()

    def close_application(self):
        apps = QtWidgets.QApplication(sys.argv)
        sys.exit(apps.exec_())

    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(494, 413)
        MainWindow.setMaximumSize(QtCore.QSize(556, 413))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setObjectName("grid_layout")
        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.vertical_layout_2.setObjectName("vertical_layout_2")
        self.rxlna_gain_top_label = QtWidgets.QLabel(self.central_widget)
        self.rxlna_gain_top_label.setMaximumSize(QtCore.QSize(100, 15))
        self.rxlna_gain_top_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.rxlna_gain_top_label.setObjectName("rxlna_gain_top_label")
        self.vertical_layout_2.addWidget(self.rxlna_gain_top_label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.rxlna_gain_combobox = QtWidgets.QComboBox(self.central_widget)
        self.rxlna_gain_combobox.setMaximumSize(QtCore.QSize(16777215, 20))
        self.rxlna_gain_combobox.setEditable(False)
        self.rxlna_gain_combobox.setObjectName("rxlna_gain_combobox")
        self.rxlna_gain_combobox.addItem("")
        self.rxlna_gain_combobox.addItem("")
        self.rxlna_gain_combobox.addItem("")
        self.vertical_layout_2.addWidget(self.rxlna_gain_combobox)
        self.rxvga_gain_top_label = QtWidgets.QLabel(self.central_widget)
        self.rxvga_gain_top_label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.rxvga_gain_top_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rxvga_gain_top_label.setOpenExternalLinks(False)
        self.rxvga_gain_top_label.setObjectName("rxvga_gain_top_label")
        self.vertical_layout_2.addWidget(self.rxvga_gain_top_label)
        self.rxvga_gain_line = QtWidgets.QLineEdit(self.central_widget)
        self.rxvga_gain_line.setMaximumSize(QtCore.QSize(16777215, 20))
        self.rxvga_gain_line.setObjectName("rxvga_gain_line")
        self.vertical_layout_2.addWidget(self.rxvga_gain_line)
        self.rxvga_gain_scroll_bar = QtWidgets.QScrollBar(self.central_widget)
        self.rxvga_gain_scroll_bar.setMaximumSize(QtCore.QSize(16777215, 20))
        self.rxvga_gain_scroll_bar.setMaximum(31)
        self.rxvga_gain_scroll_bar.setInvertedControls(False)
        self.rxvga_gain_scroll_bar.setPageStep(1)
        self.rxvga_gain_scroll_bar.setSingleStep(1)
        self.rxvga_gain_scroll_bar.setOrientation(QtCore.Qt.Horizontal)
        self.rxvga_gain_scroll_bar.setObjectName("rxvga_gain_scroll_bar")
        self.vertical_layout_2.addWidget(self.rxvga_gain_scroll_bar)
        self.txvga_gain_top_label = QtWidgets.QLabel(self.central_widget)
        self.txvga_gain_top_label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.txvga_gain_top_label.setAlignment(QtCore.Qt.AlignCenter)
        self.txvga_gain_top_label.setObjectName("txvga_gain_top_label")
        self.vertical_layout_2.addWidget(self.txvga_gain_top_label)
        self.txvga_gain_line = QtWidgets.QLineEdit(self.central_widget)
        self.txvga_gain_line.setMaximumSize(QtCore.QSize(16777215, 20))
        self.txvga_gain_line.setObjectName("txvga_gain_line")
        self.vertical_layout_2.addWidget(self.txvga_gain_line)
        self.txvga_gain_scroll_bar = QtWidgets.QScrollBar(self.central_widget)
        self.txvga_gain_scroll_bar.setMaximumSize(QtCore.QSize(16777215, 20))
        self.txvga_gain_scroll_bar.setMaximum(63)
        self.txvga_gain_scroll_bar.setInvertedControls(False)
        self.txvga_gain_scroll_bar.setPageStep(1)
        self.txvga_gain_scroll_bar.setSingleStep(1)
        self.txvga_gain_scroll_bar.setOrientation(QtCore.Qt.Horizontal)
        self.txvga_gain_scroll_bar.setObjectName("txvga_gain_scroll_bar")
        self.vertical_layout_2.addWidget(self.txvga_gain_scroll_bar)
        self.tx_baseband_gain_top_label = QtWidgets.QLabel(self.central_widget)
        self.tx_baseband_gain_top_label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.tx_baseband_gain_top_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_baseband_gain_top_label.setObjectName("tx_baseband_gain_top_label")
        self.vertical_layout_2.addWidget(self.tx_baseband_gain_top_label)
        self.tx_baseband_gain_layout = QtWidgets.QHBoxLayout()
        self.tx_baseband_gain_layout.setObjectName("tx_baseband_gain_layout")
        self.tx_baseband_gain_combo_box = QtWidgets.QComboBox(self.central_widget)
        self.tx_baseband_gain_combo_box.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tx_baseband_gain_combo_box.setEditable(False)
        self.tx_baseband_gain_combo_box.setObjectName("tx_baseband_gain_combo_box")
        self.tx_baseband_gain_combo_box.addItem("")
        self.tx_baseband_gain_combo_box.addItem("")
        self.tx_baseband_gain_layout.addWidget(self.tx_baseband_gain_combo_box)
        self.tx_baseband_gain_label = QtWidgets.QLabel(self.central_widget)
        self.tx_baseband_gain_label.setObjectName("tx_baseband_gain_label")
        self.tx_baseband_gain_layout.addWidget(self.tx_baseband_gain_label)
        self.vertical_layout_2.addLayout(self.tx_baseband_gain_layout)
        ##########

        self.com_port_top_label = QtWidgets.QLabel(self.central_widget)
        self.com_port_top_label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.com_port_top_label.setAlignment(QtCore.Qt.AlignCenter)
        self.com_port_top_label.setObjectName("com_port_top_label")
        self.vertical_layout_2.addWidget(self.com_port_top_label)
        self.com_port_line = QtWidgets.QLineEdit(self.central_widget)
        self.com_port_line.setMaximumSize(QtCore.QSize(16777215, 20))
        self.com_port_line.setObjectName("com_port_line")
        self.vertical_layout_2.addWidget(self.com_port_line)
        ##########
        self.spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_2.addItem(self.spacer_item)
        self.send_all_button = QtWidgets.QPushButton(self.central_widget)
        self.send_all_button.setMaximumSize(QtCore.QSize(16777215, 23))
        self.send_all_button.setToolTip("")
        self.send_all_button.setObjectName("send_all_button")
        self.vertical_layout_2.addWidget(self.send_all_button)
        self.grid_layout.addLayout(self.vertical_layout_2, 5, 2, 2, 1)
        self.top_side_horizontal_layout = QtWidgets.QHBoxLayout()
        self.top_side_horizontal_layout.setObjectName("top_side_horizontal_layout")
        self.setups_label = QtWidgets.QLabel(self.central_widget)
        self.setups_label.setObjectName("setups_label")
        self.top_side_horizontal_layout.addWidget(self.setups_label)
        self.setups_combo_box = QtWidgets.QComboBox(self.central_widget)
        self.setups_combo_box.setMinimumSize(QtCore.QSize(150, 23))
        self.setups_combo_box.setMaximumSize(QtCore.QSize(300, 23))
        self.setups_combo_box.setEditable(True)
        self.setups_combo_box.setObjectName("setups_combo_box")
        self.setups_combo_box.addItem("")
        self.setups_combo_box.setItemText(0, "")
        self.setups_combo_box.addItem("")
        self.top_side_horizontal_layout.addWidget(self.setups_combo_box)
        self.del_button = QtWidgets.QPushButton(self.central_widget)
        self.del_button.setMinimumSize(QtCore.QSize(0, 0))
        self.del_button.setMaximumSize(QtCore.QSize(30, 23))
        self.del_button.setCheckable(False)
        self.del_button.setAutoDefault(False)
        self.del_button.setObjectName("del_button")
        self.top_side_horizontal_layout.addWidget(self.del_button)
        self.spacer_item1 = QtWidgets.QSpacerItem(40, 20,
                                                  QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.top_side_horizontal_layout.addItem(self.spacer_item1)
        self.connection_status_label = QtWidgets.QLabel(self.central_widget)
        self.connection_status_label.setObjectName("connection_status_label")
        self.top_side_horizontal_layout.addWidget(self.connection_status_label)
        self.connection_label = QtWidgets.QLabel(self.central_widget)
        self.connection_label.setObjectName("connection_label")
        self.top_side_horizontal_layout.addWidget(self.connection_label)
        self.spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                  QtWidgets.QSizePolicy.Minimum)
        self.top_side_horizontal_layout.addItem(self.spacer_item2)
        self.lock_label = QtWidgets.QLabel(self.central_widget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lock_label.setFont(font)
        self.lock_label.setTextFormat(QtCore.Qt.AutoText)
        self.lock_label.setObjectName("lock_label")
        self.top_side_horizontal_layout.addWidget(self.lock_label)
        self.lock_check_box = QtWidgets.QCheckBox(self.central_widget)
        self.lock_check_box.setText("")
        self.lock_check_box.setObjectName("lock_check_box")
        self.top_side_horizontal_layout.addWidget(self.lock_check_box)
        self.grid_layout.addLayout(self.top_side_horizontal_layout, 0, 0, 1, 4)
        line_3 = QtWidgets.QFrame(self.central_widget)
        line_3.setFrameShape(QtWidgets.QFrame.HLine)
        line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        line_3.setObjectName("line_3")
        self.grid_layout.addWidget(line_3, 1, 1, 1, 3)
        self.rf_vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.rf_vertical_layout_1.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.rf_vertical_layout_1.setObjectName("rf_vertical_layout_1")
        self.rf_frequency_top_label = QtWidgets.QLabel(self.central_widget)
        self.rf_frequency_top_label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.rf_frequency_top_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rf_frequency_top_label.setOpenExternalLinks(False)
        self.rf_frequency_top_label.setObjectName("rf_frequency_top_label")
        self.rf_vertical_layout_1.addWidget(self.rf_frequency_top_label)
        self.rf_frequency_layout = QtWidgets.QHBoxLayout()
        self.rf_frequency_layout.setObjectName("rf_frequency_layout")
        self.rf_frequency_line = QtWidgets.QLineEdit(self.central_widget)
        self.rf_frequency_line.setMaximumSize(QtCore.QSize(100, 20))
        self.rf_frequency_line.setObjectName("rf_frequency_line")
        self.rf_frequency_layout.addWidget(self.rf_frequency_line)
        self.rf_frequency_label = QtWidgets.QLabel(self.central_widget)
        self.rf_frequency_label.setObjectName("rf_frequency_label")
        self.rf_frequency_layout.addWidget(self.rf_frequency_label)
        self.rf_vertical_layout_1.addLayout(self.rf_frequency_layout)
        self.rf_frequency_scroll_bar = QtWidgets.QScrollBar(self.central_widget)
        self.rf_frequency_scroll_bar.setMaximumSize(QtCore.QSize(16777215, 20))
        self.rf_frequency_scroll_bar.setMinimum(4900)
        self.rf_frequency_scroll_bar.setMaximum(5900)
        self.rf_frequency_scroll_bar.setPageStep(1)
        self.rf_frequency_scroll_bar.setSingleStep(1)
        self.rf_frequency_scroll_bar.setInvertedControls(False)
        self.rf_frequency_scroll_bar.setOrientation(QtCore.Qt.Horizontal)
        self.rf_frequency_scroll_bar.setObjectName("rf_frequency_scroll_bar")
        self.rf_vertical_layout_1.addWidget(self.rf_frequency_scroll_bar)
        self.padac_output_bias_top_label = QtWidgets.QLabel(self.central_widget)
        self.padac_output_bias_top_label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.padac_output_bias_top_label.setAlignment(QtCore.Qt.AlignCenter)
        self.padac_output_bias_top_label.setObjectName("padac_output_bias_top_label")
        self.rf_vertical_layout_1.addWidget(self.padac_output_bias_top_label)
        self.padac_output_bias_layout = QtWidgets.QHBoxLayout()
        self.padac_output_bias_layout.setObjectName("padac_output_bias_layout")
        self.padac_output_bias_line = QtWidgets.QLineEdit(self.central_widget)
        self.padac_output_bias_line.setMaximumSize(QtCore.QSize(100, 20))
        self.padac_output_bias_line.setObjectName("padac_output_bias_line")
        self.padac_output_bias_layout.addWidget(self.padac_output_bias_line)
        self.padac_output_bias_label = QtWidgets.QLabel(self.central_widget)
        self.padac_output_bias_label.setObjectName("padac_output_bias_label")
        self.padac_output_bias_layout.addWidget(self.padac_output_bias_label)
        self.rf_vertical_layout_1.addLayout(self.padac_output_bias_layout)
        self.padac_output_bias_scroll_bar = QtWidgets.QScrollBar(self.central_widget)
        self.padac_output_bias_scroll_bar.setMaximumSize(QtCore.QSize(16777215, 20))
        self.padac_output_bias_scroll_bar.setMaximum(315)
        self.padac_output_bias_scroll_bar.setInvertedControls(False)
        self.padac_output_bias_scroll_bar.setPageStep(1)
        self.padac_output_bias_scroll_bar.setSingleStep(1)
        self.padac_output_bias_scroll_bar.setOrientation(QtCore.Qt.Horizontal)
        self.padac_output_bias_scroll_bar.setObjectName("padac_output_bias_scroll_bar")
        self.rf_vertical_layout_1.addWidget(self.padac_output_bias_scroll_bar)
        line_2 = QtWidgets.QFrame(self.central_widget)
        line_2.setFrameShape(QtWidgets.QFrame.HLine)
        line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        line_2.setObjectName("line_2")
        self.rf_vertical_layout_1.addWidget(line_2)
        self.max2828_top_label = QtWidgets.QLabel(self.central_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.max2828_top_label.setFont(font)
        self.max2828_top_label.setObjectName("self.max2828_top_label")
        self.rf_vertical_layout_1.addWidget(self.max2828_top_label, 0, QtCore.Qt.AlignHCenter)
        self.max2828_combo_box = QtWidgets.QComboBox(self.central_widget)
        self.max2828_combo_box.setObjectName("self.max2828_combo_box")
        self.max2828_combo_box.addItem("")
        self.max2828_combo_box.addItem("")
        self.max2828_combo_box.addItem("")
        self.max2828_combo_box.addItem("")
        self.rf_vertical_layout_1.addWidget(self.max2828_combo_box)
        self.max5866_top_label = QtWidgets.QLabel(self.central_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.max5866_top_label.setFont(font)
        self.max5866_top_label.setObjectName("self.max5866_top_label")
        self.rf_vertical_layout_1.addWidget(self.max5866_top_label, 0, QtCore.Qt.AlignHCenter)
        self.max5866_combo_box = QtWidgets.QComboBox(self.central_widget)
        self.max5866_combo_box.setEditable(False)
        self.max5866_combo_box.setObjectName("max5866_combo_box")
        self.max5866_combo_box.addItem("")
        self.max5866_combo_box.addItem("")
        self.max5866_combo_box.addItem("")
        self.max5866_combo_box.addItem("")
        self.max5866_combo_box.addItem("")
        self.rf_vertical_layout_1.addWidget(self.max5866_combo_box)
        spacer_item3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.rf_vertical_layout_1.addItem(spacer_item3)
        self.grid_layout.addLayout(self.rf_vertical_layout_1, 5, 1, 2, 1)
        line = QtWidgets.QFrame(self.central_widget)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setObjectName("line")
        self.grid_layout.addWidget(line, 1, 0, 1, 1)
        line_4 = QtWidgets.QFrame(self.central_widget)
        line_4.setFrameShape(QtWidgets.QFrame.HLine)
        line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        line_4.setObjectName("line_4")
        self.grid_layout.addWidget(line_4, 7, 1, 1, 2)
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 21))
        self.menubar.setObjectName("menubar")
        self.menu_exit = QtWidgets.QMenu(self.menubar)
        self.menu_exit.setObjectName("menu_exit")
        MainWindow.setMenuBar(self.menubar)
        statusbar = QtWidgets.QStatusBar(MainWindow)
        statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(statusbar)
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.menu_exit.addAction(self.action_exit)
        self.menubar.addAction(self.menu_exit.menuAction())

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Programming-Control Interface v1.0"))
        self.rxlna_gain_top_label.setText(_translate("MainWindow", "RX LNA Gain"))
        self.rxlna_gain_combobox.setItemText(0, _translate("MainWindow", "Min"))
        self.rxlna_gain_combobox.setItemText(1, _translate("MainWindow", "Mid"))
        self.rxlna_gain_combobox.setItemText(2, _translate("MainWindow", "Max"))
        self.rxvga_gain_top_label.setText(_translate("MainWindow", "RX VGA Gain"))
        self.rxvga_gain_line.setText(_translate("MainWindow", "0"))
        self.rxvga_gain_scroll_bar.setStatusTip(_translate("MainWindow", "Change to RX VGA Gain"))
        self.txvga_gain_top_label.setText(_translate("MainWindow", "TX VGA Gain"))
        self.txvga_gain_line.setText(_translate("MainWindow", "0"))
        self.com_port_top_label.setText(_translate("MainWindow", "Enter COM PORT"))
        self.com_port_line.setText(_translate("MainWindow", "COM3"))
        self.com_port_top_label.setStatusTip(_translate("MainWindow", "COM3 is Default"))
        self.com_port_line.setStatusTip(_translate("MainWindow", "COM3 is Default"))
        self.txvga_gain_scroll_bar.setStatusTip(_translate("MainWindow", "Change to TX VGA Gain"))
        self.tx_baseband_gain_top_label.setText(_translate("MainWindow", "TX Baseband Gain"))
        self.tx_baseband_gain_combo_box.setItemText(0, _translate("MainWindow", "-5.0"))
        self.tx_baseband_gain_combo_box.setItemText(1, _translate("MainWindow", "Max Gain"))
        self.tx_baseband_gain_label.setText(_translate("MainWindow", "dB"))
        self.send_all_button.setStatusTip(_translate("MainWindow", "It sends bytes"))
        self.send_all_button.setText(_translate("MainWindow", "Send All"))
        self.setups_label.setText(_translate("MainWindow", "Setups: "))
        self.setups_combo_box.setItemText(1, _translate("MainWindow", "Last Power Down"))
        self.del_button.setStatusTip(_translate("MainWindow", "Delete"))
        self.del_button.setText(_translate("MainWindow", "Del"))
        self.connection_status_label.setStatusTip(_translate("MainWindow", "Connection Status"))
        self.connection_status_label.setText(_translate("MainWindow", "Connection Status:"))
        self.connection_label.setText(_translate("MainWindow", "No Device"))
        self.connection_label.setStatusTip(_translate("MainWindow", "Connection"))
        self.lock_label.setStatusTip(_translate("MainWindow", "Lock"))
        self.lock_label.setText(_translate("MainWindow", "Lock: "))
        self.lock_check_box.setStatusTip(_translate("MainWindow", "Lock"))
        self.rf_frequency_top_label.setText(_translate("MainWindow", "RF Frequency"))
        self.rf_frequency_line.setText(_translate("MainWindow", "0"))
        self.rf_frequency_label.setText(_translate("MainWindow", "Mhz"))
        self.rf_frequency_scroll_bar.setStatusTip(_translate("MainWindow", "Change to RF Frequency"))
        self.padac_output_bias_top_label.setText(_translate("MainWindow", "PA DAC Output Bias"))
        self.padac_output_bias_line.setText(_translate("MainWindow", "0"))
        self.padac_output_bias_label.setText(_translate("MainWindow", "uA"))
        self.padac_output_bias_scroll_bar.setStatusTip(_translate("MainWindow", "Change to PA DAC Output Bias"))
        self.max2828_top_label.setText(_translate("MainWindow", "Max2828"))
        self.max2828_combo_box.setStatusTip(_translate("MainWindow", "Change to Max2828 Mode(Default)"))
        self.max2828_combo_box.setItemText(0, _translate("MainWindow", "Receiver"))
        self.max2828_combo_box.setItemText(1, _translate("MainWindow", "Transmitter"))
        self.max2828_combo_box.setItemText(2, _translate("MainWindow", "IDLE"))
        self.max2828_combo_box.setItemText(3, _translate("MainWindow", "Standby"))
        self.max5866_top_label.setText(_translate("MainWindow", "Max5866"))
        self.max5866_combo_box.setStatusTip(_translate("MainWindow", "Change to Max5866 Mode"))
        self.max5866_combo_box.setItemText(0, _translate("MainWindow", "Shutdown"))
        self.max5866_combo_box.setItemText(1, _translate("MainWindow", "IDLE"))
        self.max5866_combo_box.setItemText(2, _translate("MainWindow", "RX"))
        self.max5866_combo_box.setItemText(3, _translate("MainWindow", "TX"))
        self.max5866_combo_box.setItemText(4, _translate("MainWindow", "Standby"))
        self.menu_exit.setTitle(_translate("MainWindow", "Exit"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        line_edit_name = QtWidgets.QLineEdit()
        scroll_bar_name = QtWidgets.QScrollBar()


class MainWindow(QtWidgets.QMainWindow, Window):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_ui(self)

        # Connect scroll bars to functions
        self.rf_frequency_scroll_bar.valueChanged.connect(
            lambda: self.scroll_bar_value(self.rf_frequency_scroll_bar, self.rf_frequency_line))
        self.padac_output_bias_scroll_bar.valueChanged.connect(
            lambda: self.scroll_bar_value(self.padac_output_bias_scroll_bar, self.padac_output_bias_line))
        self.rxvga_gain_scroll_bar.valueChanged.connect(
            lambda: self.scroll_bar_value(self.rxvga_gain_scroll_bar, self.rxvga_gain_line))
        self.txvga_gain_scroll_bar.valueChanged.connect(
            lambda: self.scroll_bar_value(self.txvga_gain_scroll_bar, self.txvga_gain_line))


'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Window.MainWindow = QtWidgets.QMainWindow
    main_window = QtWidgets.QMainWindow()
    ui = Window()
    ui.setup_ui(main_window)
    main_window.show()

    sys.exit(app.exec_()) '''
