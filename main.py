import cv2 # Se importa opencv
import numpy as np # Se importa numpy como np
from numpy.lib.function_base import copy # Se importa el modulo copy

imagen = cv2.imread("rgb.jpg") # Se lee la imagen

R = imagen[:, :, 2] # Se crea una escala de grises desde el canal R
G = imagen[:, :, 1] # Se crea una escala de grises desde el canal G
B = imagen[:, :, 0] # Se crea una escala de grises desde el canal B

RGB = np.vstack((R, G, B)) # Se concatenan las escalas creadas

# Se muestran las imagenes
cv2.imshow("Imagen", imagen)
cv2.imshow("RGB", RGB)

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran las ventanas

