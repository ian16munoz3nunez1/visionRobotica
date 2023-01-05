import cv2 # Se importa opencv

imagen = cv2.imread("spiderman.jpg") # Se lee la imagen

escala = 0.5
imagen = cv2.resize(imagen, None, fx=escala, fy=escala) # Se cambia el tamaño de la imagen

fondo = cv2.imread("matute.jpg") # Se lee el fondo
fondo = cv2.resize(fondo, (imagen.shape[1], imagen.shape[0])) # Se cambia el tamaño del fondo

imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV) # Se convierte la imagen de BGR a HSV
mask = cv2.inRange(imagenHSV, (50, 100, 100), (65, 255, 255)) # Se obtiene la mascara de la imagen
maskNegativa = cv2.bitwise_not(mask) # Se crea una imagen negativa de la mascara

imagenMask = cv2.bitwise_and(imagen, imagen, mask=maskNegativa) # Se aplica la mascara a la imagen
fondoMask = cv2.bitwise_and(fondo, fondo, mask=mask) # Se aplica la mascara al fondo
imagenFondo = cv2.bitwise_or(imagenMask, fondoMask) # Se unen la imagen y el fondo

# Se muestran las imagenes
cv2.imshow("Imagen", imagen)
cv2.imshow("Fondo", fondo)
cv2.imshow("Mascara", mask)
cv2.imshow("Negativa de la mascara", maskNegativa)
cv2.imshow("Mascara aplicada a la imagen", imagenMask)
cv2.imshow("Mascara aplicada al fondo", fondoMask)
cv2.imshow("Imagen y fondo", imagenFondo)

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

