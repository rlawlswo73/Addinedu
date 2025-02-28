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
unsigned long lastSensorTime = 0;
unsigned long lastSensorTime_1 = 0;   // 마지막 센서 업데이트 시간
unsigned long lastSensorTime_2 = 0;   // 마지막 센서 업데이트 시간
unsigned long lastMotorTime = 0;
unsigned long currentMotorTime = 0;
unsigned long startMotorTime = 0;
unsigned long currentTime = millis();
unsigned long motorStartTime = 0;         // 모터 시작 시간
const unsigned long sensorInterval = 100; // 센서 읽기 주기 (100ms)
const unsigned long motorRunTime = 1000;  // 모터 동작 시간 (1초)
int dStatus = 0;
int fdStatus = 0;
int motorStatus = 0;
bool isConveyorRunning = false;           // 모터 동작 상태
unsigned long moveStartTime = 0;  // 모터가 시작된 시간을 저장
bool isMoving = false;  // 모터가 동작 중인지 여부를 저장


void loop() {
  currentTime = millis();
  // 센서 읽기
  if (currentTime - lastSensorTime >= sensorInterval) {
    lastSensorTime = currentTime;
    dStatus = kedex.detect();       // 센서 1
    fdStatus = kedex.front_detect(); // 센서 2
  }

  // // 모터
  if (dStatus == 1) {
    // kedex.serialRead();
    Serial.println(dStatus);
    moveConv(150);
  }

  if (fdStatus == 1) {
    moveConv(400);
    delay(500);
    moveConv(1);
    // kedex.conveyorMove(0);  // 모터 정지
    // kedex.conveyorMove(1);  // 모터 정지
    kedex.moveToPosition(400);
    value = 0;
    servo.write(value);
    delay(1300);

    value = 80;
    servo.write(value);
    delay(1300);
    kedex.moveToPosition(0);
  } else {
  }
}

void startMotor() {
  startMotorTime = millis();
}

void moveConv(int duration) {
  if (duration > 0) {
    if (!isMoving) {
      // 모터가 아직 동작 중이 아니면, 시작 시간 저장하고 모터를 시작
      moveStartTime = millis();  
      kedex.conveyorMove(1);  // 모터 시작
      kedex.resetFlags();
      isMoving = true;
    } else if (millis() - moveStartTime >= duration) {
      // 지정된 시간이 경과하면 모터를 멈추고 상태를 초기화
      kedex.conveyorMove(0);  // 모터 정지
      kedex.resetFlags();  // 플래그 리셋
      isMoving = false;
    }
  }
}

// 서보 모터 동작
void moveServo() {
  value = 0;
  servo.write(value);
  delay(1300);

  value = 80;
  servo.write(value);
  delay(1300);
}
