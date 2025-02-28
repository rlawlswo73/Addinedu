const int X_AXIS = A0;
const int Y_AXIS = A1;
const int ZERO_POS = 512;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int x = analogRead(X_AXIS);
  int y = analogRead(Y_AXIS);

  x = x - ZERO_POS;
  y = (y - ZERO_POS) * -1;

  double degree = atan2(x, y) * 180 / PI;
  Serial.println(degree);
  delay(150);
}
