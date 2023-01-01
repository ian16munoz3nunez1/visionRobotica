import cv2 # Se importa opencv
import numpy as np # Se importa numpy como np
from numpy.lib.function_base import copy # Se importa el modulo copy

imagen = cv2.imread("rgb.jpg") # Se lee la imagen

# Se crea una copia de la imagen para aplicar los filtros
r = copy(imagen)
g = copy(imagen)
b = copy(imagen)

# Se asigna un valor de 0 a los canales B y G
r[:, :, 0] = 0
r[:, :, 1] = 0

# Se asigna un valor de 0 a los canales B y R
g[:, :, 0] = 0
g[:, :, 2] = 0

# Se asigna un valor de 0 a los canales G y R
b[:, :, 1] = 0
b[:, :, 2] = 0

filtros = np.vstack((r, g, b)) # Se concatenan los filtros aplicados

# Se muestran las imagenes
cv2.imshow("Imagen", imagen)
cv2.imshow("Filtros", filtros)

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran las ventanas

