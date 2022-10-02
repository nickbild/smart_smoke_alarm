#include <WiFiNINA.h>
#include "secrets.h"

#define BUZZER_PIN 2
#define ALERT_PIN 3
#define MANUAL_PIN 4

WiFiClient client;
const char* host = "192.168.1.113";
const char* url = "/send_alert?";

void setup() {
//  Serial.begin(115200);

  // Additional GND and VCC.
  pinMode(6, OUTPUT);
  digitalWrite(6, LOW);
  pinMode(7, OUTPUT);
  digitalWrite(7, HIGH);
  
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(ALERT_PIN, INPUT);
  pinMode(MANUAL_PIN, INPUT);

  // Connect to WiFi.
  WiFi.begin(SSID, PASSWORD);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
//    Serial.print(".");
  }

//  Serial.println("\nWiFi connected.");
//  Serial.println("IP address: ");
//  Serial.println(WiFi.localIP());
}

void loop() {
  if (digitalRead(MANUAL_PIN) == HIGH) {
    playBuzzer();
  }
}

void playBuzzer() {
  delay(3000);
  for (int i=0; i<30; i++) {
    tone(BUZZER_PIN, 1000);
    if (digitalRead(ALERT_PIN) == HIGH) { sendAlertToAPI(); }
    delay(1000);
    noTone(BUZZER_PIN);
    if (digitalRead(ALERT_PIN) == HIGH) { sendAlertToAPI(); }
    delay(1000);
  }
}

void sendAlertToAPI() {
  // Send in person detection alert to API.
  if (!client.connect(host, 5000)) {
//    Serial.println("Connection failed.");
    return;
  }

  client.print(String("GET ") + url + "location_id=" + LOCATION_ID + " HTTP/1.1\r\n" +
    "Host: " + host + "\r\n" +
    "Connection: close\r\n\r\n");

  while(client.available()) {}

  client.stop();
}
