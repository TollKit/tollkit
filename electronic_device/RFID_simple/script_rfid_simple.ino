
// CREDENCIALES 
// const char* ssid = "Redmi";
// const char* contrasena = "123456789";


#include<ESP8266WiFi.h>
#include<PubSubClient.h>
#include "credenciales.h"
#include <SPI.h>      // incluye libreria bus SPI
#include <MFRC522.h>      // incluye libreria especifica para MFRC522
  #define SS_PIN D8
  #define RST_PIN D0
 const char* servidor_mqtt= "192.168.43.114"; //mosquitto
 int puerto = 1883;
 
 WiFiClient espClient;
PubSubClient client(espClient);
MFRC522 mfrc522(SS_PIN, RST_PIN); // crea objeto mfrc522 enviando pines de slave select y reset

byte LecturaUID[4];         // crea array para almacenar el UID leido
byte Usuario1[4]= {0x82, 0x95, 0x40, 0x1C} ;    // UID de tarjeta leido en programa 1
byte Usuario2[4]= {0xE0, 0xB2, 0x4E, 0xD3} ;    // UID de llavero leido en programa 1
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
    if(client.connect("ESP8266")){
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
  SPI.begin();        // inicializa bus SPI
  mfrc522.PCD_Init();     // inicializa modulo lector
  Serial.println("Listo");    // Muestra texto Listo
}

void loop() {
  if(!client.connected()) //para que se reconecte//
  reconnect();
  
  if ( ! mfrc522.PICC_IsNewCardPresent())   // si no hay una tarjeta presente
    return;           // retorna al loop esperando por una tarjeta
  
  if ( ! mfrc522.PICC_ReadCardSerial())     // si no puede obtener datos de la tarjeta
    return;           // retorna al loop esperando por otra tarjeta
    
    Serial.print("TOLLKIT:");       // muestra texto UID:
    for (byte i = 0; i < mfrc522.uid.size; i++) { // bucle recorre de a un byte por vez el UID
          
          LecturaUID[i]=mfrc522.uid.uidByte[i];     // almacena en array el byte del UID leido      
          }
          
          Serial.print("\t");         // imprime un espacio de tabulacion             
                    
          if(comparaUID(LecturaUID, Usuario1)){    // llama a funcion comparaUID con Usuario1
            client.loop();
            client.publish("id", "Bienvenido Richard Elescano");
             delay(2000);
            Serial.println("Bienvenido Richard Elescano");} // si retorna verdadero muestra texto bienvenida
          else if(comparaUID(LecturaUID, Usuario2)){ // llama a funcion comparaUID con Usuario2
          client.loop();
            client.publish("id", "ACCESO DENEGADO");
             delay(2000);
            Serial.println("ACCESO DENEGADO");} // si retorna verdadero muestra texto bienvenida
           else{           // si retorna falso
            client.loop();
            client.publish("id", "MUESTRE CARNET");
             delay(2000);
            Serial.println("MUESTRE CARNET"); }   // muestra texto equivalente a acceso denegado          
                  
                  mfrc522.PICC_HaltA();     // detiene comunicacion con tarjeta                

}

boolean comparaUID(byte lectura[],byte usuario[]) // funcion comparaUID
{
  for (byte i=0; i < mfrc522.uid.size; i++){    // bucle recorre de a un byte por vez el UID
  if(lectura[i] != usuario[i])        // si byte de UID leido es distinto a usuario
    return(false);          // retorna falso
  }
  return(true);           // si los 4 bytes coinciden retorna verdadero
}
