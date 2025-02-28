const int R_PIN = 3;
const int G_PIN = 5;
const int B_PIN = 6;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(R_PIN, OUTPUT);
  pinMode(G_PIN, OUTPUT);
  pinMode(B_PIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0) {
    Serial.println("----");
    char input = Serial.read();
    Serial.println(input);

    if(input == 'b') {
      analogWrite(R_PIN, 0);
      analogWrite(G_PIN, 0);
      analogWrite(B_PIN, 255);
      Serial.println("BLue");
    } else if(input == 'g') {
      analogWrite(R_PIN, 0);
      analogWrite(G_PIN, 255);
      analogWrite(B_PIN, 0);
      Serial.println("GReen");
    } else if(input == 'r') {
      analogWrite(R_PIN, 255);
      analogWrite(G_PIN, 0);
      analogWrite(B_PIN, 0);
      Serial.println("REd");
    } else {
      Serial.println("Not a command ! !");
    }

  }
  
  // for (int i = 0; i < 255; i++) {
  //   analogWrite(R_PIN, i);
  //   analogWrite(G_PIN, i);
  //   analogWrite(B_PIN, i);
  //   delay(10);
  // }
}
