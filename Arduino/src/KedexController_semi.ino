#include <Stepper.h>


const int DETECT_PIN = 13;
const int RELAY_PIN = 3;
const int STEP_N1 = 8;
const int STEP_N2 = 9;
const int STEP_N3 = 10;
const int STEP_N4 = 11;


class Product {
private:
    int productID;
    String productName;
    int categoryID;
public:
    Product(): productID(0), productName(""), categoryID(0) {}
    Product(int pID, String pName, int cID)
        : productID(pID), productName(pName), categoryID(cID) {}
    int getProductID() { return productID; }
    String getProductName() { return productName; }
    int getCategoryID() { return categoryID; }
    void displayProductInfo() {
        Serial.println("Product ID: " + String(productID));
        Serial.println("Product Name: " + productName);
        Serial.println("Category ID: " + String(categoryID));
    }
};

// data: 123|productname|112 -> 123
String split(String &data, char seperator)
{
    int seperatorPosition = data.indexOf(seperator);
    String result;
    if(seperatorPosition != -1)
    {
        result = data.substring(0, seperatorPosition);
        data = data.substring(seperatorPosition + 1, data.length());
    }
    else
    {
        result = data;
        data= "";
    }
    Serial.println(result);
    Serial.println("---------------------------------");
    return result;
}

class KedexController {
    int kedexStatus;
    int stepperPos;
    Stepper kedexStepper;
    Product queue[50];
    int front;
    int end;

public:
    KedexController():
    kedexStatus(0), stepperPos(0), front(0), end(0), kedexStepper(512,STEP_N4,STEP_N2,STEP_N3,STEP_N1)
    {}

    KedexController(int stepperSpeed): 
    kedexStatus(0), stepperPos(0), front(0), end(0), kedexStepper(512,11,9,10,8)
    { kedexStepper.setSpeed(stepperSpeed); }

    int getKedexStatus() { return kedexStatus; }
    void setKedexStatus(int status) { kedexStatus = status; }

    bool isFull() const { return (end + 1) % 50 == front; }
    bool isEmpty() const { return front == end; }
    bool enqueue(const Product& product) {
        if (isFull()) {
            return false;
        }
        queue[end] = product;
        end = (end + 1) % 50;
        return true;
    }
    bool dequeue(Product& product) {
        if (isEmpty()) {
            return false;
        }
        product = queue[front];
        front = (front + 1) % 50;
        return true;
    }
    
    bool peek(Product& product) const {
        if (isEmpty()) return false;

        product = queue[front];
        return true;
    }

    void serialRead() {
        // 시리얼에서 값 읽어와서 int productID, String sku, String productName, destinationID 값 저장한 Product 객체 만들기
        String data;

        while (Serial.available() > 0) {
            data = Serial.readStringUntil('\n');
            Serial.println(data);
        }

        if (data != "") {
          int productID = split(data, '|').toInt();
          String productName = split(data, '|');
          int categoryID = data.toInt();

          Product temp(productID, productName, categoryID);
          enqueue(temp);
        }
    }

    void setStepperToPos() {
        Product temp;
        peek(temp);
        if (temp.getCategoryID() == 1) {
            stepperPos = 512;
            kedexStepper.step(stepperPos);
        } else if (temp.getCategoryID() == 3) {
            stepperPos = -512;
            kedexStepper.step(stepperPos);
        }
    }

    bool detect() {
        if (digitalRead(DETECT_PIN) == HIGH) {
            Product temp;
            dequeue(temp);
            kedexStepper.step(-1 * stepperPos);
            stepperPos = 0;
            return true;
        }
        return false;
    }

    void conveyorMove() {
        if (kedexStatus != 0) {
            digitalWrite(RELAY_PIN, HIGH);
        }
        else {
            digitalWrite(RELAY_PIN, LOW);
        }
    }
    
};

KedexController kedex(60);

void setup() {
    Serial.begin(9600);
    pinMode(RELAY_PIN, OUTPUT);
}

void loop() {
    kedex.serialRead();

    if (kedex.getKedexStatus() == 0) {
        if (!kedex.isEmpty()) {
            kedex.setKedexStatus(1);
        }
    } else if (kedex.getKedexStatus() == 1) {
        kedex.setStepperToPos();
        kedex.setKedexStatus(2);
    } else if (kedex.getKedexStatus() == 2) {
        if(kedex.detect()) {
            kedex.setKedexStatus(3);
        }
    } else {
        if (kedex.isEmpty()) {
            kedex.setKedexStatus(0);
        } else {
            kedex.setKedexStatus(1);
        }
    }

    kedex.conveyorMove();

}