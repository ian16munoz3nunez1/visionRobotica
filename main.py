import cv2 # Se importa 'opencv'
import numpy as np # Se importa 'numpy' como np

imagen = cv2.imread("rubik.jpg") # Se lee la imagen

escala = 0.3
imagen = cv2.resize(imagen, None, fx=escala, fy=escala) # Se cambian las dimensiones de la imagen

kernel = np.array(([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
]), dtype=np.float32) # Se obtiene el kernel para el filtro de la imagen

filtro = cv2.filter2D(imagen, -1, kernel) # Se aplica el filtro a la imagen

# Se muestran las imagenes
cv2.imshow("Imagen", imagen)
cv2.imshow("Filtro", filtro)

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

