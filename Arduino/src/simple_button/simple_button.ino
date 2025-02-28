const int PUSH_BUTTON = 2;
bool flag;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(PUSH_BUTTON, INPUT);
  Serial.begin(9600);
  flag = false;
}

void loop() {
  // put your main code here, to run repeatedly:
  int button_status = digitalRead(PUSH_BUTTON);
  digitalWrite(LED_BUILTIN, button_status);

  if (button_status == HIGH) {
    if (flag == false) {
      Serial.println("Button is pressed.");
      flag = true;
    }
  } else {
    if (flag == true) {
      Serial.println("Button is unpressed.");
      flag = false;
    }
  }

  delay(100);
  // Serial.println(button_status);
}
