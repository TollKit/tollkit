import os
import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Imprimimos la versión de tensorflow
print(tf.__version__)

direc_entrenamiento='URL-DATASET'
direc_entre_mask=os.path.join(direc_entrenamiento,"with_mask")
direc_entre_No_mask=os.path.join(direc_entrenamiento,"without_mask")


print('total imagenes con mascarillas', len(os.listdir(direc_entre_mask)))
print('total imagenes sin mascarillas', len(os.listdir(direc_entre_No_mask)))


model=tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(150,150,3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(32, (3,3),activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3),activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512,activation='relu'),
    #Clasificacion binaria
    tf.keras.layers.Dense(1,activation= 'sigmoid')
    
])

# ------------------------

from tensorflow.keras.optimizers import Adam
model.compile(optimizer=Adam(lr=0.001),
            loss='binary_crossentropy',
            metrics=['accuracy'])

from tensorflow.keras.preprocessing.image import ImageDataGenerator
img_height =150
img_width=150
batch_size=10
train_datagen=ImageDataGenerator(rescale=1./255,
                                shear_range=0.2,
                                zoom_range=0.2,
                                horizontal_flip=True,
                                validation_split=0.2) #set validation split

train_generator =train_datagen.flow_from_directory(
direc_entrenamiento,
target_size=(img_height,img_width),
batch_size=batch_size,
class_mode='binary',
subset='training') #set as trainign data

validation_generator = train_datagen.flow_from_directory(
    direc_entrenamiento, #same directory as a training data
    target_size=(img_height,img_width),
    batch_size=batch_size,
    class_mode='binary',
    subset='validation' #data set para al validacion
)

nb_epochs =10
history =model.fit_generator(
    train_generator,
    steps_per_epoch = train_generator.samples // batch_size,
    validation_data = validation_generator,
    validation_steps=validation_generator.samples // batch_size,
    epochs = nb_epochs
)


import matplotlib.pyplot as plt
acc = history.history['accuracy']
loss =history.history['loss']

#Graficar la excatitud  vs las perdidas
epochs =range(len(acc))

#envio de datos a graficar 
plt.plot(epochs, acc, 'b', label='Exactitud del entrenamiento comunitarias mascarilla ')
plt.title('Exactitud del entrenamiento- P comunitarias')

plt.figure()

plt.plot(epochs, loss, 'b', label ='Error del training- P Comunitarias')
plt.title('Error de entrenamiento - P comunitarias')
plt.legend()

plt.show()


# -----------------------

import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from PIL import Image


vc = cv2.VideoCapture(0)

plt.ion()
if vc.isOpened(): 
    is_capturing, frame = vc.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)    
    webcam_preview = plt.imshow(frame)    
else:
    is_capturing = False
    
while is_capturing:
    try:    
        is_capturing, frame = vc.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
        #Lee el mismo size que espera el modelo y te ahorra reshapes
        frame_res = cv2.resize(frame, dsize=(150, 150), interpolation=cv2.INTER_CUBIC) 
        x=image.img_to_array(frame_res)
        x=np.expand_dims(x, axis=0)
        images = np.vstack([x])
        classes = model.predict(images, batch_size=10)
        if classes[0]>0:
            print("No lleva Mascarilla - P. Comunitarias")
        else:
            print("Si lleva Macarilla - P.Comunitarias")
        webcam_preview = plt.imshow(frame)
        
        webcam_preview.set_data(frame)
        plt.draw()
        try:    
            plt.pause(0.05)
        except Exception:
            pass
    except KeyboardInterrupt:
        vc.release()

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

open("mask_classifier.tflite","wb").write(tflite_model)