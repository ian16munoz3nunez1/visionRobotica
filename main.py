import cv2 # Se importa la opencv --> pip install opencv-contrib-python
import numpy as np # Se importa la libreria numpy como np --> pip install numpy
import matplotlib.pyplot as plt # Se importa la libreria pyplot --> pip install matplotlib

imagen = np.zeros((16, 8, 3), dtype=np.uint8) # Se crea una imagen de 16x8x3

# Se asigna el color (125, 225, 0) desde la posicion (1, 1) a la (2, 6)
imagen[1:3, 1:7, 0] = 125
imagen[1:3, 1:7, 1] = 225

# Se asigna el color (100, 0, 250) desde la posicion (4, 2) a la (10, 5)
imagen[4:11, 2:6, 0] = 100
imagen[4:11, 2:6, 2] = 250

# Se asigna el color (0, 200, 190) desde la posicion (12, 1) a la (14, 6)
imagen[12:15, 1:7, 1] = 200
imagen[12:15, 1:7, 2] = 190

# Se cambia el formato de la imagen de BGR a RGB para mostrarlo en el pyplot
rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

plt.imshow(rgb) # Se agrega la imagen al pyplot

plt.show() # Se muestra el pyplot

