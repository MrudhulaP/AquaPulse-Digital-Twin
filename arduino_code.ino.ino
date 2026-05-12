int flowSensor = A0;
int waterSensor = A1;

int flowValue = 0;
int waterValue = 0;

void setup() {

  Serial.begin(9600);

  pinMode(13, OUTPUT);

}

void loop() {

  flowValue = analogRead(flowSensor);
  waterValue = analogRead(waterSensor);

  Serial.print("Flow: ");
  Serial.print(flowValue);

  Serial.print(" Water: ");
  Serial.println(waterValue);

  if(flowValue < 300 || waterValue < 300) {

    digitalWrite(13, HIGH);

  }
  else {

    digitalWrite(13, LOW);

  }

  delay(1000);
}
