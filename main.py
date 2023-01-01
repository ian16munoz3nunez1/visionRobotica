import cv2 # Se importa la opencv --> pip install opencv-contrib-python
import numpy as np # Se importa la libreria numpy como np --> pip install numpy
import matplotlib.pyplot as plt # Se importa la libreria pyplot --> pip install matplotlib

imagen = np.zeros((8, 15), dtype=np.uint8) # Se crea una imagen de 8x15

imagen[2, 3] = 255 # Se asigna un valor de 255 al pixel en la posicion (2, 3)

imagen[2, 11] = 170 # Se asigna un valor de 170 al pixel en la posicion (2, 11)

imagen[5, 7] = 85 # Se asigna el balor de 85 al pixel en la posicion (5, 7)

plt.imshow(imagen, cmap="gray") # Se agrega la imagen al pyplot

plt.show() # Se muestra el pyplot

