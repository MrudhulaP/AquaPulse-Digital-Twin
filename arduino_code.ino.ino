#include <Wire.h>
#include <Adafruit_BMP085.h>

Adafruit_BMP085 bmp;

// Pins
int flowSensor = A0;
int leakSensor = A1;

void setup() {

  Serial.begin(9600);

  if (!bmp.begin()) {

    Serial.println("BMP180 not detected");

    while (1);

  }

  pinMode(13, OUTPUT);
}

void loop() {

  // Read sensors
  int flowValue = analogRead(flowSensor);

  int leakValue = analogRead(leakSensor);

  float pressure = bmp.readPressure();

  // Print values
  Serial.print("Flow:");
  Serial.print(flowValue);

  Serial.print(" Leak:");
  Serial.print(leakValue);

  Serial.print(" Pressure:");
  Serial.println(pressure);

  // Leak condition
  if (leakValue < 150 || pressure < 90000) {

    digitalWrite(13, HIGH);

  }
  else {

    digitalWrite(13, LOW);

  }

  delay(1000);
}
