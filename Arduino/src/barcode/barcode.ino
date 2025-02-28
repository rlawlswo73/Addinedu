/*
Test qrData :
123|ARD-UNO-R3|ARDUINO|11


Serial Monitor Output :
=================================
123|ARD-UNO-R3|ARDUINO|11
---------------------------------
Product ID: 123
SKU: ARD-UNO-R3
product name: ARDUINO
Destination ID: 11
---------------------------------
11
ARD-UNO-R3
=================================
*/

#include <SoftwareSerial.h>
#include <LiquidCrystal.h>
#include <Wire.h>

int seconds = 0;

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
SoftwareSerial BARCODE(0,1);

// SofwareSerial qrSerial(2,3);

void qrRead();

class Product {
private:
    int productID;
    String sku;
    String productName;
    int destinationID;

public:
    Product(int pID, String s, String pName, int dID) 
        : productID(pID), sku(s), productName(pName), destinationID(dID) {}

    int getProductID() { return productID; }
    String getSku() { return sku; }
    String getProductName() { return productName; }
    int getDestinationID() { return destinationID; }

    void displayProductInfo() {
        Serial.println("Product ID: " + String(productID));
        Serial.println("SKU: " + sku);
        Serial.println("Product Name: " + productName);
        Serial.println("Destination ID: " + String(destinationID));
    }
};

String qrData;

void setup()
{
  	Serial.begin(9600);
    BARCODE.begin(115200);
  
    lcd.begin(16,2);
    lcd.print("QR Scanner Ready");
}


// int count = 0;
 
void loop()
{
  // int flags = -1;

  // if (flags == -1) {
  //   qrRead();
  //   flags *= -1;
  // } else if (flags == 1 && qrData != "") {
  //   Serial.println("=================================");
  //   Serial.println(qrData);
  //   Serial.println("---------------------------------");
  //   qrData == "";
  //   flags *= -1;
  // }

  qrRead();

  delay(1000);    //demo
}

void qrRead()
{
  // String qrData = "123|ARD-UNO-R3|ARDUINO|11";
  if (BARCODE.available()) {
    qrData = BARCODE.readString();
    Serial.println("=================================");
    Serial.println(qrData);
    Serial.println("---------------------------------");
  }

  // int productID = split(qrData, '|').toInt();
  // String sku = split(qrData, '|');
  // String productName = split(qrData, '|');
  // int destinationID = split(qrData, '|').toInt();

  // Product 객체 생성
  // Product product(productID, sku, productName, destinationID);
  // product.displayProductInfo(); // 제품 정보 표시

  // // 목적지 ID에 따라 LCD에 표시
  // lcdDisplay(product.getSku(), product.getDestinationID());

}

// Split 함수: 문자열을 구분자로 분리하여 반환한다.
// 예: split('123/ARDUINO-UNO-R3/Seoul') -> '123'
String split(String &data, char seperator)
{
    int seperatorPosition = data.indexOf(seperator);
    String result;
   
    if(seperatorPosition != -1)
    {
        // 구분자 전까지의 문자열을 result에 저장
        result = data.substring(0, seperatorPosition);
        // 구분자 이후의 문자열로 data를 업데이트
        data = data.substring(seperatorPosition + 1, data.length());
    }
    else
    {
        // 구분자가 없으면 data 전체를 result에 저장하고, data를 빈 문자열로 설정
        result = data;
        data= "";
    }
    Serial.println(result);
    Serial.println("---------------------------------");
    return result;
}

void lcdDisplay (String sku, int destination)
{
    lcd.clear();
  	Serial.println(String(destination));
  	Serial.println(sku);
  	lcd.setCursor(0, 0);
  	lcd.print("Destinantion " + String(destination));
  	
    lcd.setCursor(0, 1);
  	lcd.print(sku);
}