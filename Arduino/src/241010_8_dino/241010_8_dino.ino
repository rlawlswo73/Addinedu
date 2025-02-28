#include <Servo.h>
// #include <Thread.h>
// #include <ThreadController.h>

Servo servo;
// ThreadController controll = ThreadController();

// Thread myThread = Thread();

const int T = 3;
int count = 0;
int sum = 0;
int data = 0;

int distance = 6; // 거리 6 m
int vel = 6; // 초기속도 : 6m/s
int time_sleep = 0; // 다음 점프까지 대기시간
int light = 0; // 초기화
// unsigned long edge = 0;
// unsigned long prev_edge = 0;
// unsigned long term = 0;

float ms = 0.01;

int filter(int light) {
  count++;
  sum += light;
  if (count == T) {
    int temp = sum;
    count = 0;
    sum = 0;
    // Serial.println(temp);
    return temp / T;
  }
}

// void servo_active() {
//   if (data <= 50) {
//     delay(1100);
//     Serial.println("점프!");
//     servo.write(90);
//     delay(150);
//   } else {
//     servo.write(60);
//     Serial.println("달리기!");
//     delay(150);
//   }
// }

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(9);

  // myThread.onRun(servo_active);
  // myThread.setInterval(50);

  // controll.add(&myThread);

  servo.write(60);
}

void loop() {
  // put your main code here, to run repeatedly:
  // int data = filter(light);

  for(int i = 0; i < T; i++) {
    int light = analogRead(A0);
    sum += light;
  }

  data = sum / T;
  sum = 0;
  // data = analogRead(A0);
  int pow = sq(data);
 
  Serial.print(data);
  Serial.print(", ");

  ms += 0.01;
  int temp = 100 - ms;
  if (data <=  32) {
    delay(100);
    Serial.println("점프!");
    servo.write(90);
    delay(100); 
  } else {
    servo.write(60);
    Serial.println("달리기!");
    delay(100);
  }

}
