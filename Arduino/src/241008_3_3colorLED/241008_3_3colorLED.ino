const int R_PIN = 3;
const int G_PIN = 5;
const int B_PIN = 6;

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i = 0; i < 255; i++) {
    analogWrite(R_PIN, i);
    analogWrite(G_PIN, i);
    analogWrite(B_PIN, i);
    delay(10);
  }
}
