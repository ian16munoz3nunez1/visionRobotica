import cv2 # Se importa opencv

# Se leen las imagenes
sonic = cv2.imread("sonic.jpg")
gato = cv2.imread("gato.jpg")
explo = cv2.imread("explo.jpg")

sonic = cv2.resize(sonic, None, fx=0.3, fy=0.3) # Se escala la imagen
gato = cv2.resize(gato, None, fx=0.45, fy=0.45) # Se escala la imagen
explo = cv2.resize(explo, None, fx=0.2, fy=0.2) # Se escala la imagen

sonicHSV = cv2.cvtColor(sonic, cv2.COLOR_BGR2HSV) # Se convierte la imagen de BGR a HSV
gatoHSV = cv2.cvtColor(gato, cv2.COLOR_BGR2HSV) # Se convierte la imagen de BGR a HSV
exploHSV = cv2.cvtColor(explo, cv2.COLOR_BGR2HSV) # Se convierte la imagen de BGR a HSV

sonicMask = cv2.inRange(sonicHSV, (55, 240, 240), (65, 255, 255)) # Se obtiene la mascara de la imagen
gatoMask = cv2.inRange(gatoHSV, (55, 240, 240), (65, 255, 255)) # Se obtiene la mascara de la imagen
exploMask = cv2.inRange(exploHSV, (55, 160, 160), (65, 245, 255)) # Se obtiene la mascara de la imagen

cv2.imshow("Sonic", sonic) # Se muestra la imagen original
cv2.imshow("Sonic (Mascara)", sonicMask) # Se muestra la mascara de la imagen

cv2.imshow("Gato", gato) # Se muestra la imagen original
cv2.imshow("Gato (Mascara)", gatoMask) # Se muestra la mascara de la imagen

cv2.imshow("Explosion", explo) # Se muestra la mascara original
cv2.imshow("Explosion (Mascara)", exploMask) # Se muestra la mascara de la imagen

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

