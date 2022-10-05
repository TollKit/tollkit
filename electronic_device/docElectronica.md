<h1>Desarrollo Electrónico</h1>


<h2>Componentes electrónicos</h2>

| Componente  | Descripción  | Imágen de referencia |
| :------------ |:---------------| -----:|
| RFID módulo RC522   | El módulo RC522 es Lector-Grabador RFID 13.56MHz, posee comunicación SPI lo que permite trabajar fácilmente con la mayoría de microcontroladores. El rango de detección de tags RFID es de aprox. 5-7cm. Compatible con Arduino, Pic, Raspberry Pi y más. | <a href='https://postimg.cc/D8qqJHrj' target='_blank'><img src='https://i.postimg.cc/D8qqJHrj/RFID.png' border='0' alt='RFID'/></a> |
| Sensor ultrasónico HC-SR04  | Es un módulo electrónico que incorpora un par de transductores de ultrasonido que se utilizan de manera conjunta para determinar la distancia entre el sensor (módulo) y un objeto. El tiempo entre la transmisión y la recepción de la señal ultrasónica es usada para calcular la distancia.  |  <a href='https://postimg.cc/V0LczT44' target='_blank'><img src='https://i.postimg.cc/V0LczT44/pngwing-com.png' border='0' alt='pngwing-com'/></a>|
| Sensor de temperatura infrorrojo Mlx90614 | Es un chip de silicio con una fina membrana micro mecanizada,diseñada para ser sensible a la radiación infrarroja emitida por un objeto a distancia. El sensor posee internamente una etapa de amplificación y digitalización(ADC) de la señal procedente de la membrana. La salida del sensor es lineal y se compensa de acuerdo a las variaciones de la temperatura ambiente. |    <a href='https://postimg.cc/hfD9qrnj' target='_blank'><img src='https://i.postimg.cc/hfD9qrnj/MLX90614.png' border='0' alt='MLX90614'/></a> |
| Relé optoacoplador de 5 V | Este módulo relé sirve para conmutación de cargas de potencia. Los contactos de los relevadores están diseñados para conmutar cargas de hasta 10 A y 250VAC (30VDC), aunque se recomienda dejar un margen abajo de estos límites. El modulo permite manejar la bobina del relé y la señal de control puede provenir de cualquier circuito de control TTL como un microcontrolador o tarjeta Arduino salidas desde 3.3V-5V.     |  <a href='https://postimg.cc/DWY6xpF1' target='_blank'><img src='https://i.postimg.cc/DWY6xpF1/rele.jpg' border='0' alt='rele'/></a>|
| Bomba de agua AD20P | Es una bomba de agua DC sin escobillas con las características de larga vida, bajo ruido, chispa inversa, etc. Sin interferencias electromagnéticas. Voltaje de funcionamiento: CC 12 V. Corriente de funcionamiento: 400 mA. Cabezal máximo: 118.1 in. Caudal máximo: 240 L.  |  <a href='https://postimg.cc/7fYVyy6S' target='_blank'><img src='https://i.postimg.cc/7fYVyy6S/pump.jpg' border='0' alt='pump'/></a>|
| ESP32 | Microcontrolador programable con ide arduino con un módulo WiFi integrado. Este será usado para la adquisición de las señales porvenientes de los sensores y del envío de datos mediante MQTT.  |  <a href='https://postimg.cc/dDX7BYmQ' target='_blank'><img src='https://i.postimg.cc/dDX7BYmQ/esp32.png' border='0' alt='esp32'/></a>|

<h2>Implementación</h2>
<h3>Sensor de temperatura</h3>
Para esta aplicacion en especifico se uso este sensor para medir la temperatura corporal de las personas que desean ingresar a un espacio publico y que segun bajo las regulaciones del minsa ésta no puede exceder los 38°C.
<a href='https://postimg.cc/0r5stBmr' target='_blank'><img src='https://i.postimg.cc/0r5stBmr/MLX90614-with-ESP32-connection-diagram.jpg' border='0' alt='MLX90614-with-ESP32-connection-diagram'/></a>

---------

Las conexiones serán las siguientes:

* VIN: +3.3V - +5.0V DC
* GND: 0V Tierra
* SCL: I2C clock
* SCL: I2C clock
* SDA: I2C data

---------
Para usar este sensor en el IDE de arduino debemos descargar la librería "Adafruit_MLX90614.h"

--------

