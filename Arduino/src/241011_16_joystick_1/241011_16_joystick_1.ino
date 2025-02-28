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

  int x_pos = map(x, ZERO_POS * -1, ZERO_POS, 180, 0);
  servo.write(x_pos);
  Serial.println(x_pos);

  delay(150);
}
