#include <WiFi.h>
#include <ESP32Servo.h>
#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>


Servo servo;

// const char *ssid = "Addinedu_509_office_2.4G";
// const char *password = "Addinedu8565!";
const char *ssid = "AIE_509_2.4G";
const char *password = "addinedu_class1";
const char* INPUT_PARAM1 = "degree";

AsyncWebServer server(80);

const char html[] PROGMEM = R"rawliteral(
  <!DOCTYPE html>
  <html>
  <body>
  <centor>
  <h1> Hello, ESP32 Web Serber - Async!</h1>
  <div>
  Photoresistor Value : <div id="sensor">None</div>
  </div>
  <br/>
  <form action="/get">
  Servo Degree : <input type="text" name="degree">
  <input type="submit" value="Submit">
  </form>
  </centor>
  <script>
    setInterval(getSensorValue, 100);
    function getSensorValue() {
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {
          document.getElementById("sensor").innerHTML = this.responseText;
        }
      };
      xhttp.open("GET", "/sensor", true);
      xhttp.send();
    }
  </script>
  </body>
  </html>
)rawliteral";

// 페이지 요청이 들어오면 처리하는 함수
String processor(const String& var) {
  Serial.println(var);
  return var;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  servo.attach(5);
  Serial.println("ESP32 Web Server Start");
  // Serial.println(ssid);

  // WiFi 접속
  WiFi.begin(ssid, password);

  // 접속 체크
  while(WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println();

  // 전속 완료
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  // callback 함수 등록
  server.on("/", HTTP_GET, [] (AsyncWebServerRequest *req) {
    req->send_P(200, "text/html", html, processor);
  });

  server.on("/sensor", HTTP_GET, [] (AsyncWebServerRequest *request) {
    int sensor = analogRead(34); // 가변 저항 센서 값 읽기
    String s1 = String(sensor); // int to String
    Serial.println(s1);
    request->send(200, "text/plain", s1);
  });

  server.on("/get", HTTP_GET, [] (AsyncWebServerRequest *req) {
    String inputMessage = req->getParam(INPUT_PARAM1)->value();
    Serial.println(inputMessage);
    float degree = inputMessage.toFloat();
    servo.write(degree);
    req->send_P(200, "text/html", html, processor);
  });

  server.begin();

  Serial.println("HTTP Server Started!");
  delay(100);
}

void loop() {
  // put your main code here, to run repeatedly:
  // while(Serial.available() > 0) {
  //   String input = Serial.readStringUntil('\n');
  //   float degree = input.toFloat();
  //   Serial.println(degree);
  //   servo.write(degree);
  // }
}