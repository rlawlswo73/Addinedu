#include <WiFi.h>
// #include <WebServer.h>
#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>

// const char *ssid = "Addinedu_509_office_2.4G";
// const char *password = "Addinedu8565!";
const char *ssid = "AIE_509_2.4G";
const char *password = "addinedu_class1";
const int ledPin3 = 23;
const int ledPin2 = 22;
const int ledPin1 = 21;

AsyncWebServer server(80);

const char html[] PROGMEM = R"rawliteral(
  <!DOCTYPE html>
  <html>
  <body>
  <centor>
  <h1> Hello, ESP32 Web Serber - Async!</h1>
  <div> LED PIN 21 :
  <input type="checkbox" onchange="toggleCheckBox1(this)" />
  </div>
  <div> LED PIN 22 :
  <input type="checkbox" onchange="toggleCheckBox2(this)" />
  </div>
  <div> LED PIN 23 :
  <input type="checkbox" onchange="toggleCheckBox3(this)" />
  </div>
  <script>
  function toggleCheckBox1(element) {
    var req = new XMLHttpRequest();
    if (element.checked) {
      req.open("GET", "/on1", true)
    }
    else {
      req.open("GET", "/off1", true);
    }
    req.send();
  }
  function toggleCheckBox2(element) {
    var req = new XMLHttpRequest();
    if (element.checked) {
      req.open("GET", "/on2", true)
    }
    else {
      req.open("GET", "/off2", true);
    }
    req.send();
  }
  function toggleCheckBox3(element) {
    var req = new XMLHttpRequest();
    if (element.checked) {
      req.open("GET", "/on3", true)
    }
    else {
      req.open("GET", "/off3", true);
    }
    req.send();
  }
  </script>
  </centor>
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
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin1, OUTPUT);

  Serial.begin(115200);
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

  // 페이지 요청 함수 등록 & 서버 시작
  server.on("/", HTTP_GET, [] (AsyncWebServerRequest *req) {
    req->send_P(200, "text/html", html, processor);
  });

  server.on("/on1", HTTP_GET, [] (AsyncWebServerRequest *req) {
    Serial.println("/on1");
    digitalWrite(ledPin1, HIGH);
    req->send_P(200, "text/html", html, processor);
  });

  server.on("/off1", HTTP_GET, [] (AsyncWebServerRequest *req) {
    Serial.println("/off1");
    digitalWrite(ledPin1, LOW);
    req->send_P(200, "text/html", html, processor);
  });

  server.on("/on2", HTTP_GET, [] (AsyncWebServerRequest *req) {
    Serial.println("/on2");
    digitalWrite(ledPin2, HIGH);
    req->send_P(200, "text/html", html, processor);
  });

  server.on("/off2", HTTP_GET, [] (AsyncWebServerRequest *req) {
    Serial.println("/off2");
    digitalWrite(ledPin2, LOW);
    req->send_P(200, "text/html", html, processor);
  });

  server.on("/on3", HTTP_GET, [] (AsyncWebServerRequest *req) {
    Serial.println("/on3");
    digitalWrite(ledPin3, HIGH);
    req->send_P(200, "text/html", html, processor);
  });

  server.on("/off3", HTTP_GET, [] (AsyncWebServerRequest * req) {
    Serial.println("/off3");
    digitalWrite(ledPin3, LOW);
    req->send_P(200, "text/html", html, processor);
  });

  server.begin();

  Serial.println("HTTP Server Started!");
  delay(100);
}

void loop() {
  // put your main code here, to run repeatedly:
}