Inicialmente llamamos a las librerias a utilizar , luego definimos las variables alarma y calibracion que seran las necesarias para indicar cuando la temperatura corporal de la persona sobrepase los 38°C, y la variable calibracion es necesaria para obtener una medicion mas exacta de nuestro sensor. Luego en el programa utilizamos el metodo de la clase mlx , el cual es :"mlx.readObjectTempC" el cual nos brindara la temperatura en °C, con este valor ajustaremos el valor de alarma para que envie un mensaje cuando se sobrepase el valor maximo. Finalmente enviaremos los datos via wifi utilizando el ESP32 con la libreria pubsubclient y mediante el protocolo MQTT.

<h3>Sensor ultrasónico</h3>
Para esta aplicación en específico se usó este sensor para realizar un dispensador en gel sin contacto, es decir, las personas en el ingreso al establecimiento solo deben acercar sus manos cierta distancia y con ayuda de este sensor se activará una bomba para dispensar alcohol en gel a fin de desinfectar las manos de la persona y cumplir con los protocolos sanitarios.
<a href='https://postimg.cc/8jJLqDrC' target='_blank'><img src='https://i.postimg.cc/8jJLqDrC/1617136789-426-Tutorial-de-sensores-ultrasonicos-para-Arduino-ESP8266-y-ESP32.png' border='0' alt='1617136789-426-Tutorial-de-sensores-ultrasonicos-para-Arduino-ESP8266-y-ESP32'/></a>

---------

Las conexiones serán las siguientes:

* VCC (+5V DC)
* TRIG (Disparo del ultrasonido)
* ECHO (Recepción del ultrasonido)
* GND (Tierra: 0V)

---------
Para usar este sensor en el IDE de arduino no se utiliza librerías especiales para el sensor, solamente se utiliza la función "pulseIn" incluida en el IDE de Arduino para medir la longitud del pulso de eco que devuelve el sensor ultrasónico.

--------

Inicialmente se definen las variables en los pines y su estado de entrada o salida En este caso en particular se utilizó un relé como salida para activar la bomba que nos dispensara el alcohol en gel. Luego en el programa se realiza la ecuación del tiempo con la funcion Pulsein y se configura par aunque si la distancia es menor a 5 el relé se active y de lo contrario no lo haga Finalmente enviaremos los datos que indiquen si el relé se activó o no via wifi utilizando el ESP32 con la libreria "wifi.h" y la libreria "pubsubclient" para usar el protocolo MQTT.

<h3>Módulo RFID</h3>
Para esta aplicacion en especifico se uso este modulo para regular el ingreso en los establecimientos solo de personas autorizadas pertenecientes a la organizacion o invitados registrados.

<a href='https://postimg.cc/9RyyrBCq' target='_blank'><img src='https://i.postimg.cc/9RyyrBCq/RFID-ESP32-Node-MCU-Steckplatine.png' border='0' alt='RFID-ESP32-Node-MCU-Steckplatine'/></a>

---------

Las conexiones serán las siguientes:

<a href='https://postimg.cc/ThqHsVgw' target='_blank'><img src='https://i.postimg.cc/ThqHsVgw/nfc-osc-bb-g-Bdc-Dg8-Rq9.jpg' border='0' alt='nfc-osc-bb-g-Bdc-Dg8-Rq9'/></a>

---------
Para poder trabajar el Modulo en Arduino es necesario descargar su librería correspondiente, la que usaremos será la libreria : "MFRC522"

--------

Se tiene primero un código para leer el código de identificación de nuestros Tags, lo cual es necesario para realizar el control de acceso. Una vez obtenido los códigos de nuestros tags, ya podemos realizar el control de acceso indicando que códigos serán los que tendrán permitidos el ingreso, para ello primero se llama a las librerias a utilizar y luego de esto se crea objeto mfrc522 enviando pines de slave select y reset con esta linea: 
* MFRC522 mfrc522(SS_PIN, RST_PIN);
Posterior a esto se definen los usuarios que tendran permitido el ingreso, en este caso son los siguientes:
* byte Usuario1[4]= {0x82, 0x95, 0x40, 0x1C} ;    // UID de tarjeta leido en programa 1
* byte Usuario2[4]= {0xE0, 0xB2, 0x4E, 0xD3} ;    // UID de llavero leido en programa 1
Luego, con los metodos 
* mfrc522.PICC_IsNewCardPresent y mfrc522.PICC_ReadCardSerial
conoceremos si hay una tarjeta presente o si no se peuden obtener datos 
de la tarjeta
finalmente se imprime el mensaje de acceso concedido o acceso denegado
Todos los datos son enviados via WiFi por el ESP 32 con la libreria "WiFi.h"
y "pubsubclient" para hacer uso del protocolo MQTT

