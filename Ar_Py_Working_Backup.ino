
char starter_byte     = 0XAA;
char source_byte      = 0X01;
char destination_byte = 0X02;
char command_byte     ;
char ack_byte        = 0X01;
int ndx = 0;
char pack[12];
boolean starterReceived;
bool checkStarter(char myByte){
  if (char(myByte) == char(0XAA)) return true;
  }
bool checkSource(char myByte){
  if (char(myByte) == char(0X01)) return true;
  } 
bool checkDest(char myByte){
  if (char(myByte) == char(0X02)) return true; //It will work just for max2828
  }   
bool checkCommand(char myByte){
  if (char(myByte) >= char(0X01) && myByte <= char(0X07)) return true;
  } 
      
void setup() {
Serial.begin(9600);
while(!Serial){;}
}

void loop() { 
     
       while(Serial.available()){
        /*for(int i = 0; i<=11 ; i++){
        char rb = Serial.read();
        pack[i] = rb; } */
        char rb = Serial.read();
        pack[ndx] = rb;
        if(checkStarter(pack[0])){        
           ndx++;}
        starter_byte     = pack[0];
        source_byte      = pack[2];
        destination_byte = pack[1];
        command_byte     = pack[3];
        ack_byte         = char(0X01);
        char Ack[5] = {starter_byte, source_byte, destination_byte, command_byte, ack_byte};
        if(ndx == 12 && checkStarter(pack[0]) && checkSource(pack[1]) && checkDest(pack[2]) && checkCommand(pack[3]) ){
            for(int i = 0; i < 5; i++)
            Serial.write(char(Ack[i])); 
            ndx=0;
          }
          else if(ndx == 12 ){
             ack_byte = char(0X00);
             char Ack[5] = {starter_byte, source_byte, destination_byte, command_byte, ack_byte};
             for(int i = 0; i < 5; i++)
             Serial.write(char(Ack[i])); 
             ndx=0;
          }
                   
        }
              
  }


  
     
  
