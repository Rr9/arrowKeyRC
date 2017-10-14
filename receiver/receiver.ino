#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

int DRIVE = 3;//D3 - PWM - Drive Motor
int TURN = 5;//D5 - PWM - Turn Motor

//Drive motor - D2, D4
int DriveA = 2;
int DriveB = 4;
//Turn motor - D9, D10
int TurnA = 9;
int TurnB = 10;

RF24 radio(7, 8); //CE CNS
byte address[][6] = {"0"}; //pipe adress 

void setup() {
  Serial.begin(9600);
  delay(1000);
  
  radio.begin();
  radio.setChannel(115);
  radio.setPALevel(RF24_PA_MIN);
  radio.setDataRate(RF24_250KBPS);
  radio.openReadingPipe(1, address[0]);
  radio.startListening();

  pinMode(DRIVE, OUTPUT);
  pinMode(TURN, OUTPUT);
  pinMode(DriveA, OUTPUT);
  pinMode(DriveB, OUTPUT);
  pinMode(TurnA, OUTPUT);
  pinMode(TurnB, OUTPUT);
}

void loop() {
  char text[4] = "g11";  
  
  if( radio.available() ){
    while(radio.available()){
      radio.read(&text, sizeof(text));
    }
    Serial.println(text);
  }

  //DRIVE
  if(text[1] == 0){
    analogWrite(DRIVE, 255);
    digitalWrite(DriveA, HIGH);
    digitalWrite(DriveB, LOW);  
  }else if(text[1] == 2){
    analogWrite(DRIVE, 255);
    digitalWrite(DriveA, LOW);
    digitalWrite(DriveB, HIGH);  
  }else{
    analogWrite(DRIVE, 0);
  }

  //TURN
  if(text[2] == 0){
    analogWrite(TURN, 127);
    digitalWrite(TurnA, HIGH);
    digitalWrite(TurnB, LOW);  
  }else if(text[2] == 2){
    analogWrite(TURN, 127);
    digitalWrite(TurnA, LOW);
    digitalWrite(TurnB, HIGH);  
  }else{
    analogWrite(TURN, 0);
  }

  
  delay(200);
}



