const int PIR_PIN = 2;
const int LED_PIN = 4;

unsigned long start_time = 0;
unsigned long end_time = 0;
unsigned long time_count = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(PIR_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int input = digitalRead(PIR_PIN);
  Serial.print(millis());
  Serial.print(", ");
  // digitalWrite(LED_PIN, input);
  // delay(100);

  Serial.print(input);
  if(input == HIGH) {
    start_time = millis();
    end_time = start_time + 5000;
    time_count = start_time;
  }

  if(time_count <= end_time ) {
    time_count += 100;
    digitalWrite(LED_PIN, HIGH);
    delay(100);
  } else {
    digitalWrite(LED_PIN, LOW);  
  }

  Serial.print(", ");
  Serial.print(start_time);
  Serial.print(", ");
  Serial.print(end_time);
  Serial.print(", ");
  Serial.println(time_count);
}
