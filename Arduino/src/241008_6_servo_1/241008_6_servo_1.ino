#include <Servo.h>

Servo servo;

int pos = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(9);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(pos = 10; pos <= 180; pos++) {
    servo.write(pos);
    delay(15);
  }

  // servo.write(0);
  // delay(15);
  for(pos = 180; pos >= 0; pos--) {
    servo.write(pos);
    delay(15);
  }
}
