import cv2 # Se importa 'opencv'
import numpy as np # Se importa 'numpy' como np

imagen = np.zeros((600, 800, 3), dtype=np.uint8) # Se crea una imagen de 600x800 de 3 canales de tipo uint8

# Se declaran los colores que se usaran
blanco = (255, 255, 255)
morado = (255, 0, 255)

# Se dibujan las figuras en la imagen
cv2.circle(imagen, (650, 450), 90, blanco, -1)
cv2.circle(imagen, (160, 220), 50, blanco, -1)
cv2.circle(imagen, (250, 430), 150, blanco, -1)
cv2.rectangle(imagen, (50, 50), (100, 100), blanco, -1)
cv2.rectangle(imagen, (300, 40), (750, 250), blanco, -1)
cv2.rectangle(imagen, (440, 300), (540, 400), blanco, -1)

grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) # Se convierte la imagen a escala de grises

# Se obtienen los contornos de las figuras con la imagen en escala de grises
cnts, _ = cv2.findContours(grises, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen, cnts, -1, morado, 2) # Se dibujan los contornos en la imagen original

cv2.imshow("Imagen", imagen) # Se muestra la imagen

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

