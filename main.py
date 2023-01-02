import cv2 # Se importa opencv
import matplotlib.pyplot as plt # Se importa matplotlib como plt

imagen = cv2.imread("imagen.jpg") # Se lee la imagen

imagen = cv2.resize(imagen, None, fx=0.25, fy=0.25) # Se escala la imagen a 0.25
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) # Se convierte la imagen a escala de grises
grisesM, grisesN = grises.shape[0:2] # Se obtienen el ancho y alto de la imagen
histograma = cv2.calcHist([grises], [0], None, [100], [0, 256]).flatten()/(grisesM*grisesN) # Se calcula el histograma de la imagen


b, g, r = cv2.split(imagen) # Se separan los canales de la imagen

r = cv2.multiply(r, 1.5) # Se multiplica el canal R por 1.5
r = cv2.add(r, 50) # Se suma 50 al canal R
g = cv2.multiply(g, 1.5) # Se multiplica el canal G por 1.5
g = cv2.add(g, 50) # Se suma 50 al canal G
b = cv2.multiply(b, 1.5) # Se multiplica el canal B por 1.5
b = cv2.add(b, 50) # Se suma 50 al canal B

imagenRGB = cv2.merge((b, g, r)) # Se combinan los canales
grisesRGB = cv2.cvtColor(imagenRGB, cv2.COLOR_BGR2GRAY) # Se convierte la imagen a escala de grises
grisesRGB_m, grisesRGB_n = grisesRGB.shape[0:2] # Se obtienen el ancho y alto de la imagen
histogramaRGB = cv2.calcHist([grisesRGB], [0], None, [100], [0, 256]).flatten()/(grisesRGB_m*grisesRGB_n) # Se calcula el histograma de la imagen


b, g, r = cv2.split(imagen) # Se separan los canales de la imagen

r = cv2.equalizeHist(r) # Se ecualiza el canal R
g = cv2.equalizeHist(g) # Se ecualiza el canal G
b = cv2.equalizeHist(b) # Se ecualiza el canal B

imagenEqual = cv2.merge((b, g, r)) # Se combinan los canales
grisesEqual = cv2.cvtColor(imagenEqual, cv2.COLOR_BGR2GRAY) # Se convierte la imagen a escala de grises
grisesEqualM, grisesEqualN = grisesEqual.shape[0:2] # Se obtienen el ancho y alto de la imagen
histogramaEqual = cv2.calcHist([grisesEqual], [0], None, [100], [0, 256]).flatten()/(grisesEqualM*grisesEqualN) # Se calcula el histograma de la imagen


plt.figure(1)
# Se grafica el histograma de la imagen original
plt.subplot(311)
plt.bar(range(len(histograma)), histograma)
plt.title("Imagen original")

# Se grafica el histograma de la imagen con mas brillo
plt.subplot(312)
plt.bar(range(len(histogramaRGB)), histogramaRGB)
plt.title("Imagen RGB")

# Se grafica el histograma de la imagen ecualizada
plt.subplot(313)
plt.bar(range(len(histogramaEqual)), histogramaEqual)
plt.title("Imagen ecualizada")


plt.figure(2)
# Se grafica el histograma de la imagen original
plt.subplot(131)
plt.bar(range(len(histograma)), histograma)
plt.title("Imagen original")

# Se grafica el histograma de la imagen con mas brillo
plt.subplot(132)
plt.bar(range(len(histogramaRGB)), histogramaRGB)
plt.title("Imagen RGB")

# Se grafica el histograma de la imagen ecualizada
plt.subplot(133)
plt.bar(range(len(histogramaEqual)), histogramaEqual)
plt.title("Imagen ecualizada")

plt.show() # Se muestra el pyplot

# Se muestran las imagenes
cv2.imshow("Imagen original", imagen)
cv2.imshow("Imagen RGB", imagenRGB)
cv2.imshow("Imagen ecualizada", imagenEqual)

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

