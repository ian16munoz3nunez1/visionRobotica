import cv2 # Se importa 'opencv'
import numpy as np # Se importa 'numpy' como np
from numpy.lib.function_base import copy # Se importa el modulo copy de 'numpy'

imagen = cv2.imread("imagen.png") # Se lee la imagen

escala = 0.8
imagen = cv2.resize(imagen, None, fx=escala, fy=escala) # Se cambian las dimensiones de la imagen

imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV) # Se convierte la imagen de BGR a HSV

mask = cv2.inRange(imagenHSV, (21, 110, 190), (27, 255, 255)) # Se obtiene la mascara de imagen
maskFloodfill = copy(mask) # Se crea una copia de la mascara para rellenar los pixeles

cv2.floodFill(maskFloodfill, None, (0, 0), 255) # Se rellena la mascara con los pixeles faltantes
maskFloodfillNegativa = cv2.bitwise_not(maskFloodfill) # Se obtiene la negativa de la mascara rellenada

fill = cv2.bitwise_or(mask, maskFloodfillNegativa) # Se rellena la mascara original

# Se muestran las imagenes
cv2.imshow("Imagen", imagen)
cv2.imshow("Mascara", mask)
cv2.imshow("Mascara (Floodfill)", maskFloodfill)
cv2.imshow("Mascara (Floodfill negativa)", maskFloodfillNegativa)
cv2.imshow("Fill", fill)

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

