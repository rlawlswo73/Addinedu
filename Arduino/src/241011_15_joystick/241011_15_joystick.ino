const int X_AXIS = A0;
const int Y_AXIS = A1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(analogRead(X_AXIS));
  Serial.print(", ");
  Serial.println(analogRead(Y_AXIS));

  delay(150);
}
