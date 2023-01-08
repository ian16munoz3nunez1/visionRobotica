# Aplicar una operacion de opening a la imagen 4

import cv2 # Se importa 'opencv'
import numpy as np # Se importa 'numpy' como np

imagen = cv2.imread("imagen_4.png") # Se lee la imagen

kernel = np.ones((3, 3), np.uint8) # Se crea el kernel para el filtro
opening = cv2.morphologyEx(imagen, cv2.MORPH_OPEN, kernel) # Se aplica el filtro de opening a la imagen

cv2.imshow("Imagen", imagen) # Se muestra la imagen original
cv2.imshow("Opening", opening) # Se muestra la imagen con el filtro de opening

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

