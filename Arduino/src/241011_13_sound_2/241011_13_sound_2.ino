const int SOUND_PIN = A0;
const int LED_PIN_1 = 2;
const int LED_PIN_2 = 3;
const int LED_PIN_3 = 4;
const int LED_PIN_4 = 5;
const int LED_PIN_5 = 6;
const int LED_PIN_6 = 7;
const int LED_PIN_7 = 8;
const int LED_PIN_8 = 9;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_PIN_1, OUTPUT);
  pinMode(LED_PIN_2, OUTPUT);
  pinMode(LED_PIN_3, OUTPUT);
  pinMode(LED_PIN_4, OUTPUT);
  pinMode(LED_PIN_5, OUTPUT);
  pinMode(LED_PIN_6, OUTPUT);
  pinMode(LED_PIN_7, OUTPUT);
  pinMode(LED_PIN_8, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  // int output = analogRead(SOUND_PIN);
  // int level_class = 255 / 8;
  // int level = map(output, 0, 512, 0, 255);

  // if (level_class >= level) {
  //   digitalWrite(LED_PIN_1, LOW);
  //   digitalWrite(LED_PIN_2, LOW);
  //   digitalWrite(LED_PIN_3, LOW);
  //   digitalWrite(LED_PIN_4, LOW);
  //   digitalWrite(LED_PIN_5, LOW);
  //   digitalWrite(LED_PIN_6, LOW);
  //   digitalWrite(LED_PIN_7, LOW);
  //   digitalWrite(LED_PIN_8, HIGH);
  // } else if (level_class * 2  >= level) {
  //   digitalWrite(LED_PIN_1, LOW);
  //   digitalWrite(LED_PIN_2, LOW);
  //   digitalWrite(LED_PIN_3, LOW);
  //   digitalWrite(LED_PIN_4, LOW);
  //   digitalWrite(LED_PIN_5, LOW);
  //   digitalWrite(LED_PIN_6, LOW);
  //   digitalWrite(LED_PIN_7, HIGH);
  //   digitalWrite(LED_PIN_8, HIGH);
  // } else if (level_class * 3  >= level) {
  //   digitalWrite(LED_PIN_1, LOW);
  //   digitalWrite(LED_PIN_2, LOW);
  //   digitalWrite(LED_PIN_3, LOW);
  //   digitalWrite(LED_PIN_4, LOW);
  //   digitalWrite(LED_PIN_5, LOW);
  //   digitalWrite(LED_PIN_6, HIGH);
  //   digitalWrite(LED_PIN_7, HIGH);
  //   digitalWrite(LED_PIN_8, HIGH);
  // } else if (level_class * 4  >= level) {
  //   digitalWrite(LED_PIN_1, LOW);
  //   digitalWrite(LED_PIN_2, LOW);
  //   digitalWrite(LED_PIN_3, LOW);
  //   digitalWrite(LED_PIN_4, LOW);
  //   digitalWrite(LED_PIN_5, HIGH);
  //   digitalWrite(LED_PIN_6, HIGH);
  //   digitalWrite(LED_PIN_7, HIGH);
  //   digitalWrite(LED_PIN_8, HIGH);
  // } else if (level_class * 5  >= level) {
  //   digitalWrite(LED_PIN_1, LOW);
  //   digitalWrite(LED_PIN_2, LOW);
  //   digitalWrite(LED_PIN_3, LOW);
  //   digitalWrite(LED_PIN_4, HIGH);
  //   digitalWrite(LED_PIN_5, HIGH);
  //   digitalWrite(LED_PIN_6, HIGH);
  //   digitalWrite(LED_PIN_7, HIGH);
  //   digitalWrite(LED_PIN_8, HIGH);
  // } else if (level_class * 6  >= level) {
  //   digitalWrite(LED_PIN_1, LOW);
  //   digitalWrite(LED_PIN_2, LOW);
  //   digitalWrite(LED_PIN_3, HIGH);
  //   digitalWrite(LED_PIN_4, HIGH);
  //   digitalWrite(LED_PIN_5, HIGH);
  //   digitalWrite(LED_PIN_6, HIGH);
  //   digitalWrite(LED_PIN_7, HIGH);
  //   digitalWrite(LED_PIN_8, HIGH);
  // } else if (level_class * 7  >= level) {
  //   digitalWrite(LED_PIN_1, LOW);
  //   digitalWrite(LED_PIN_2, HIGH);
  //   digitalWrite(LED_PIN_3, HIGH);
  //   digitalWrite(LED_PIN_4, HIGH);
  //   digitalWrite(LED_PIN_5, HIGH);
  //   digitalWrite(LED_PIN_6, HIGH);
  //   digitalWrite(LED_PIN_7, HIGH);
  //   digitalWrite(LED_PIN_8, HIGH);
  // } else if (level_class * 8  >= level) {
  //   digitalWrite(LED_PIN_1, HIGH);
  //   digitalWrite(LED_PIN_2, HIGH);
  //   digitalWrite(LED_PIN_3, HIGH);
  //   digitalWrite(LED_PIN_4, HIGH);
  //   digitalWrite(LED_PIN_5, HIGH);
  //   digitalWrite(LED_PIN_6, HIGH);
  //   digitalWrite(LED_PIN_7, HIGH);
  //   digitalWrite(LED_PIN_8, HIGH);
  // } else {
  //   digitalWrite(LED_PIN_1, LOW);
  //   digitalWrite(LED_PIN_2, LOW);
  //   digitalWrite(LED_PIN_3, LOW);
  //   digitalWrite(LED_PIN_4, LOW);
  //   digitalWrite(LED_PIN_5, LOW);
  //   digitalWrite(LED_PIN_6, LOW);
  //   digitalWrite(LED_PIN_7, LOW);
  //   digitalWrite(LED_PIN_8, LOW);
  // }

  if (level_class <= level) {
    digitalWrite(LED_PIN_8, HIGH);
  } else {
    digitalWrite(LED_PIN_8, LOW);
  }
  if (level_class * 2  <= level) {
    digitalWrite(LED_PIN_7, HIGH);
  } else {
    digitalWrite(LED_PIN_7, LOW);
  }
  if (level_class * 3  <= level) {
    digitalWrite(LED_PIN_6, HIGH);
  } else {
    digitalWrite(LED_PIN_6, LOW);
  } 
  if (level_class * 4  <= level) {
    digitalWrite(LED_PIN_5, HIGH);
  } else {
    digitalWrite(LED_PIN_5, LOW);
  } 
  if (level_class * 5  <= level) {
    digitalWrite(LED_PIN_4, HIGH);
  } else {
    digitalWrite(LED_PIN_4, LOW);
  } 
  if (level_class * 6  <= level) {
    digitalWrite(LED_PIN_3, HIGH);
  } else {
    digitalWrite(LED_PIN_3, LOW);
  } 
  if (level_class * 7  <= level) {
    digitalWrite(LED_PIN_2, HIGH);
  } else {
    digitalWrite(LED_PIN_2, LOW);
  } 
  if (level_class * 8  <= level) {
    digitalWrite(LED_PIN_1, HIGH);
  } else {
    digitalWrite(LED_PIN_1, LOW);
  }

  Serial.println(level);
  delay(150);
}
