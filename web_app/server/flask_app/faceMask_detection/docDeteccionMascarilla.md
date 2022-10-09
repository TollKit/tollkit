<h1>Desarrollo del Reconocimiento de Mascarilla </h1>

## Repositorio de referencia

https://github.com/balajisrinivas/Face-Mask-Detection

## Repositorio de referencia

Video de guía para uso del código

## Topología de la CNN

Para el entrenamiento del modelo se aplica transfer learning con el modelo base MobileNetV2. 
MobileNetV2 es una arquitectura de red neuronal convolucional que busca funcionar bien en dispositivos móviles. Se basa en una estructura residual invertida donde las conexiones residuales se encuentran entre las capas de cuello de botella. La capa de expansión intermedia utiliza circunvoluciones ligeras en profundidad para filtrar entidades como fuente de no linealidad. En conjunto, la arquitectura de MobileNetV2 contiene la capa inicial de convolución completa con 32 filtros, seguida de 19 capas de cuello de botella residuales.

## Requerimientos

* Python 3.6 (única versión de Python 3 que permite la instalación de tensorflow 1)

* Numpy 1.18.2 (importante)

* Scipy 1.4.1 (importante)

* Keras 

* Tensorflow 1.7.0

