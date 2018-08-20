
char starter_byte     = 0XAA;
char source_byte      = 0X01;
char destination_byte = 0X02;
char command_byte     = 0XBB;
char zero_byte        = 0X00;
char pack[12];
char sourceReturn();
char destReturn();
char sourceValue;
char destValue;
int ndx = 0;
int mdx = 0;

                
void setup() {
Serial.begin(9600);
while(!Serial){;}
}

void loop() { 
       char Ack[12] = {starter_byte, source_byte, destination_byte, command_byte,
                zero_byte, zero_byte, zero_byte, zero_byte, 
                zero_byte, zero_byte, zero_byte, zero_byte};
       while(Serial.available() ){  
        char rb = Serial.read();
        pack[ndx] = rb;        
        if(pack[0] == char(0XAA)) {
          source_byte = char(pack[2]);
          destination_byte = char(pack[1]);
          Serial.write(pack[ndx]);
          ndx++;}
        if(ndx == 12){
            for(int i = 0; i < 12; i++)
            Serial.write(char(Ack[i])); 
            ndx=0;
          } 
             
        }
              
  }


  
     
  
