# -*- coding: utf-8 -*-
#Usar OpenCV y la cámara

import cv2
import numpy as np
import time
import sys

def get_image():
     # leer la captura
     retval, im = video.read()#Se inica la lectura del video
     return im


if __name__=='__main__':
    datos=[]#Se crea la matriz que va a contener la información a mostrar (diferencias en los frames)
    camara = 0   #Defecto es 0
    video = cv2.VideoCapture(camara) #Se inicia la captura de video
    for i in range(0,19):
        img_1 = get_image()
        img_2= get_image()
        d=img_1-img_2 #se realiza la captura  de dos imagenes y se  restan para encontrar las diferencias
        suma=np.sum(d[:])# se hace la suma de todos los datos encontrados en la resta para identificarlos
        datos=[datos,suma]#Se agregan a la matriz original
        time.sleep(0.1)
 
#si no hay captura de video cerrar todo
    if not video:
        sys.exit(1)
     
    while True: 
        img = get_image()#Se obtiene un frame del video
        if img is None:
            break
        cv2.imshow("camara", img)#Se muestra la imagen capturada
        if cv2.waitKey(10) == 27:#Espera por 'ESC'
            break
    video.release()#Se cierra la camara
    cv2.destroyAllWindows()
