#include <stdlib.h>

const int FLOOR_CONUT = 2;

const int FLOOR_1 = A0;
const int INTER_FLOOR_1_1 = 2;
const int INTER_FLOOR_1_2 = 3;
const int FLOOR_2 = 4;
const int INTER_FLOOR_2_1 = 5;
const int INTER_FLOOR_2_2 = 6;
const int FLOOR_3 = 7;

const int FCS_1 = 8; // FLOOR_CALL_STATUS
const int FCS_2 = 9;
const int FCS_3 = 10;

const int FCB_1 = 11; // FLOOR_CALL_BUTTON
const int FCB_2 = 12;
const int FCB_3 = 13;

const int ELEVATOR_FLOOR[7] = { // 엘레베이터가 있을 수 있는 위치
  FLOOR_1, 
  INTER_FLOOR_1_1, 
  INTER_FLOOR_1_2,
  FLOOR_2, 
  INTER_FLOOR_2_1, 
  INTER_FLOOR_2_2,
  FLOOR_3
};

const int FCS_ARRAY[3] = {
  FCS_1,
  FCS_2,
  FCS_3
};

int elevator_pos = 1; // 엘레베이터의 현재 위치
int call_order[3] = {0, 0, 0}; // 엘레베이터를 부른 순서
bool call_elevator[3] = {0, 0, 0}; // 배열의 각 요소는 각 층에 대응된다

int delay_time = 25;
float half_time = 0.0;

int goal = 0; // 현재 가야할 곳
int final_destination = elevator_pos; // 엘리베이터가 중간에 목적지를 잃었을때 가야할 곳(가장 가까운 층)

// 엘레베이터 현재 위치 LED 표시
void elevator_pos_LED() {
  for(int i = 0; i < (sizeof(ELEVATOR_FLOOR) / sizeof(int)); i++) {
    digitalWrite(ELEVATOR_FLOOR[i], LOW);  
  }
  digitalWrite(ELEVATOR_FLOOR[elevator_pos-1], HIGH);
}

// 현재 위치를 층으로 변환
int position_convert(int x) {
  int index = 0;
  switch(x) {
    case 1:
      index = 0;
      break;
    case 4:
      index = 1;
      break;
    case 7:
      index = 2;
      break;
    default:
      index = -9999;
      break;
  }
  return index;
}

// // 순서 정렬
void call_sort() {
  for(int i = 0; i <= FLOOR_CONUT; i++) {
    call_order[i] = call_elevator[position_convert(call_order[i])] * call_order[i];
    if(call_order[i] == 0) {
      if(i != FLOOR_CONUT) {
        call_order[i] = call_order[i+1];
        call_order[i+1] = 0;
      } else {
        call_order[FLOOR_CONUT] = 0;
      }
    }
  }
}

// 순서 지정
void call_order_priority(int x) {
  int index = position_convert(x);

  for(int i = 0; i <= FLOOR_CONUT; i++) {
    if(call_order[i] == 0 && call_elevator[index] == HIGH) {
      call_order[i] = x;
      break;
    }
    if(call_order[i] == index && call_elevator[index] == LOW) {
      call_order[i] = 0;
    }
  }
}

