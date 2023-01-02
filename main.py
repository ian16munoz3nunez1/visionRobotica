import cv2 # Se importa opencv
import numpy as np # Se importa numpy como np

imagen = cv2.imread("rgb.jpg") # Se lee la imagen

negativa = 255 - imagen # Se obtiene la negativa de la imagen

# Se muestran las imagenes
cv2.imshow("Imagen", imagen)
cv2.imshow("Negativa", negativa)

# Se espera a que el usuario pulse la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

