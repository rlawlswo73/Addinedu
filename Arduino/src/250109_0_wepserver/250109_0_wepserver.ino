#include <WiFi.h>
#include <WebServer.h>

// const char *ssid = "Addinedu_509_office_2.4G";
// const char *password = "Addinedu8565!";
const char *ssid = "AIE_509_2.4G";
const char *password = "addinedu_class1";
const int ledPin = 23;

WebServer server(80);
void handle_root(); // 페이지 요청이 들어오면 처리하는 함수 

const char html[] PROGMEM = R"rawliteral(
  <!DOCTYPE html>
  <html>
  <body>
  <centor>
  <h1> Hello, ESP32 Web Serber - Async!</h1>
  <div> LED PIN 21 :
  <input type="checkbox" onchange="toggleCheckBox(this)" />
  </div>
  <script>
  function toggleCheckBox(element) {
    var req = new XMLHttpRequest();
    if (element.checked) {
      req.open("GET", "/on", true)
    }
    else {
      req.open("GET", "/off", true);
    }
    req.send();
  }
  </script>
  </centor>
  </body>
  </html>
)rawliteral";

void handle_root() {
  server.send(200, "text/html", html);
}

void ledOn() {
  Serial.println("On");
  digitalWrite(ledPin, HIGH);
  server.send(200, "text/html", html);
}

void ledOff() {
  Serial.println("Off");
  digitalWrite(ledPin, LOW);
  server.send(200, "text/html", html);
}

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);

  Serial.begin(115200);
  Serial.println("ESP32 Web Server Start");
  Serial.println(ssid);

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

  // 페이지 요청 함수 등록 & 서버 시작
  server.on("/", handle_root);
  server.on("/on", HTTP_GET, ledOn);
  server.on("/off", HTTP_GET, ledOff);
  server.begin();

  Serial.println("HTTP Server Started!");
  delay(100);
}

void loop() {
  // put your main code here, to run repeatedly:
  server.handleClient();
}