// 엘레베이터가 이동하는 함수
void move_elevator() {
  goal = call_order[0];
  if (half_time >= 1.0) {
    // 호출 된 곳이 있는지 확인.
    if(call_elevator[0] == HIGH || call_elevator[1] == HIGH || call_elevator[2] == HIGH) {
      // 가야할 곳 지정 -> 어딜 먼저 가는지 우선순위 지정 -> 누른 순서 기억?
      // 우선적으로 가야할 곳 call_order

      if(call_order[0] != 0) {
        goal = call_order[0];

        // 엘리베이터가 이동해야할 상대적 방향 구하기
        if(goal != elevator_pos) {
          if(goal > elevator_pos) {
            elevator_pos++;
          }
          else if(goal < elevator_pos) {
            elevator_pos--;
          }
          delay(delay_time);

        } else if (goal == elevator_pos) {
          int index = position_convert(elevator_pos);
          call_elevator[index] = 0;
          call_order[0] = 0;
          call_sort();
          digitalWrite(FCS_ARRAY[index], call_elevator[index]);
        }

        if(elevator_pos == FLOOR_2 && (FLOOR_2 == call_order[1] || FLOOR_2 == call_order[2])) {
          if (FLOOR_2 == call_order[1]) {
            call_order[1] = 0;
          } else if (FLOOR_2 == call_order[1]) {
            call_order[2] = 0;
          }
          call_elevator[1] = 0;
        }
      }

      if((call_elevator[0] == HIGH || call_elevator[1] == HIGH || call_elevator[2] == HIGH) && (call_order[0] == 0 && call_order[1] == 0 && call_order[2] == 0)) {
        if(call_elevator[0] == HIGH) {
          call_order[0] = 1;
        } else if(call_elevator[1] == HIGH) {
          call_order[0] = 4;
        } else if(call_elevator[2] == HIGH) {
          call_order[0] = 7;
        }
      }
      
    } else {
      int floor_diff_1 = pow(elevator_pos - 1, 2);
      int floor_diff_2 = pow(elevator_pos - 4, 2);
      int floor_diff_3 = pow(elevator_pos - 7, 2);

      if(floor_diff_1 != 0 && floor_diff_2 != 0 && floor_diff_3 != 0) {
        if(floor_diff_1 <= floor_diff_2 && floor_diff_1 <= floor_diff_3) {
          final_destination = 1;
        } else if (floor_diff_2 <= floor_diff_1 && floor_diff_2 <= floor_diff_3) {
          final_destination = 4;
        } else if (floor_diff_3 <= floor_diff_2 && floor_diff_3 <= floor_diff_1) {
          final_destination = 7;
        }
        if(final_destination != elevator_pos) {
          if(final_destination > elevator_pos) {
            elevator_pos++;
          }
          else if(final_destination < elevator_pos) {
            elevator_pos--;
          }
          delay(delay_time);
        } else if (final_destination == elevator_pos) {
          int index = position_convert(elevator_pos);
          call_elevator[index] = 0;
          call_order[0] = 0;
          call_sort();
        }
      }
      goal = 0;
    }
    half_time = 0.0;
  }
}

// 호출 버튼 LED
void call_button_led() {
  for(int i = 0; i < (sizeof(FCS_ARRAY)/ sizeof(int)); i++) {
    digitalWrite(FCS_ARRAY[i], call_elevator[i]);
  }
}

// 입력을 저장하는 함수
void call_button_pushed() {
  int press_button_1;
  int press_button_2;
  int press_button_3;
  
  static int prevButtonState_1 = LOW;
  press_button_1 = digitalRead(FCB_1);
  static int prevButtonState_2 = LOW;
  press_button_2 = digitalRead(FCB_2);
  static int prevButtonState_3 = LOW;
  press_button_3 = digitalRead(FCB_3);

  if (press_button_1 == HIGH && prevButtonState_1 == LOW) {
    call_elevator[0] = !call_elevator[0];
    call_order_priority(1);
  }

  if (press_button_2 == HIGH && prevButtonState_2 == LOW) {
    call_elevator[1] = !call_elevator[1];
    call_order_priority(4);
  }

  if (press_button_3 == HIGH && prevButtonState_3 == LOW) {
    call_elevator[2] = !call_elevator[2];
    call_order_priority(7);
  }

  prevButtonState_1 = press_button_1;
  prevButtonState_2 = press_button_2;
  prevButtonState_3 = press_button_3;
}

void setup() {
  pinMode(FLOOR_1, OUTPUT);
  for(int i = 2; i <= 10; i++) {pinMode(i, OUTPUT);}
  for(int i = 11; i <= 13; i++) {pinMode(i, INPUT);}
  Serial.begin(9600);
}

void loop() {
  call_button_pushed();
  move_elevator();
  elevator_pos_LED();
  call_button_led();

  half_time += 0.05;
  delay(delay_time);

  call_sort();

  Serial.print("(");
  Serial.print(call_elevator[0]);
  Serial.print(", ");
  Serial.print(call_elevator[1]);
  Serial.print(", ");
  Serial.print(call_elevator[2]);
  Serial.print("), (");
  Serial.print(call_order[0]);
  Serial.print(", ");
  Serial.print(call_order[1]);
  Serial.print(", ");
  Serial.print(call_order[2]);
  Serial.println(")");
}
