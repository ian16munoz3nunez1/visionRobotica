import cv2 # Se importa opencv
import numpy as np # Se importa numpy como np

imagen = cv2.imread("rgb.jpg") # Se lee la imagen

R = imagen[:, :, 2] # Se crea una escala de grises desde el canal R
G = imagen[:, :, 1] # Se crea una escala de grises desde el canal G
B = imagen[:, :, 0] # Se crea una escala de grises desde el canal B

# Se crea un filtro para una escala de grises con el promedio de los canales
promedio = R*0.33 + G*0.33 + B*0.33
promedio = promedio.astype(np.uint8) # Se convierte el promedio a uint8

# Se muestran las imagenes
cv2.imshow("Imagen", imagen)
cv2.imshow("Promedio", promedio)

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran las ventanas

