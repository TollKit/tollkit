// CREDENCIALES 
 char* ssid = "Nizama iPhone 11";
 const char* contrasena = "sebastian54321";
 //char* ssid = "JUL_NIZ";
 //const char* contrasena = "FIEE20182";

int trig = 25;
int echo = 26;
int relay = 4;
long tiempo;
long distancia;
int estado_actual = 0;

// sensor temperatura
#include <Adafruit_MLX90614.h> 
#include<Wire.h>
#include <WiFi.h>
#include<PubSubClient.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);
#include <SPI.h>      // incluye libreria bus SPI
#include <MFRC522.h>      // incluye libreria especifica para MFRC522
#define SS_PIN 5
#define RST_PIN 2
const char* servidor_mqtt= "172.20.10.5"; //mosquitto
int puerto = 1883;
 
WiFiClient espClient;
PubSubClient client(espClient);
MFRC522 mfrc522(SS_PIN, RST_PIN); // crea objeto mfrc522 enviando pines de slave select y reset
//sensor de temperatura
Adafruit_MLX90614 mlx = Adafruit_MLX90614(); 
int alarma = 33;         // valor de temperatura de alarma
int calibracion = 5;     // factor de calibracion 


byte LecturaUID[4];         // crea array para almacenar el UID leido
byte Usuario1[4]= {0x82, 0x95, 0x40, 0x1C} ;    // UID de tarjeta leido en programa 1
byte Usuario2[4]= {0xE0, 0xB2, 0x4E, 0xD3} ;    // UID de llavero leido en programa 1

void setup_wifi(){
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid,contrasena);
  //Conexion a wifi
  while(WiFi.status()!=WL_CONNECTED){
  delay(300);
  Serial.print(".");
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
  //sensor ultrasonico
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(relay, OUTPUT);
  digitalWrite(relay, HIGH);
  digitalWrite(trig, LOW);//Inicializamos el pin con 0
  
  Serial.begin(115000); 
  setup_wifi();
  client.setServer (servidor_mqtt, puerto);
  mlx.begin(); // sensor de temperatura
  SPI.begin();        // inicializa bus SPI
  mfrc522.PCD_Init();     // inicializa modulo lector
  Serial.println("Listo");    // Muestra texto Listo

  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(5,0);
  lcd.print("TOLLKIT"); // Mensaje a desplegar
  delay(3000); // espera 3 segundos con el mensaje estatico
}

