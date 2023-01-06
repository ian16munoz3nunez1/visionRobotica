import cv2 # Se importa 'opencv'
from numpy.lib.function_base import copy # Se importa el modulo 'copy' de la libreria 'numpy'
from etiquetado import etiquetas # Se importa la funcion 'etiquetas' del archivo 'etiquetado'

imagen = cv2.imread("imagen.png") # Se lee la imagen

escala = 0.6
imagen = cv2.resize(imagen, None, fx=escala, fy=escala) # Se cambian las dimensiones de la imagen

imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV) # Se convierte la imagen de BGR a HSV

mask = cv2.inRange(imagenHSV, (2, 135, 190), (15, 255, 255)) # Se obtiene la mascara de la imagen
maskFloodfill = copy(mask) # Se crea una copia de la mascara para rellenar los pixeles

cv2.floodFill(maskFloodfill, None, (0, 0), 255) # Se obtienen los pixeles a rellenar
maskFloodfillNegativa = cv2.bitwise_not(maskFloodfill) # Se obtiene la negativa de los pixeles a rellenar

fill = cv2.bitwise_or(mask, maskFloodfillNegativa) # Se rellena la mascara original

# Se muestran las imagenes
cv2.imshow("Imagen", imagen)
cv2.imshow("Fill", fill)

_, n = etiquetas(fill, 1) # Se obtiene el numero de objetos contados en la imagen
print(f"Numero de objetos: {n}")

# Se muestran todas las etiquetas encontradas por el programa
for i in range(n):
    etiqueta, _ = etiquetas(fill, i+1)
    cv2.imshow(f"Etiqueta_{i+1}", etiqueta)

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

