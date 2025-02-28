#include <Servo.h>

Servo servo;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(9);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available() > 0) {
    String input = Serial.readStringUntil('\n'); // 문자열 입력을 통째로 받아옴
    float pos = input.toFloat(); // 숫자형으로 변환
    
    Serial.println(pos);
    servo.write(pos);
  }
}
