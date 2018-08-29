
char starter_byte     = 0XAA;
char source_byte      = 0X01;
char destination_byte = 0X02;
char command_byte     ;
char ack_byte        = 0X01;
int ndx = 0;
char pack[12];
char pack_ack[5];
bool checkStarter(char myByte){
  if (char(myByte) == char(0XAA)) return true; //else return false;
  }
bool checkSource(char myByte){
  if (char(myByte) == char(0X01)) return true; //else return false;
  } 
bool checkDest(char myByte){
  if (char(myByte) == char(0X02)) return true;  //else return false;//It will work just for max2828
  }   
bool checkCommand(char myByte){
  if (char(myByte) >= char(0X01) && myByte <= char(0X07)) return true; // //else return false;
  } 
bool checkCommand1(char myByte1, char myByte2){ //RFFrequency
  int myInt1 = atoi(myByte1);
  int myInt2 = atoi(myByte2);
  int myInt = myInt1*100+myByte2;
  if (myInt >= 4900 && myInt <= 5900) return true;  //else return false;
  }
bool checkCommand2(char myByte1, char myByte2){ //PADAC
  int myInt1 = atoi(myByte1);
  int myInt2 = atoi(myByte2);
  int myInt = myInt1*100+myByte2;
  if (myInt >= 0 && myInt <= 512) return true;  //else return false;
  }
bool checkCommand3(char myByte){ //RX VGA Gain
  if (char(myByte) >= char(0X00) && myByte <= char(0X20)) return true; // //else return false;
  }
bool checkCommand4(char myByte){ //TX VGA Gain
  if (char(myByte) >= char(0X00) && myByte <= char(0X40)) return true;  //else return false;
  }
bool checkCommand5(char myByte){ //RX LNA Gain
  if (char(myByte) >= char(0X00) && myByte <= char(0X02)) return true;  //else return false;
  }
bool checkCommand6(char myByte){ //TX LNA Gain
  if (char(myByte) >= char(0X00) && myByte <= char(0X01)) return true;  //else return false;
  }
bool checkCommand7(char myByte){ //Device
  if ((char(myByte) >= char(0X02) && myByte <= char(0X03)) || char(myByte) == char(0X00)) return true;  //else return false;
  }
bool checkCommandTotal(int param, char myByte1, char myByte2){
  switch(param){
    case 1: if(checkCommand1(myByte1,myByte2)); return true; break;
    case 2: if(checkCommand2(myByte1,myByte2)); return true; break;
    case 3: if(checkCommand3(myByte2)); return true; break;
    case 4: if(checkCommand4(myByte2)); return true; break;
    case 5: if(checkCommand5(myByte2)); return true; break;
    case 6: if(checkCommand6(myByte2)); return true; break;
    case 7: if(checkCommand7(myByte2)); return true; break;
    default: return 0;
    }
  }
void prepare_ack(){
  pack_ack[0] = pack[0];
  pack_ack[1] = pack[2];
  pack_ack[2] = pack[1];
  pack_ack[3] = pack[3];
  pack_ack[4] = ack_byte;
  }
int state = 0;
int current_byte = 0;
int packNum = 0;      
void setup() {
  Serial.begin(9600);
  while(!Serial){;}
  state = 0;
  current_byte = 0;
  packNum = 0;
  ack_byte  = 0X01;
  pinMode(13, OUTPUT);
  //digitalWrite(13,LOW);
}

void loop() {
        switch (state){
          case 0:
            if(Serial.available() > 0){              
              pack[0] = Serial.read();
              if(char(pack[0]) == char(0xAA)){
                //Working
                state = 1;
                current_byte = 1;
              }
            }
            break;
          case 1:
            if(Serial.available() > 0){
              pack[current_byte]= Serial.read();
              current_byte++;
              if(current_byte == 12){
                state = 2;
                packNum++;
              }
            }
            break;
          case 2:
            if(checkCommandTotal(packNum, pack[4], pack[5])){
              digitalWrite(13,HIGH);
            }
            if(checkStarter(pack[0]) && checkSource(pack[1]) && checkDest(pack[2]) && checkCommand(pack[3])){
              //working
              ack_byte = 0X01;
              state = 3;
            }else{
              ack_byte = 0X00;
              state = 7;
            }
            break;
          case 3:
            prepare_ack();
            state = 4;
            current_byte = 0;
            break;
          case 4:
            Serial.write(pack_ack[current_byte]);
            current_byte++;
            if(current_byte == 5){
              state = 0;
            }
            break;
          }
   
  }


  
     
  
