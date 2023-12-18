// https://github.com/morrissinger/ESP8266-Websocket/tree/master
// https://stackoverflow.com/questions/59005181/unable-to-connect-https-protocol-with-esp8266-using-wificlientsecure

#include <ESP8266WiFi.h>
#include <WebSocketClient.h>
#include <ESP8266HTTPClient.h>

//Brown-Guest
const char* ssid     = "Verizon_HF9J74";
const char* password = "treat6-omit-fro";
char path[] = "/";
char host[] = "kazar4.com";
  
WebSocketClient webSocketClient;

// Use WiFiClient class to create TCP connections
WiFiClientSecure client;

void setup() {
  Serial.begin(9600);
  while (!Serial);
  Serial1.begin(9600); // Initialize TX/RX communication (do not need to wait)
  delay(10);

  // We start by connecting to a WiFi network

  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);

  // Serial.println(WiFi.macAddress());
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  delay(5000);
  
  const char *sslFingerprint = "4E E4 07 83 B5 C6 5C 20 92 3C A2 FB 02 62 2F 6A D1 01 8D B8";

  client.setFingerprint(sslFingerprint);
  // Connect to the websocket server
  if (client.connect("kazar4.com", 9001)) {
    Serial.println("Connected");
  } else {
    Serial.println("Connection failed.");
    while(1) {
      // Hang on failure
    }
  }

  // Handshake with the server
  webSocketClient.path = path;
  webSocketClient.host = host;
  if (webSocketClient.handshake(client)) {
    Serial.println("Handshake successful");

    webSocketClient.sendData("ESP");
  } else {
    Serial.println("Handshake failed.");
    while(1) {
      // Hang on failure
    }  
  }

}


void loop() {
  String data;

  if (client.connected()) {
    
    webSocketClient.getData(data);
    if (data.length() > 0) {
      //Serial.print("Received data: ");
      //Serial.println(data);
      //Serial.println("Sending data to Arduino Lights");

      Serial.print("<");
      Serial.print(data);
      Serial.print(">");

      //Serial1.write("GOT SOMETHING"); // Sending data to Arduino
    }

    if (Serial1.available() > 0) {
      Serial.println(Serial1.readString());
      // Serial1.readStringUntil('<');
      // String message = Serial1.readStringUntil('>');
      // Serial.println(message);
      // webSocketClient.sendData(message);
    }
    
    // capture the value of analog 1, send it along
    // pinMode(1, INPUT);
    // data = String(analogRead(1));
    // webSocketClient.sendData("POG");
    
    
  } else {
    Serial.println("Client disconnected.");
    while (1) {
      // Hang on disconnect.
    }
  }
  
  // wait to fully let the client disconnect
  //delay(3000);
  
}
