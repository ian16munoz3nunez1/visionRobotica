# Crear una imagen HSV por cada color que se encuentra en la imagen 'figuras.png'
# Se pueden usar los programas:
# gpick - Linux - sudo apt install gpick
# JustColorPicker - Windows - https://annystudio.com/software/colorpicker/#download
# Para detectar el color de las figuras

import cv2 # Se importa la opencv
import numpy as np # Se importa la libreria numpy como np

# Se crean los campos 'hue', 'saturation' y 'value' para la primer imagen
h = np.zeros((400, 400), dtype=np.uint8) + 29
s = np.zeros((400, 400), dtype=np.uint8) + 255
v = np.zeros((400, 400), dtype=np.uint8) + 255

hsv = cv2.merge((h, s, v)) # Se mezclan los campos HSV
imagen = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Se convierte la imagen de HSV a BGR
cv2.imshow("Imagen 1", imagen) # Se muestra la primer imagen

# Se crean los campos 'hue', 'saturation' y 'value' para la segunda imagen
h = np.zeros((400, 400), dtype=np.uint8) + 169
s = np.zeros((400, 400), dtype=np.uint8) + 237
v = np.zeros((400, 400), dtype=np.uint8) + 237

hsv = cv2.merge((h, s, v)) # Se mezclan los campos HSV
imagen = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Se convierte la imagen de HSV a BGR
cv2.imshow("Imagen 2", imagen) # Se muestra la segunda imagen

# Se crean los campos 'hue', 'saturation' y 'value' para la tercer imagen
h = np.zeros((400, 400), dtype=np.uint8) + 42
s = np.zeros((400, 400), dtype=np.uint8) + 156
v = np.zeros((400, 400), dtype=np.uint8) + 189

hsv = cv2.merge((h, s, v)) # Se mezclan los campos HSV
imagen = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Se convierte la imagen de HSV a BGR
cv2.imshow("Imagen 3", imagen) # Se muestra la tercer imagen

# Se crean los campos 'hue', 'saturation' y 'value' para la cuarta imagen
h = np.zeros((400, 400), dtype=np.uint8) + 13
s = np.zeros((400, 400), dtype=np.uint8) + 201
v = np.zeros((400, 400), dtype=np.uint8) + 240

hsv = cv2.merge((h, s, v)) # Se mezclan los campos HSV
imagen = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Se convierte la imagen de HSV a BGR
cv2.imshow("Imagen 4", imagen) # Se muestra la cuarta imagen

while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()

