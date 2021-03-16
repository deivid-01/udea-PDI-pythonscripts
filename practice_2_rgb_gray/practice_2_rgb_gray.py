# -*- coding: utf-8 -*-
import cv2
import numpy as np

def mouse(event, x, y, flags, param): #Posición del mouse
    if event==cv2.EVENT_MOUSEMOVE:
        print('RGB Pixel (', x ,', ', y ,'): ', imagen.item(y, x, 2), '/', imagen.item(y, x, 1), '/' , imagen.item(y, x, 0))#Se muestran en consola los datos del pixel donde se encuentra posicionado el mouse
        
def separar(imagen):
    while(1):
        imagenGrayScale=cv2.imread("rgb.png",0)#Se carga la imagen en escala de grises=0, RGB=1, default=BGR
        cv2.namedWindow('imageGray')# Se le asigna un nombre a la ventana
        cv2.setMouseCallback('imageGray',mouse) #Se llama al método  encargado de detectar el movimiento del mouse
        cv2.imshow('imageGray',imagenGrayScale)#Se muestra la imagen en escala de grises
        cv2.namedWindow('image')#Se crea la ventana y se le asigna un nombre
        
        cv2.setMouseCallback('image',mouse)#Se llama al método encargado de decirnos la posicion del mouse cada que se mueva y la información de la mat4riz en esa posición
        
        cv2.imshow('image',imagen)# Muestra la imagen
        cv2.namedWindow('b')#Crea una nueva ventana
        cv2.setMouseCallback('b',mouse)#Llama al método encargado de obtenener las coordenadas del mouse
        b = imagen.copy()#Se crea una copia de la imagen original
        b[:,:,1] = 0    #Se hace 0 (negro) el componente G
        b[:,:,2] = 0    #Se hace 0 (negro) el componente R
        cv2.imshow('b',b)#Se muestra la imagen unicamente con el componente B
        #Set blue and red Channel to 0
        cv2.namedWindow('g')
        cv2.setMouseCallback('g',mouse)
        g = imagen.copy()#Se crea una copia de la imagen original
        g[:,:,0] = 0 #Se hace 0 (negro) el componente B
        g[:,:,2] = 0 #Se hace 0 (negro) el componente R
        cv2.imshow('g',g)#Se muestra la imagen unicamente con el componente G
        #Set green and ble Channel to 0
        cv2.namedWindow('r')
        cv2.setMouseCallback('r',mouse)
        r = imagen.copy()
        r[:,:,0] = 0 #Se hace 0 (negro) el componente B
        r[:,:,1] = 0 #Se hace 0 (negro) el componente G
        cv2.imshow('r',r)#Se muestra la imagen unicamente con el componente R
        k = cv2.waitKey(0)
        if k == ord('s'):#Esperar hasta que se presione 's'
            break
    cv2.destroyAllWindows()#Se cierran las ventanas

if __name__=='__main__':
  imagen = cv2.imread("rgb.png")#Se lee la imagen
  
  #Se llama al método encargado de separar la imagen en sus componentes RGB independientemente
  separar(imagen)

