import cv2 # Se importa la opencv --> pip install opencv-contrib-python
import numpy as np # Se importa la libreria numpy como np --> pip install numpy
import matplotlib.pyplot as plt # Se importa la libreria pyplot --> pip install matplotlib

imagen = np.zeros((9, 8, 3), dtype=np.uint8) # Se crea una imagen de 9x8x3

# Se asigna el color cian al pixel en la posicion (1, 1)
imagen[1, 1, 0] = 255
imagen[1, 1, 1] = 255

# Se asigna el color magenta al pixel en la posicion (3, 6)
imagen[3, 6, 0] = 255
imagen[3, 6, 2] = 255

# Se asigna el color amarillo al pixel en la posicion (7, 3)
imagen[7, 3, 1] = 255
imagen[7, 3, 2] = 255

# Se cambia el formato de la imagen de BGR a RGB para mostrarlo en el pyplot
rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

plt.imshow(rgb) # Se agrega la imagen al pyplot

plt.show() # Se muestra el pyplot

