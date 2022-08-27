# ---
import cv2
import numpy as np
from pyzbar.pyzbar import decode
#img=cv2.imread('descarga.png')

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
import time
print('Empezando')
while True:
    success, img=cap.read()
    try:
        for barcode in decode(img):
            print(barcode.data)
            myData=barcode.data.decode('utf-8')
            if 'minsa' in myData:
                print(type(myData))
                pts=np.array([barcode.polygonl.np.int32])
                pts=pts.reshape((-1,1,2)) 
                cv2.polylines(img,[pts],True,(255,0,255),5)
            else: print('Por favor presente un QR válido')
        cv2.imshow('Result',img)
        key= cv2.waitKey(1)
        if key==27:
            break
        #time.sleep(5)
    except:
        print('-'*100)
        print('Se ha detectado su carnet de vacunación')
#code=decode(img)
#print(code)
for barcode in decode(img):
    print(barcode.data)
    myData=barcode.data.decode('utf-8')
    print(myData)