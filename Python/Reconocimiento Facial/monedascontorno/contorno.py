#!/usr/local/bin/python
# coding: utf-8

# Importación de cv2
import cv2

imagen = cv2.imread('monedascontorno\img\contorno.jpg')
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_, imagen_umbral = cv2.threshold(grises,150,255, cv2.THRESH_BINARY)
contorno, jerarquia = cv2.findContours(imagen_umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen, contorno, -1, (255, 0, 0), 3)

cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Grises', grises)
cv2.imshow('Imagen Umbral', imagen_umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()