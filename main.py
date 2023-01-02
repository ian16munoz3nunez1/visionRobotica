import cv2 # Se importa opencv
import numpy as np # Se importa numpy como np

imagen = cv2.imread("rgb.jpg") # Se lee la imagen

grises = cv2.rotate(imagen, cv2.ROTATE_90_CLOCKWISE) # Se rota la imagen original 90 grados
grises = cv2.cvtColor(grises, cv2.COLOR_BGR2GRAY) # Se convierte la imagen a escala de grises

negativa = 255 - grises # Se obtiene la negativa de la imagen en escala de grises

# Se muestran las imagenes
cv2.imshow("Imagen", imagen)
cv2.imshow("Grises", grises)
cv2.imshow("Negativa", negativa)

# Se espera a que el usuario pulse la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

