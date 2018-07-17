#include <SoftwareSerial.h>
SoftwareSerial BTSerial(10, 11); // RX, TX
char ligar;

#define LED = 5
int tempo = 10;
int brilho = 128;

int button1Pin = 7;
int button2Pin = 8;
int button3Pin = 9;


int button1State = 0;
int button2State = 0;
int button3State = 0;

void setup() {
  pinMode(button1Pin, INPUT);
  pinMode(button2Pin, INPUT);
  pinMode(button3Pin, INPUT);
  pinMode(5, OUTPUT);
  BTSerial.begin(38400);
  Serial.begin(57600);
}

void loop() {
  button1State = digitalRead(button1Pin);
  button2State = digitalRead(button2Pin);
  button3State = digitalRead(button3Pin);


  if (button1State == HIGH) {
    Serial.print("1");
    delay(1500);
  }

  if (button2State == HIGH) {
    Serial.print("2");
    delay(1500);
  }

  if (button3State == HIGH) {
    Serial.print("3");
    delay(1500);
  }

  if (Serial.available() > 0) {
    ligar = Serial.read();
    if (ligar == 'A') {
      BTSerial.write(ligar);
      while (true) {
        for (int i = 0; i < brilho; i++) {
          analogWrite(5, i);
          delay(tempo);
        }

        for (int i = brilho; i > 0; i --) {
          analogWrite(5, i);
          delay(tempo);
        }

        if (BTSerial.available() > 0) {
          if (BTSerial.read() == 'a') {
            Serial.write('4');
            digitalWrite(5, LOW);
            break;
          }
        }
      }
    }
  }
}
