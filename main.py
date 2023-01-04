# Generar imagenes de distinto color usando el modelo HSV
# 1. Generar una imagen de color amarillo
# 2. Generar una imagen de color naranja
# 3. Generar una imagen de color cian
# 4. Generar una imagen de color magenta
# 5. Generar una imagen de color azul

import cv2 # Se importa la opencv
import numpy as np # Se importa la libreria numpy como np

s = np.zeros((480, 640), dtype=np.uint8) + 255 # Se asigna el nivel al campo 'saturation'
v = np.zeros((480, 640), dtype=np.uint8) + 255 # Se asigna el nivel al campo 'value'

h = np.zeros((480, 640), dtype=np.uint8) + 30 # Se asigna el nivel al campo de 'hue' para el color amarillo
hsv = cv2.merge((h, s, v)) # Se mezclan los canales 'hue', 'saturation' y 'value'
imagen = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Se convierte el espacio de color de 'HSV' a 'BGR'
cv2.imshow("Imagen 1", imagen) # Se muestra la imagen 1

h = np.zeros((480, 640), dtype=np.uint8) + 15 # Se asigna el nivel al campo de 'hue' para el color naranja
hsv = cv2.merge((h, s, v)) # Se mezclan los canales 'hue', 'saturation' y 'value'
imagen = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Se convierte el espacio de color de 'HSV' a 'BGR'
cv2.imshow("Imagen 2", imagen) # Se muestra la imagen 1

h = np.zeros((480, 640), dtype=np.uint8) + 90 # Se asigna el nivel al campo de 'hue' para el color cian
hsv = cv2.merge((h, s, v)) # Se mezclan los canales 'hue', 'saturation' y 'value'
imagen = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Se convierte el espacio de color de 'HSV' a 'BGR'
cv2.imshow("Imagen 3", imagen) # Se muestra la imagen 1

h = np.zeros((480, 640), dtype=np.uint8) + 135 # Se asigna el nivel al campo de 'hue' para el color magenta
hsv = cv2.merge((h, s, v)) # Se mezclan los canales 'hue', 'saturation' y 'value'
imagen = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Se convierte el espacio de color de 'HSV' a 'BGR'
cv2.imshow("Imagen 4", imagen) # Se muestra la imagen 1

h = np.zeros((480, 640), dtype=np.uint8) + 120 # Se asigna el nivel al campo de 'hue' para el color azul
hsv = cv2.merge((h, s, v)) # Se mezclan los canales 'hue', 'saturation' y 'value'
imagen = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Se convierte el espacio de color de 'HSV' a 'BGR'
cv2.imshow("Imagen 5", imagen) # Se muestra la imagen 1

while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()