void loop() {
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  tiempo = pulseIn(echo, HIGH);
  distancia = tiempo / 58.2;
  if (estado_actual == 0){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("1/5 Reconocim."); // Mensaje a desplegar
    lcd.setCursor(0,1);
    lcd.print("de mascarilla"); // Mensaje a desplegar
    delay(10000);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("2/5 Carnet de"); // Mensaje a desplegar
    lcd.setCursor(0,1);
    lcd.print("vacunacion (QR)"); // Mensaje a desplegar
    delay(5000);
    estado_actual = 1;
    }
  if (estado_actual == 1){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("3/5 Medicion de"); // Mensaje a desplegar
    lcd.setCursor(0,1);
    lcd.print("temperatura"); // Mensaje a desplegar
    }
  if (estado_actual == 2){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("4/5 Carnet"); // Mensaje a desplegar
    lcd.setCursor(0,1);
    lcd.print("universiario"); // Mensaje a desplegar
    }
  if (estado_actual == 3){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("5/5 Desinfeccion"); // Mensaje a desplegar
    lcd.setCursor(0,1);
    lcd.print("de manos"); // Mensaje a desplegar
    }
  
  if (distancia <= 8 && estado_actual==3){
    Serial.print(distancia);      //Enviamos serialmente el valor de la distancia
    Serial.print("cm ");
    Serial.println("GEL");
    client.publish("gel", "OK"); //ENVIO MQTT GEL
    digitalWrite(relay, LOW);
    delay(4000);
    client.publish("alcohol", "True"); //ENVIO MQTT TEMPERATURA
    digitalWrite(relay, HIGH);
    estado_actual = 0;
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Gel: "); // Mensaje a desplegar
    lcd.setCursor(0,1);
    lcd.print("OK"); // Mensaje a desplegar
    delay(3000); // espera 3 segundos con el mensaje estatico
  }
  else{
    Serial.println("ESTATICO");
    //digitalWrite(relay, LOW);
    Serial.print(distancia);      //Enviamos serialmente el valor de la distancia
    Serial.print("cm ");
  }
  
  double h=mlx.readObjectTempC()+calibracion; //lectura del sensor de temperatura
  String ST=String(h,2);
  if(!client.connected()) //para que se reconecte//
  reconnect();
  
  //SENSOR TEMPERATURA
  client.loop();
  if(h>28 && estado_actual==1){
    client.publish("temp", ST.c_str()); //ENVIO MQTT TEMPERATURA
    estado_actual = 2;
    lcd.clear();
    lcd.setCursor(0,0) ;
    lcd.print("Temperatura:"); // Mensaje 2 a desplegar
    lcd.setCursor(0,1) ;
    lcd.print(ST); // Mensaje 2 a desplegar
    delay(2000);
    }
  //lcd.setCursor(0,1) ;
  //lcd.print(ST); // Mensaje 2 a desplegar
  Serial.println(ST);
  delay(2000);

  
  if ( ! mfrc522.PICC_IsNewCardPresent())   // si no hay una tarjeta presente
    return;           // retorna al loop esperando por una tarjeta
  
  if ( ! mfrc522.PICC_ReadCardSerial())     // si no puede obtener datos de la tarjeta
    return;           // retorna al loop esperando por otra tarjeta

  if(estado_actual==2){
    
    Serial.print("TOLLKIT:");       // muestra texto UID:
    for (byte i = 0; i < mfrc522.uid.size; i++) { // bucle recorre de a un byte por vez el UID
          
          LecturaUID[i]=mfrc522.uid.uidByte[i];     // almacena en array el byte del UID leido      
          }
          
          Serial.print("\t");         // imprime un espacio de tabulacion             
                    
          if(comparaUID(LecturaUID, Usuario1)){    // llama a funcion comparaUID con Usuario1
            client.loop();
            client.publish("rfid", "Estudiante UNI"); //id
            delay(2000);
            Serial.println("Bienvenido Jhomar Astuyauri");
            estado_actual = 3;
            lcd.clear();
            lcd.setCursor(0,0) ;
            lcd.print("Grupo:"); // Mensaje 2 a desplegar
            lcd.setCursor(0,1) ;
            lcd.print("Estudiante UNI"); // Mensaje 2 a desplegar
            delay(2000);
            } // si retorna verdadero muestra texto bienvenida
          
          else if(comparaUID(LecturaUID, Usuario2)){ // llama a funcion comparaUID con Usuario2
            client.loop();
            client.publish("rfid", "EXTRENO"); //id
            delay(2000);
            Serial.println("ACCESO DENEGADO");
            estado_actual = 3;
            lcd.clear();
            lcd.setCursor(0,0) ;
            lcd.print("Grupo:"); // Mensaje 2 a desplegar
            lcd.setCursor(0,1) ;
            lcd.print("Externo"); // Mensaje 2 a desplegar
            delay(2000);
            } // si retorna verdadero muestra texto bienvenida
          
          else{           // si retorna falso
            client.loop();
            client.publish("rfid", "MUESTRE CARNET"); //id
             delay(2000);
            Serial.println("MUESTRE CARNET"); }   // muestra texto equivalente a acceso denegado          
                  
          mfrc522.PICC_HaltA();     // detiene comunicacion con tarjeta
  }
  
  delay(3000);

}

boolean comparaUID(byte lectura[],byte usuario[]) // funcion comparaUID
{
  for (byte i=0; i < mfrc522.uid.size; i++){    // bucle recorre de a un byte por vez el UID
  if(lectura[i] != usuario[i])        // si byte de UID leido es distinto a usuario
    return(false);          // retorna falso
  }
  return(true);           // si los 4 bytes coinciden retorna verdadero
}
