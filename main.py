import cv2 # Se importa opencv

imagen = cv2.imread("ejercicio1.png") # Se lee la imagen

escala = 0.5
imagen = cv2.resize(imagen, None, fx=escala, fy=escala) # Se escala el tamaño de la imagen

imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV) # Se convierte la imagen de BGR a HSV

# Se obtiene la imagen de la mascara
# Para seleccionar el color se envian como parametros la imagen
# El valor minimo del color a seleccionar
# Y el valor maximo del color a seleccionar
mask = cv2.inRange(imagenHSV, (145, 135, 160), (155, 145, 165))

cv2.imshow("Imagen", imagen) # Se muestra la imagen original
cv2.imshow("Mascara", mask) # Se muestra la mascara de imagen

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

