# Aplicar una operacion de dilatacion a la imagen 2

import cv2 # Se importa 'opencv'
import numpy as np # Se importa 'numpy' como np

imagen = cv2.imread("imagen_2.png") # Se lee la imagen

kernel = np.ones((5, 5), np.uint8) # Se crea el kernel para el filtro
dilatacion = cv2.dilate(imagen, kernel) # Se aplica el filtro de dilatacion a la imagen

cv2.imshow("Imagen", imagen) # Se muestra la imagen original
cv2.imshow("Dilatacion", dilatacion) # Se muestra la imagen con el filtro de dilatacion

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

