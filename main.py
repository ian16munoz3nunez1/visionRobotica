import cv2 # Se importa opencv

imagen = cv2.imread("ejercicio5.png") # Se lee la imagen

escala = 0.5
imagen = cv2.resize(imagen, None, fx=escala, fy=escala) # Se escala el tamaño de la imagen

imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV) # Se convierte la imagen de BGR a HSV

mask = cv2.inRange(imagenHSV, (55, 250, 235), (60, 255, 240)) # Se obtiene la mascara de la imagen

cv2.imshow("Imagen", imagen) # Se muestra la imagen original
cv2.imshow("Mascara", mask) # Se muestra la mascara de imagen

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

