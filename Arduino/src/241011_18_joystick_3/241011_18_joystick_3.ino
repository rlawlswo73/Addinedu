#include <Servo.h>

const int X_AXIS = A0;
const int Y_AXIS = A1;
const int ZERO_POS = 512;
const int SERVO_PIN = 11;

Servo servo;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(SERVO_PIN);
}

void loop() {
  // put your main code here, to run repeatedly:
  int x = analogRead(X_AXIS);
  int y = analogRead(Y_AXIS);

  x = x - ZERO_POS;
  y = (y - ZERO_POS) * -1;

  double degree = atan2(x, y) * 180 / PI;
  
  if(degree < 0) {
    degree = degree * -1;
  }

  servo.write(180 - degree);

  Serial.println(degree);
  delay(100);
}
