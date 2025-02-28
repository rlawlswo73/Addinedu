const int SOUND_PIN = A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int sound_level = analogRead(SOUND_PIN);
  Serial.println(sound_level);
  delay(50);
}
