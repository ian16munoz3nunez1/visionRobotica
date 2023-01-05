import cv2 # Se importa opencv

imagen = cv2.imread("ironman.jpg") # Se lee la imagen

escala = 0.5
imagen = cv2.resize(imagen, None, fx=escala, fy=escala) # Se escala el tamaño de la imagen

imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV) # Se convierte la imagen de BGR a HSV

mask = cv2.inRange(imagenHSV, (50, 100, 100), (65, 255, 255)) # Se obtiene la mascara de la imagen

maskNegativa = cv2.bitwise_not(mask) # Se crea una imagen negativa de la mascara

imagenMask = cv2.bitwise_and(imagen, imagen, mask=maskNegativa) # Se aplica la mascara a la imagen

# Se muestran las imagenes
cv2.imshow("Imagen original", imagen)
cv2.imshow("Mascara", mask)
cv2.imshow("Negativa de la mascara", maskNegativa)
cv2.imshow("Mascara aplicada a la imagen", imagenMask)

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

