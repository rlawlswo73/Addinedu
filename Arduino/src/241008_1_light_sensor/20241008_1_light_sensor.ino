const int LED_PIN = 9;
int max = 0;
int min = 9999;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
}



void loop() {
  // put your main code here, to run repeatedly:
  int light = analogRead(A0);

  if (max < light) {
    max = light;
  }

  if (min > light) {
    min = light;
  }

  int output = map(light, min, max, 250, 0);

  analogWrite(LED_PIN, output);
  Serial.print(output);
  Serial.print(", ");
  Serial.print(min);
  Serial.print(", ");
  Serial.println(max);

  delay(100);
}
