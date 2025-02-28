#include <SoftwareSerial.h>

#define QR_RX 1
#define QR_TX 0


SoftwareSerial QR(QR_RX, QR_TX);
String test[100] = {};
int i=0; 


class Product {
private:
    String productID;
    String productName;
    String categoryID;

public:
    Product(String pID, String pName, String cID) 
        : productID(pID), productName(pName), categoryID(cID) {}

    // int getProductID() { return productID; }
    // String getProductName() { return productName; }
    // int getCategoryID() { return categoryID; }

    void getProductInfo() {
        Serial.println(productID);
        Serial.println(productName);
        Serial.println(categoryID);
        // Serial.println("Product ID: " + String(productID));
        // Serial.println("Product Name: " + productName);
        // Serial.println("Category ID: " + String(categoryID));
    }
};


void qrRead()
{
    Serial.println("-----------");
    
    if (QR.available() > 0)
    {
        Serial.println("QR read");
        String qrData = QR.readString();
        delay(200);
    
        Serial.println(qrData);
        // if (qrData != "") {
        //   test[i++]=qrData;
        //   for ( int k = 0; k < i ; k++ )
        //   {
        //       Serial.println(test[k]);
        //   }
        // } 

        // String productID = split(qrData, '|');
        // String productName = split(qrData, '|');
        // String categoryID = split(qrData, '|'); 

        // Product 객체 생성
        // Product product(productID, productName, categoryID);

        // product.getProductInfo();
    }
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

void setup()
{
  	Serial.begin(115200);
    QR.begin(115200);
}

void loop()
{
    Serial.println("QR ready");
    qrRead();

    delay(2000);    //demo
}
