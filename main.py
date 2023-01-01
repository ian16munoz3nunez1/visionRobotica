import cv2 # Se importa opencv
import numpy as np # Se importa numpy como np

imagen = cv2.imread("rgb.jpg") # Se lee la imagen

R = imagen[:, :, 2] # Se crea una escala de grises desde el canal R
G = imagen[:, :, 1] # Se crea una escala de grises desde el canal G
B = imagen[:, :, 0] # Se crea una escala de grises desde el canal B

# Se crea un filtro para una escala de grises con el metodo BT.601
bt_601 = R*0.299 + G*0.587 + B*0.114
bt_601 = bt_601.astype(np.uint8) # Se convierte el BT.601 a uint8

# Se muestran las imagenes
cv2.imshow("Imagen", imagen)
cv2.imshow("BT.601", bt_601)

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran las ventanas

