# Sistema de Control de Acceso por COVID-19 [Open Source]

![](https://img.shields.io/badge/tensorflow-%3E%3D1.15.2-brightgreen) ![](https://img.shields.io/badge/keras-2.3.1-brightgreen) ![](https://img.shields.io/badge/imutils-0.5.3-brightgreen) ![](https://img.shields.io/badge/numpy-1.18.2-brightgreen) ![](https://img.shields.io/badge/opencv--python-4.2.0.*-brightgreen) ![](https://img.shields.io/badge/matplotlib-3.2.1-brightgreen) ![](https://img.shields.io/badge/scipy-1.4.1-brightgreen) ![](https://img.shields.io/badge/flask-2.0.2-orange) ![](https://img.shields.io/badge/flask--bcrypt-0.7.1-orange) ![](https://img.shields.io/badge/jinja2-3.0.3-orange) ![](https://img.shields.io/badge/pymysql-1.0.2-orange) ![](https://img.shields.io/badge/selenium-4.1.0-brightgreen) ![](https://img.shields.io/badge/pyautogui-0.9.53-red) ![]() ![]() ![]() ![]() ![]() ![]() ![]() 

 <a width="400" href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/SsHgvXcM/Toll-Kit-github.png' border='0' alt='Toll-Kit-github'/></a>

## Acerca del Proyecto

<a href='https://postimg.cc/GTtQ7r0N' target='_blank'><img src='https://i.postimg.cc/kGFp5XTn/Whats-App-Image-2022-09-27-at-5-39-10-PM.jpg' border='0' alt='Whats-App-Image-2022-09-27-at-5-39-10-PM'/></a>

### Motivación

Buscamos inspirar a la próxima generación de científicxs e ingenierxs para que nos ayuden a explorar y aprender sobre tecnología. Compartimos la documentación completa de este dispositivo como una forma de aporte al desarrollo tecnológico a través de un proyecto divertido.

### Habilidades

Este proyecto tiene elementos de ensamblaje mecánico, utiliza componentes electrónicos y tiene un software que se encargará de ejecturar todo. Para completar con éxito este proyecto necesitará tener algo de experiencia en lo siguiente:

* **Diseño Mécanico:** Para diseñar el chasis junto a los compartimentos para almacenar cada módulo electrónico.

* **Electrónica:** Para implementar los diferentes módulos electrónicos que luego serán comunicados por MQTT a Flask.

* **Software::** Para el reconocimiento de mascarilla, detección del carnet de vacunación a través del QR y el desarrollo web.

La mayoría de requisitos son habilidades que puede aprender y adquirir con bastante rapidez viendo videos e investigando en Internet, y a lo largo del proyecto también tratamos de brindar información complementaria sobre algunas de ellas.

### Compromiso de tiempo esperado

Según nuestra experiencia, la construcción de este proyecto requiere no menos de 100 horas-persona y, según la familiaridad y el nivel de habilidad de los involucrados, podría ser mucho más. *Sin embargo, este proyecto generalmente pretende ser una herramienta de enseñanza y aprendizaje.* A lo largo de la documentación, tratamos de brindar información complementaria para aquellos que puedan ser nuevos en este tipo de proyecto.



### Roadmap de implementación

<a href='https://postimg.cc/MMtP3vhz' target='_blank'><img src='https://i.postimg.cc/gjbCJhsL/roadmap-Toll-Kit.jpg' border='0' alt='roadmap-Toll-Kit'/></a>

Esta es una ruta para construir un TollKit y se divide en 6 etapas:

* **Etapa 1:** Empieza planificando el proyecto, teniendo en cuenta la disponibilidad de cada miembro, conocimientos y nuevas funcionalidades que quieran integrarle. Te recomendamos usar Trello!

* **Etapa 2:** Consigue todos los componentes electrónicos, filamento y elabora una arquitectura de software.
* **Etapa 3:** Empieza a probar el correcto funcionamiento de cada módulo electrónico por separado y descarga las librerías/frameworks necesarios.
* **Etapa 4:** Ensambla el diseño 3D y prueba los módulos de visión computarizada.
* **Etapa 5:** Monta los módulos electrónicos en el chasis e integralos con el servidor de Flask.
* **Etapa 6:** Después de que todo haya sido probado, calibrado y el software esté funcionando, ¡TollKit estará listo para su uso!

## Empieza aquí

* [Electrónica](https://github.com/)
* [Visión Computarizada](https://github.com/)
* [Diseño 3D](https://github.com/)
* [Desarrollo Web](https://github.com/)

## Equipo

Estos fueron los creadores originales de este proyecto. Ahora, este repositorio de código abierto está a cargo de mantenedores voluntarios de la comunidad.

<ul>
    <li>Sebastián Nizama (Electónica) - octavio.nizama.z@uni.pe </li>
    <li>Richard Elescano (Electónica) - relescanor@uni.pe</li>
    <li>Marko Julca (Visión Computarizada) - marko.julca.g@uni.pe</li>
    <li>Nicolás Silva (Electónica & Diseño 3D) - nicolas.silva.m@uni.pe</li>
    <li>Jhomar Astuyauri (Producto & Desarrollo Web) - jhomar.astuyauri.h@uni.pe</li>
</ul>

### Especial agradecimiento

Héctor Llamaccponca, Jean Kevin Inga y Paulo Quispe

------------------------------------------------------------------------


A día de hoy la pandemia ha cambiado en muchas formas la manera en cómo salimos y entramos a establecimientos (Centros comerciales, restaurantes, universidades, etc.) por restricciones de COVID-19. A partir de esto han surgido nuevas responsabilidades como el del personal de seguridad encargado de verificar si cuentas con Mascarilla, Carnet de Vacunación con 3 dosis, Temperatura menor a 38.5, Carnet Universitario, verter alcohol en gel para la desinfección de tus manos y finalmente permitirte el pase al establecimiento.
<p>Identificamos las siguientes 3 problemáticas:</p>
<ul>
    <li>Realizar este tipo de tareas repetitivas termina siendo estresante para el personal de seguridad generando tensiones musculares, inflamación, problemas con los nervios, etc.</li>
    <li>Al ser el personal de seguridad un intermediario entre todas las personas del exterior y el establecimiento, existe un mayor riesgo de contagio debido a que si el personal de seguridad se contagia de forma asintomática, podría inconscientemente contagiar a cada persona que va ingresando al establecimiento siendo esto perjudicial.</li>
    <li>Es cierto que en muchos lugares el personal de seguridad está atento a que cada persona cumpla con las consideraciones mínimas para ingresar a un establecimiento, sin embargo, también es cierto que entre tantas personas, el error humano puede estar presente. El personal de seguridad no siempre verifica que se tenga un carnet de vacunación real y muchas veces vierte cualquier cantidad de gel.</li>
</ul>
Por esa razón decidimos crear TollKit, una herramienta que busca complementar la labor del personal de seguridad haciendo todas las tareas repetitivas de verificación de Mascarilla, Carnet de Vacunación con 3 dosis, Temperatura menor a 38.5, Carnet Universitario y dispensar alcohol en gel. Proporcionando además un Dashboard con todas las métricas necesarias para tener controladas las restricciones por COVID19. De esta forma, el personal podrá hacerse cargo de otras responsabilidades que impliquen un esfuerzo humano necesario.
</p>
<h2>Vistas</h2>

<h3>Vista de usuario</h3>

<a href='https://postimg.cc/FYGwmHXn' target='_blank'><img src='https://i.postimg.cc/25fYQ1cm/Vista-Usuario.png' border='0' alt='Vista-Usuario'/></a>

<h3>Dashboard</h3>
<a href='https://postimg.cc/gLn2yTqG' target='_blank'><img src='https://i.postimg.cc/QCqKDLFK/dashboard-Tollkit.png' border='0' alt='dashboard-Tollkit'/></a>

<h2>Tecnologias</h2>
<table>
    <tbody>
        <tr>
            <td>Programming languages</td>
            <td>C, Python and SQL</td>
        </tr>
        <tr>
            <td>Libraries/MicroFramework/Framework</td>
            <td>Flask, PyMySQL, Bycript, REGEX, Flash, TensorFlow (2.9.1), Keras, Numpy, OS, OpenCV, Matplotlib and Pillow </td>
        </tr>
        <tr>
            <td>Hardware</td>
            <td>Arduino Nano, Raspberry 3B+, HC-SR04 Ultrasonic Sensor, Mlx90614 Infrared Temperature Sensor, Relay, RFID Card, LCD with I2C module, LED Matrix, Buzzer and LEDS</td>
        </tr>
        <tr>
            <td>IDE/Code Editor/Desktop Application</td>
            <td>Arduino IDE, VSCode, Solidworks and ThonnyIDE</td>
        </tr>
        <tr>
            <td>Methodology</td>
            <td>Design Thinking and Software Development Cycle + Product Roadmap</td>
        </tr>
        <tr>
            <td>Extra</td>
            <td>PLA Filament, Water Pump, Jumpers, Tripod and Matte Black Spray</td>
        </tr>
    </tbody>
<table>

<h2>Equipo electrónico</h2>
<h3>Toolkit implementado</h3>

<a href='https://postimg.cc/68HMgmcM' target='_blank'><img src='https://i.postimg.cc/68HMgmcM/tool.png' border='0' alt='tool'/></a>


<h3>Componentes electrónicos</h3>

| Componente  | Descripción  | Imágen de referencia |
| :------------ |:---------------| -----:|
| RFID módulo RC522   | El módulo RC522 es Lector-Grabador RFID 13.56MHz, posee comunicación SPI lo que permite trabajar fácilmente con la mayoría de microcontroladores. El rango de detección de tags RFID es de aprox. 5-7cm. Compatible con Arduino, Pic, Raspberry Pi y más. | <a href='https://postimg.cc/D8qqJHrj' target='_blank'><img src='https://i.postimg.cc/D8qqJHrj/RFID.png' border='0' alt='RFID'/></a> |
| Sensor ultrasónico HC-SR04  | Es un módulo electrónico que incorpora un par de transductores de ultrasonido que se utilizan de manera conjunta para determinar la distancia entre el sensor (módulo) y un objeto. El tiempo entre la transmisión y la recepción de la señal ultrasónica es usada para calcular la distancia.  |  <a href='https://postimg.cc/V0LczT44' target='_blank'><img src='https://i.postimg.cc/V0LczT44/pngwing-com.png' border='0' alt='pngwing-com'/></a>|
| Sensor de temperatura infrorrojo Mlx90614 | Es un chip de silicio con una fina membrana micro mecanizada,diseñada para ser sensible a la radiación infrarroja emitida por un objeto a distancia. El sensor posee internamente una etapa de amplificación y digitalización(ADC) de la señal procedente de la membrana. La salida del sensor es lineal y se compensa de acuerdo a las variaciones de la temperatura ambiente. |    <a href='https://postimg.cc/hfD9qrnj' target='_blank'><img src='https://i.postimg.cc/hfD9qrnj/MLX90614.png' border='0' alt='MLX90614'/></a> |
| Relé optoacoplador de 5 V | Este módulo relé sirve para conmutación de cargas de potencia. Los contactos de los relevadores están diseñados para conmutar cargas de hasta 10 A y 250VAC (30VDC), aunque se recomienda dejar un margen abajo de estos límites. El modulo permite manejar la bobina del relé y la señal de control puede provenir de cualquier circuito de control TTL como un microcontrolador o tarjeta Arduino salidas desde 3.3V-5V.     |  <a href='https://postimg.cc/DWY6xpF1' target='_blank'><img src='https://i.postimg.cc/DWY6xpF1/rele.jpg' border='0' alt='rele'/></a>|
| Bomba de agua AD20P | Es una bomba de agua DC sin escobillas con las características de larga vida, bajo ruido, chispa inversa, etc. Sin interferencias electromagnéticas. Voltaje de funcionamiento: CC 12 V. Corriente de funcionamiento: 400 mA. Cabezal máximo: 118.1 in. Caudal máximo: 240 L.  |  <a href='https://postimg.cc/7fYVyy6S' target='_blank'><img src='https://i.postimg.cc/7fYVyy6S/pump.jpg' border='0' alt='pump'/></a>|
| ESP32 | Microcontrolador programable con ide arduino con un módulo WiFi integrado. Este será usado para la adquisición de las señales porvenientes de los sensores y del envío de datos mediante MQTT.  |  <a href='https://postimg.cc/dDX7BYmQ' target='_blank'><img src='https://i.postimg.cc/dDX7BYmQ/esp32.png' border='0' alt='esp32'/></a>|

<h2>aplicación web</h2>
<h3>Programa de detección de mascarilla</h3>

