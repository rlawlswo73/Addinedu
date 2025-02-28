#include "KedexController.h"
#include <Servo.h>
// #include <Stepper.h>

Servo servo;
int value = 80;

const int STEP_N1 = 8;
const int STEP_N2 = 9;
const int STEP_N3 = 10;
const int STEP_N4 = 11;

// Stepper stepper(512, STEP_N4, STEP_N2, STEP_N3, STEP_N1);

const int DETECT_PIN = 13;
const int DETECT_PIN_2 = 12;

const int ENB = 6;
const int IN3 = 4;
const int IN4 = 5;

KedexController kedex(STEP_N1, STEP_N2, STEP_N3, STEP_N4, DETECT_PIN, ENB, IN3, IN4);

void setup() {
  Serial.begin(115200);
  pinMode(DETECT_PIN, INPUT);
  pinMode(DETECT_PIN_2, INPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  // analogWrite(ENB, 0);

  while (!Serial) {
    ;
  }
  kedex.stepInit();

  servo.attach(3);
  servo.write(value);

  analogWrite(ENB, 0);
}

/*
  0: waiting
  1: get signal
  2: moving
  3: arrivied
*/

int temp = 0;

void moveConv(int time) {
  kedex.conveyorMove(time);
  // delay(600);
  kedex.conveyorMove(0);
  // delay(200);
  kedex.resetFlags();
}

void loop() {
  int dStatus = kedex.detect();
  int fdStatus = kedex.front_detect();
  kedex.serialRead();
  // Serial.println(String(kedex.getCategoryID()));
  // Serial.println("test");
  // kedex.setDataFlow();
  // Serial.println(digitalRead(DETECT_PIN));

  if (dStatus == 1) {
    // kedex.serialRead();
    // Serial.println(kedex.getCategoryID());
    // kedex.setDataFlow();
    // if (kedex.getBarcodeAvail()) {
    // Serial.print("d1 : ");
    // Serial.println(dStatus);

    moveConv(100);
  }

  if (fdStatus == 1) {
    // Serial.print("d2 : ");
    // Serial.println(fdStatus);
    moveConv(400);
    delay(00);
    kedex.moveToPosition(400);
    delay(1500);
    value = 0;
    servo.write(value);
    delay(1500);

    value = 80;
    servo.write(value);
    delay(1500);
    kedex.moveToPosition(0);
    delay(1500);
  } else {
  }
}
