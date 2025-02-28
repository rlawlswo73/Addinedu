const int SOUND_PIN = A0;
const int LED_PIN = 3;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int level = analogRead(SOUND_PIN) * 2;

  if(level > 255) {
    level = 255;
  }
  if (level < 130) {
    level = 0;
  }
  analogWrite(LED_PIN, level);
  Serial.println(level);
  delay(100);
}
