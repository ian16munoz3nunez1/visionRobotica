import cv2 # Se importa 'opencv'
import numpy as np # Se importa 'numpy' como np

imagen = cv2.imread("imagen.png") # Se lee la imagen

grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) # Se convierte la imagen a escala de grises

bordes = cv2.Canny(grises, 50, 100) # Se obtienen los bordes de la imagen

lines = cv2.HoughLinesP(bordes, 1, np.pi/180, 100, minLineLength=10, maxLineGap=250) # Se obtienen las lineas detectadas en la imagen

for line in lines: # Por cada linea encontrada
    x1, y1, x2, y2 = line[0] # Se obtienen las coordenadas de la linea

    cv2.line(imagen, (x1, y1), (x2, y2), (255, 0, 0), 1) # Se dibuja la linea en la imagen

cv2.imshow("Imagen", imagen) # Se muestra la imagen original con las lineas detectadas
cv2.imshow("Grises", grises) # Se muestra la imagen en escala de grises
cv2.imshow("Bordes", bordes) # Se muestran los bordes de la imagen

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

