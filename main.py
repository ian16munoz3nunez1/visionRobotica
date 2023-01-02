import cv2 # Se importa opencv
import numpy as np # Se importa numpy como np
import matplotlib.pyplot as plt # Se importa matplotlib como plt

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

R = imagen[:, :, 2] # Se crea una escala de grises desde el canal R
G = imagen[:, :, 1] # Se crea una escala de grises desde el canal G
B = imagen[:, :, 0] # Se crea una escala de grises desde el canal B

# Metodo por promedio
promedio = R*0.33 + G*0.33 + B*0.33
promedio = promedio.astype(np.uint8)
# Metodo BT.601
bt_601 = R*0.299 + G*0.587 + B*0.114
bt_601 = bt_601.astype(np.uint8)
# Metodo BT.709
bt_709 = R*0.2126 + G*0.7152 + B*0.0722
bt_709 = bt_709.astype(np.uint8)

RGB = np.vstack((R, G, B)) # Se concatenan las matrices RGB
grises = np.vstack((promedio, bt_601, bt_709)) # Se concatenan los ponderaciones
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB) # Se cambia el formato de BGR a RGB

# Se muestra la imagen original
plt.figure(1)
plt.imshow(imagen)
plt.title("Imagen")

# Se muestran los filtros RGB de la imagen
plt.figure(2)
plt.imshow(RGB, cmap="gray")
plt.title("RGB")

# Se muestran las ponderaciones de la imagen
plt.figure(3)
plt.imshow(grises, cmap="gray")
plt.title("Grises")

plt.show()

