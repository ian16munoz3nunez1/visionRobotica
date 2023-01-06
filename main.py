import cv2 # Se importa 'opencv'
import numpy as np # Se importa 'numpy' como np

imagen = np.zeros((600, 800, 3), dtype=np.uint8) # Se crea una imagen de 600x800 de 3 canales de tipo uint8

# Se declaran los colores que se usaran
blanco = (255, 255, 255)
morado = (255, 0, 255)

# Se dibujan las figuras en la imagen
cv2.circle(imagen, (650, 450), 90, blanco, -1)
cv2.circle(imagen, (160, 150), 50, blanco, -1)
cv2.circle(imagen, (200, 430), 150, blanco, -1)
cv2.circle(imagen, (400, 100), 40, blanco, -1)
cv2.circle(imagen, (700, 200), 60, blanco, -1)
cv2.circle(imagen, (580, 80), 20, blanco, -1)
cv2.circle(imagen, (470, 250), 80, blanco, -1)

grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) # Se convierte la imagen a escala de grises

# Se obtienen los contornos de las figuras con la imagen en escala de grises
cnts, _ = cv2.findContours(grises, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    x, y, w, h = cv2.boundingRect(c) # Se toman las posiciones y medidas de cada contorno
    cv2.rectangle(imagen, (x, y), (x+w, y+h), morado, 2) # Se dibuja un rectangulo que encierra la figura

cv2.imshow("Imagen", imagen) # Se muestra la imagen

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

