import cv2 # Se importa opencv
import numpy as np # Se importa numpy como np
import matplotlib.pyplot as plt # Se importa matplotlib como plt

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

