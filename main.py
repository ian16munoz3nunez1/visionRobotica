# Aplicar una operacion de erosion a la imagen 2

import cv2 # Se importa 'opencv'
import numpy as np # Se importa 'numpy' como np

imagen = cv2.imread("imagen_2.png") # Se lee la imagen

kernel = np.ones((5, 5), np.uint8) # Se crea el kernel para el filtro
erosion = cv2.erode(imagen, kernel) # Se aplica el filtro de erosion a la imagen

cv2.imshow("Imagen", imagen) # Se muestra la imagen original
cv2.imshow("Erosion", erosion) # Se muestra la imagen con el filtro de erosion

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

