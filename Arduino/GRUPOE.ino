int red_pin = 3;
int green_pin = 5;
int blue_pin = 6;

const int bverde = 11;
const int bvermelho = 8;
const int bbranco = 9;
const int bamarelo = 12;
const int bazul = 10;

int buttonState = 0;
int buttonState1 = 0;
int buttonState2 = 0;
int buttonState3 = 0;
int buttonState4 = 0;
int e = 0;


void setup() {
  Serial.begin(9600);
  pinMode(red_pin, OUTPUT);
  pinMode(green_pin, OUTPUT);
  pinMode(blue_pin, OUTPUT);

  pinMode(bverde, INPUT);
  pinMode(bvermelho, INPUT);
  pinMode(bbranco, INPUT);
  pinMode(bamarelo, INPUT);
  pinMode(bazul, INPUT);
}

void alternateBlueGreen() {
  int done = 0;

  while (1) {
    for (int i = 0; i <= 255; i++) {
      analogWrite(blue_pin , 0);
      analogWrite(red_pin , 0);
      analogWrite(green_pin, i);
      delay(10);
      buttonState4 = digitalRead(bazul);
      buttonState = digitalRead(bverde);
      if ((buttonState4 == HIGH) || (buttonState == HIGH)) {
        done = 1;
        break; //Sai do for
      }
    }
    if (done) break; //Sai do while True
    for (int i = 255; i >=0 ; i--) {
      analogWrite(blue_pin , 0);
      analogWrite(red_pin , 0);
      analogWrite(green_pin, i);
      delay(10);
      buttonState4 = digitalRead(bazul);
      buttonState = digitalRead(bverde);
      if ((buttonState4 == HIGH) || (buttonState == HIGH)) {
        done = 1;
        break; //Sai do for
      }
    }
    if (done) break; //Sai do while True
    for (int i = 0; i <= 255; i++) {
      analogWrite(blue_pin , i);
      analogWrite(red_pin , 0);
      analogWrite(green_pin, 0);
      delay(10);
      buttonState4 = digitalRead(bazul);
      buttonState = digitalRead(bverde);
      if ((buttonState4 == HIGH) || (buttonState == HIGH)) {
        done = 1;
        break; //Sai do for
      }
    }
    if (done) break; //Sai do while True
    for (int i = 255; i >= 0; i--) {
      analogWrite(blue_pin , i);
      analogWrite(red_pin , 0);
      analogWrite(green_pin, 0);
      delay(10);
      buttonState4 = digitalRead(bazul);
      buttonState = digitalRead(bverde);
      if ((buttonState4 == HIGH) || (buttonState == HIGH)) {
        done = 1;
        break; //Sai do for
      }
    }
    if (done) break; //Sai do while True
  }
}

void loop() {
  buttonState = digitalRead(bverde);
  buttonState1 = digitalRead(bvermelho);
  buttonState2 = digitalRead(bbranco);
  buttonState3 = digitalRead(bamarelo);
  buttonState4 = digitalRead(bazul);

  if (Serial.available()) {
    if (Serial.read() == '5') {
      alternateBlueGreen();
    }
  }
  if (buttonState == HIGH) {
    e = 6;
    analogWrite(green_pin, 255);
    analogWrite(red_pin , 0);
    analogWrite(blue_pin, 0);
    Serial.write("2");
    delay(1000);
  }

  if (buttonState1 == HIGH) {
    analogWrite (red_pin , 255);
    analogWrite(blue_pin , 0);
    analogWrite(green_pin, 0);
    Serial.write("3");
    delay(1000);
  }
  if (buttonState2 == HIGH )  {
    e = 7;
    analogWrite (green_pin , 255);
    analogWrite (blue_pin , 255);
    analogWrite (red_pin , 255);
    Serial.write("0");
    delay(1000);
  }
  if (buttonState3 == HIGH ) {
    analogWrite (red_pin , 255);
    analogWrite (green_pin , 255);
    analogWrite(blue_pin , 0);
    Serial.write("4");
    delay(2000);
    if (e == 6) {
      analogWrite (blue_pin , 0);
      analogWrite(red_pin , 0);
      analogWrite(green_pin, 255);
    }
    if (e == 7) {
      analogWrite (blue_pin , 255);
      analogWrite(red_pin , 255);
      analogWrite(green_pin, 255);
    }
    if (e == 8) {
      analogWrite (blue_pin , 255);
      analogWrite(red_pin , 0);
      analogWrite(green_pin, 0);
    }
  }

  if (buttonState4 == HIGH) {
    e = 8;
    analogWrite (blue_pin , 255);
    analogWrite(red_pin , 0);
    analogWrite(green_pin, 0);
    Serial.write("1");
    delay(1000);
  }
}
