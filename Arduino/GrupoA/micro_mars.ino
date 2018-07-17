#include <SoftwareSerial.h>
#include <Servo.h>

int led = 9;
SoftwareSerial BTSerial(10, 11); //rx e tx
Servo myServo;
int servopos, pos = 0, switchPin = 12, switchState = 0;
char btState = '0';

void setup() {
  myServo.attach(9);
  Serial.begin(9600);
  BTSerial.begin(38400);
  myServo.write(0);
  pinMode (switchPin,INPUT);
}

void loop() {
   if (BTSerial.available()){
    btState = BTSerial.read();
    
    while (btState == 'A') {
      servopos = servopos + 10;
      delay(75);
      myServo.write(servopos);

      if (servopos == 60 )
      {
        while (servopos > 0)
        {
          servopos = servopos - 10;
          delay(75);
          myServo.write(servopos);
        }
      }
      
      switchState = digitalRead(switchPin);
      if (switchState == LOW) {
      btState = '0';
      BTSerial.write('a');
      servopos = 0;
      myServo.write(servopos);
      delay(500);
      }
    }
  }
}
