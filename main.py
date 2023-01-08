# Aplicar una operacion de closing a la imagen 6

import cv2 # Se importa 'opencv'
import numpy as np # Se importa 'numpy' como np

imagen = cv2.imread("imagen_6.png") # Se lee la imagen

kernel = np.ones((3, 3), np.uint8) # Se crea el kernel para el filtro
closing = cv2.morphologyEx(imagen, cv2.MORPH_CLOSE, kernel) # Se aplica el filtro de closing a la imagen

cv2.imshow("Imagen", imagen) # Se muestra la imagen original
cv2.imshow("Closing", closing) # Se muestra la imagen con el filtro de closing

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

