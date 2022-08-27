
// CREDENCIALES 
// const char* ssid = "Redmi";
// const char* contrasena = "123456789";




#include<WiFi.h>
#include<PubSubClient.h>
#include "credenciales.h"
#include <Adafruit_MLX90614.h> 
#include<Wire.h>
const char* servidor_mqtt= "192.168.43.114"; //mosquitto
int puerto = 1883;

WiFiClient espClient;
PubSubClient client(espClient);
Adafruit_MLX90614 mlx = Adafruit_MLX90614();
int alarma = 33;         // valor de temperatura de alarma
int calibracion = 5;     // factor de calibracion 
void setup_wifi(){
  delay(10);
  WiFi.begin(ssid,contrasena);
  while(WiFi.status()!=WL_CONNECTED){
  delay(300);
  }
}
void reconnect(){
  while(!client.connected()){
    Serial.println("Intentando conexion MQTT con parametros configurados...");
    if(client.connect("ESP32")){
      Serial.println("Conectado");
    }else{
      Serial.print("Falla, Estado:");
      Serial.print(client.state());
      Serial.println("Intentando conexion nuevamente en 2s...");
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(9600);
  setup_wifi();
  client.setServer (servidor_mqtt, puerto);
  mlx.begin(); 
}

void loop() {
  double h=mlx.readObjectTempC()+calibracion;
if(!client.connected()) //para que se reconecte//
  reconnect();
  client.loop();
  client.publish("temp", String(h).c_str());
  delay(2000);
  }
