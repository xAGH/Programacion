# Importación de librerías
from cv2 import cv2
import numpy as np

original = cv2.imread("monedascontorno\img\monedas.jpg") # Recoger imagen
grises = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY) # Imagen a escala de grises.
valorGauss = 3 # Definir el valor de Gauss que será utilizado en el valor de las matrices.
valorKernel = 3 # Definir el valor de Kernel que será utilizado en el valor de las matrices.

# Difuminación de imagen con Gauus, recibe la imagen y una matriz que definirá la cantidad de
# pixeles en el eje x & eje y para hacer su posterior promedio
gauss = cv2.GaussianBlur(grises, (valorGauss, valorGauss),0)
# Eliminación de ruido con Canny, recibe la imagen, el umbral mínimo y el umbral máximo estando
# estos en el rango de 0 a 255
canny = cv2.Canny(gauss, 8, 100)
# Creación de matriz con el valor del kernel que definirá las columnas y filas de la matriz, ademas
# de manejar el resultado como enteros de 8 bits
kernel = np.ones((valorKernel, valorKernel), np.uint8)

# Definición área útil
cierre = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

# Definición de contornos
contornos, jerarquia = cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Conteo de modenas
print(f"Monedas encontradas: {len(contornos)}")

# Dibujo de contornos
cv2.drawContours(original, contornos, -1, (0, 0, 255), 2)

# Mostrar resultado de imagen en grises
cv2.imshow("Imagen", original)
cv2.waitKey(0)