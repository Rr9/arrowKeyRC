#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8); // CNS, CE
byte address[][6] = {"0"}; //pipe adress 

int fr = 1;
int rl = 1;

void setup() {
  Serial.begin(9600);
  delay(1000);
  
  radio.begin();
  radio.setChannel(115);
  radio.setPALevel(RF24_PA_MIN);
  radio.setDataRate(RF24_250KBPS);
  radio.openWritingPipe(address[0]);
  //radio.stopListening(); //sets transmitter
}

void loop() {
  
  char text[3];
  text[2] = '\0';
  
  if( Serial.available() >0 ){
      if( Serial.peek() == 'g'){
        Serial.read();
        text[0] = Serial.read();
        text[1] = Serial.read();
        Serial.println(text);
        radio.write(&text, sizeof(text));
      }else{
        Serial.read();
      }
  }
  
  delay(250);
}
