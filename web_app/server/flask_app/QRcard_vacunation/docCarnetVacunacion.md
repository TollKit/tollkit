<h1>Desarrollo de la Detección de Carnet de Vacunación a través del QR  </h1>

# Codigo-QR

## Acerca de la automatización para el acceso

Para un mayor alcance en la data de las personas en relación a las dosis de la vacuna contra la covid 19, el minsa es la institución la cual
posee la información que se usara para la obtención de los datos de los usuarios que iran pasando atravez de Tollkit, los datos que obtendremos son el nombre, la cantidad de dosis y la edad, esto con el fin de ir registrando y corroborando posteriormente atravez de flask, si de acuerdo con la edad que tenga el usuario cumpla con el mínimo de dosis suministradas.
La interacción física con Tollkit en el proceso de automatización se dara mediante el lector de código qr que la página del minsa posee, mediante Seleium el proceso de automatización para el control de dosis se podrá llevar acabo.

## API documentación:

* [Selenium](https://github.com/SeleniumHQ/selenium)
<h3>Automatización de la página del Minsa</h3>
<p>Para el proceso de automatización de la pagina:</p>
<ul>
  <li>A través de Selenium y el lenguaje de programación de Python, comanzaremos controlando mediante un WebDriver el navegador que usaremos, por ejemplo si quisieramos controlar desde el navegador Chrome será:
https://chromedriver.chromium.org/downloads, para saber la versión que se debera descargar, nos dirigimos a la sección-Ayuda-del navegador posteriormente se le dara a -Información de Google Chrome-y se podra observar la versión que se este usando, para luego pasar a la descarga del controlador del navegador.</li>
<li>Para la codificación identificaremos la ruta en donde guardamos el controlador del navegador: C:/Program Files (x86)/chromedriver.exe, definimos como path a esta ruta, posteriormente usaremos la ruta de la página:     website='https://carnetvacunacion.minsa.gob.pe/#/verify-qr/enable, usaremos webdriver.Chrome para poder abrir la página que desea usar, creamos los elementos nombres, dosis y edad, usaremos el atributo xpath, usaremos el método que nos
devolvera una lista de palabras claves que queremos que nos retorne, en este caso el nombre del usuario, la palabra que muestre la cantidad de dosis y la edad, el atributo usado sera el find_element.' 
</li>
 </ul>
