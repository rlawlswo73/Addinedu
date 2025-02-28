
#include <Stepper.h>
 
const int stepsPerRevolution = 1024;
Stepper myStepper(stepsPerRevolution,11,9,10,8); 
 
void setup() {
  myStepper.setSpeed(30); 
  Serial.begin(9600);     
}

int speed = 0;

void loop() {
  Serial.println("counterclockwise");
  myStepper.step(stepsPerRevolution);
  delay(1000);
 
  Serial.println("clockwise");
  myStepper.step(-stepsPerRevolution);
  delay(1000);

  // myStepper.step(stepsPerRevolution);  // 한 바퀴 회전 명령
  
  if (Serial.available() > 0) {
    speed = Serial.read();
    myStepper.setSpeed(speed);
  }
}
