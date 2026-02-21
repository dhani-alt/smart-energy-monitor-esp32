#include <DHT.h>

#define DHTPIN 34
#define DHTTYPE DHT11
#define PIR_PIN 27
#define LDR_PIN 34
#define LED_PIN 25

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);

  pinMode(PIR_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);

  dht.begin();
}

void loop() {

  int motion = digitalRead(PIR_PIN);     // Read motion
  int ldrValue = analogRead(LDR_PIN);    // Read light level
  float temp = dht.readTemperature();    // Read temperature
  float hum = dht.readHumidity();        // Read humidity

  Serial.println("----- SENSOR DATA -----");
  Serial.print("Motion: ");
  Serial.println(motion);

  Serial.print("Light (LDR): ");
  Serial.println(ldrValue);

  Serial.print("Temperature: ");
  Serial.println(temp);

  Serial.print("Humidity: ");
  Serial.println(hum);

  // Energy Saving Logic
  if (motion == HIGH && ldrValue < 2000) {
    digitalWrite(LED_PIN, HIGH);   // Turn ON light
    Serial.println("Light ON");
  } else {
    digitalWrite(LED_PIN, LOW);    // Turn OFF light
    Serial.println("Light OFF");
  }

  Serial.println("----------------------");
  delay(2000);
}