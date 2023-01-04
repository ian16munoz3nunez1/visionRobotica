# Usar distintos niveles de saturación para observar la diferencia

import cv2 # Se importa la opencv
import numpy as np # Se importa la libreria numpy como np

h = np.zeros((480, 640), dtype=np.uint8) + 30 # Se asigna el nivel al campo de 'hue' para el color amarillo
v = np.zeros((480, 640), dtype=np.uint8) + 255 # Se asigna el nivel al campo 'value'

s = np.zeros((480, 640), dtype=np.uint8) + 0 # Se asigna el nivel al campo 'saturation'
hsv = cv2.merge((h, s, v)) # Se mezclan los canales 'hue', 'saturation' y 'value'
imagen = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Se convierte el espacio de color de 'HSV' a 'BGR'
cv2.imshow("Imagen 1", imagen) # Se muestra la imagen 1

s = np.zeros((480, 640), dtype=np.uint8) + 50 # Se asigna el nivel al campo 'saturation'
hsv = cv2.merge((h, s, v)) # Se mezclan los canales 'hue', 'saturation' y 'value'
imagen = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Se convierte el espacio de color de 'HSV' a 'BGR'
cv2.imshow("Imagen 2", imagen) # Se muestra la imagen 1

s = np.zeros((480, 640), dtype=np.uint8) + 100 # Se asigna el nivel al campo 'saturation'
hsv = cv2.merge((h, s, v)) # Se mezclan los canales 'hue', 'saturation' y 'value'
imagen = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Se convierte el espacio de color de 'HSV' a 'BGR'
cv2.imshow("Imagen 3", imagen) # Se muestra la imagen 1

s = np.zeros((480, 640), dtype=np.uint8) + 150 # Se asigna el nivel al campo 'saturation'
hsv = cv2.merge((h, s, v)) # Se mezclan los canales 'hue', 'saturation' y 'value'
imagen = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Se convierte el espacio de color de 'HSV' a 'BGR'
cv2.imshow("Imagen 4", imagen) # Se muestra la imagen 1

s = np.zeros((480, 640), dtype=np.uint8) + 200 # Se asigna el nivel al campo 'saturation'
hsv = cv2.merge((h, s, v)) # Se mezclan los canales 'hue', 'saturation' y 'value'
imagen = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Se convierte el espacio de color de 'HSV' a 'BGR'
cv2.imshow("Imagen 5", imagen) # Se muestra la imagen 1

while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()

