import cv2 # Se importa la opencv --> pip install opencv-contrib-python
import numpy as np # Se importa la libreria numpy como np --> pip install numpy
import matplotlib.pyplot as plt # Se importa la libreria pyplot --> pip install matplotlib

imagen = np.zeros((12, 6), dtype=np.uint8) # Se crea una imagen de 12x6

imagen[1:3, 1:5] = 200 # Se asigna un valor de 200 desde la posicion (1, 1) hasta la (2, 4)

imagen[4:11, 1:5] = 150 # Se asigna un valor de 150 desde la posicion (4, 1) hasta la (10, 4)

plt.imshow(imagen, cmap="gray") # Se agrega la imagen al pyplot

plt.show() # Se muestra el pyplot

