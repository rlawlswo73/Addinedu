#include <Servo.h>

Servo servo;

int pos = 0;
int sign = 1;
int button = 2;
bool flag = true;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(9);
  pinMode(button, INPUT);
  servo.write(0);
}

void loop() {
  // put your main code here, to run repeatedly:
  int push = digitalRead(button);
  if (push == HIGH && flag == true) {
    flag = false;
    if (pos == 180) {
      sign = -1;
    } else if (pos == 0) {
      sign = 1;
    }
    pos += sign * 10;
    servo.write(pos);
    delay(50);
  } else  if(push == LOW && flag == false) {
    flag = true;
  }
}