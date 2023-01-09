import cv2 # Se importa 'opencv'
import numpy as np # Se importa 'numpy' como np

imagen = cv2.imread("imagen.png") # Se lee la imagen

grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) # Se convierte la imagen a escala de grises

_, binary = cv2.threshold(grises, 90, 255, cv2.THRESH_BINARY) # Se convierte la imagen a formato binario

# Se obtienen los circulos detectados en la imagen
circles = cv2.HoughCircles(binary, cv2.HOUGH_GRADIENT, 1, 20, param1=10, param2=16, minRadius=1, maxRadius=130)

# Si se encontraron circulos en la imagen
if circles is not None:
    circles = np.uint16(np.around(circles)) # Se cambia el tipo de dato a uint16

    for i in circles[0, :]:
        cv2.circle(imagen, (i[0], i[1]), i[2], (0, 255, 255), 2) # Se dibuja un circulo del mismo tamaño del original
        cv2.circle(imagen, (i[0], i[1]), 2, (0, 0, 255), 3) # Se dibuja un circulo pequeño en el centro del circulo

cv2.imshow("Imagen", imagen) # Se muestra la imagen original
cv2.imshow("Grises", grises) # Se muestra la imagen en escala de grises
cv2.imshow("Binaria", binary) # Se muestra la imagen en formato binario

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

