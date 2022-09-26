![](https://img.shields.io/badge/tensorflow-%3E%3D1.15.2-brightgreen) ![](https://img.shields.io/badge/keras-2.3.1-brightgreen) ![](https://img.shields.io/badge/imutils-0.5.3-brightgreen) ![](https://img.shields.io/badge/numpy-1.18.2-brightgreen) ![](https://img.shields.io/badge/opencv--python-4.2.0.*-brightgreen) ![](https://img.shields.io/badge/matplotlib-3.2.1-brightgreen) ![](https://img.shields.io/badge/scipy-1.4.1-brightgreen) ![](https://img.shields.io/badge/flask-2.0.2-orange) ![](https://img.shields.io/badge/flask--bcrypt-0.7.1-orange) ![](https://img.shields.io/badge/jinja2-3.0.3-orange) ![](https://img.shields.io/badge/pymysql-1.0.2-orange) ![](https://img.shields.io/badge/selenium-4.1.0-brightgreen) ![]() ![]() ![]() ![]() ![]() ![]() ![]() ![]() 

<center><a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/SsHgvXcM/Toll-Kit-github.png' border='0' alt='Toll-Kit-github'/></a></center>
<h1>Welcome to TollKit!</h1>
<p>A día de hoy la pandemia ha cambiado en muchas formas la manera en cómo salimos y entramos a establecimientos (Centros comerciales, restaurantes, universidades, etc.) por restricciones de COVID-19. A partir de esto han surgido nuevas responsabilidades como el del personal de seguridad encargado de verificar si cuentas con Mascarilla, Carnet de Vacunación con 3 dosis, Temperatura menor a 38.5, Carnet Universitario, verter alcohol en gel para la desinfección de tus manos y finalmente permitirte el pase al establecimiento.
<p>Identificamos las siguientes 3 problemáticas:</p>
<ul>
    <li>Realizar este tipo de tareas repetitivas termina siendo estresante para el personal de seguridad generando tensiones musculares, inflamación, problemas con los nervios, etc.</li>
    <li>Al ser el personal de seguridad un intermediario entre todas las personas del exterior y el establecimiento, existe un mayor riesgo de contagio debido a que si el personal de seguridad se contagia de forma asintomática, podría inconscientemente contagiar a cada persona que va ingresando al establecimiento siendo esto perjudicial.</li>
    <li>Es cierto que en muchos lugares el personal de seguridad está atento a que cada persona cumpla con las consideraciones mínimas para ingresar a un establecimiento, sin embargo, también es cierto que entre tantas personas, el error humano puede estar presente. El personal de seguridad no siempre verifica que se tenga un carnet de vacunación real y muchas veces vierte cualquier cantidad de gel.</li>
</ul>
Por esa razón decidimos crear TollKit, una herramienta que busca complementar la labor del personal de seguridad haciendo todas las tareas repetitivas de verificación de Mascarilla, Carnet de Vacunación con 3 dosis, Temperatura menor a 38.5, Carnet Universitario y dispensar alcohol en gel. Proporcionando además un Dashboard con todas las métricas necesarias para tener controladas las restricciones por COVID19. De esta forma, el personal podrá hacerse cargo de otras responsabilidades que impliquen un esfuerzo humano necesario.
</p>

<h3>Views</h3>
<h2>User Screen</h2>
<a href='https://postimg.cc/FYGwmHXn' target='_blank'><img src='https://i.postimg.cc/25fYQ1cm/Vista-Usuario.png' border='0' alt='Vista-Usuario'/></a>

<h2>Dashboard</h2>
<a href='https://postimg.cc/gLn2yTqG' target='_blank'><img src='https://i.postimg.cc/QCqKDLFK/dashboard-Tollkit.png' border='0' alt='dashboard-Tollkit'/></a>

<h2>Electronic Device</h2>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/ZRpVrqQk/Captura-de-pantalla-2022-08-27-153139.png' border='0' alt='Captura-de-pantalla-2022-08-27-153139'/></a>

<h3>Electronic Components</h3>
<p>
<ul>
    <li>RFID</li>
</ul>
</p><a href='https://postimg.cc/D8qqJHrj' target='_blank'><img src='https://i.postimg.cc/D8qqJHrj/RFID.png' border='0' alt='RFID'/></a>
<p>
RFID o Radio Frequency Identification es una tecnología mediante la cual los datos digitales codificados en etiquetas RFID o etiquetas inteligentes son capturados por un lector RFID a través de ondas de radio.
</p>
<p>
<ul>
    <li>ESP32</li>
</ul>
</p><a href='https://postimg.cc/dDX7BYmQ' target='_blank'><img src='https://i.postimg.cc/dDX7BYmQ/esp32.png' border='0' alt='esp32'/></a>
<p>
Microcontrolador programable con ide arduino con un módulo WiFi integrado. Este será usado para la adquisición de las señales porvenientes de los sensores y del envío de datos mediante MQTT.
</p>
<p>
<ul>
    <li>Raspberry 3B+</li>
</ul>
</p><a href='https://postimg.cc/18jJf6tS' target='_blank'><img src='https://i.postimg.cc/18jJf6tS/pngfind-com-raspberry-pi-3-png-5955099.png' border='0' alt='pngfind-com-raspberry-pi-3-png-5955099'/></a>
<p>
Este modelo de Raspberry es un computador de placa única (SBC) de bajo costo, posee la capacidad de funcionar como una computadora personal completa y usarla para navegar por internet. La tarea de esta placa será recepcionar los datos brindados por los sensores usando MQTT y la presentación de los mismos en una aplicación web.
</p>
<p>
<ul>
    <li>HC-SR04 Ultrasonic Sensor</li>
</ul>
</p><a href='https://postimg.cc/V0LczT44' target='_blank'><img src='https://i.postimg.cc/V0LczT44/pngwing-com.png' border='0' alt='pngwing-com'/></a>
<p>
El sensor HC-SR04 es un sensor de distancia de bajo costo que utiliza ultrasonido para determinar la distancia de un objeto en un rango de 2 a 450 cm. Destaca por su pequeño tamaño, bajo consumo energético y buena precisión
</p>
<p>
<ul>
    <li>Mlx90614 Infrared Temperature Sensor</li>
</ul>
</p><a href='https://postimg.cc/hfD9qrnj' target='_blank'><img src='https://i.postimg.cc/hfD9qrnj/MLX90614.png' border='0' alt='MLX90614'/></a>
<p>
El Sensor de temperatura infrarrojo MLX90614 permite medir la temperatura de un objeto a distancia(sin contacto). El Sensor MLX90614 es un chip de silicio con una fina membrana micromecanizada, diseñada para ser sensible a la radiación infrarroja emitida por un objeto a distancia. El sensor posee internamente una etapa de amplificación y digitalización(ADC) de la señal procedente de la membrana. La salida del sensor es lineal y se compensa de acuerdo a las variaciones de la temperatura ambiente.
</p>
<p>
<ul>
    <li>Relay</li>
</ul>
</p><a href='https://postimg.cc/5XZg1CpR' target='_blank'><img src='https://i.postimg.cc/5XZg1CpR/82ac7be2-6368-41f2-8fb3-a7e34b515b6c.png' border='0' alt='82ac7be2-6368-41f2-8fb3-a7e34b515b6c'/></a>
<p>
Para el desarrollo del proyecto se requiere el control de una bomba de agua, la cual no puede ser manejado directamente con Arduino. En estos casos es necesario utilizar Relays o Reles, estos dispositivos permiten controlar cargas de alto voltaje con una señal pequeña.
</p>
        
<h3>Technologies</h3>

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

<h3>Team Members</h3>
<ul>
    <li>Sebastián Nizama</li>
    <li>Richard Elescano</li>
    <li>Marko Julca</li>
    <li>Nicolás Silva</li>
    <li>Jhomar Astuyauri</li>
</ul>
