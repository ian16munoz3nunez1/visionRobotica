import cv2 # Se importa opencv
import matplotlib.pyplot as plt

imagen = cv2.imread("imagen.jpg") # Se lee la imagen
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) # Se convierte la imagen a escala de grises
grisesM, grisesN = grises.shape[0:2] # Se obtiene el ancho y alto de la imagen
histograma = cv2.calcHist([grises], [0], None, [100], [0, 256]).flatten()/(grisesM*grisesN) # Se calcula el histograma de la imagen

imagen2 = cv2.resize(imagen, None, fx=0.5, fy=0.5) # Se cambia el tamaño de la imagen
grises2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY) # Se convierte a escala de grises
grises2M, grises2N = grises2.shape[0:2] # Se obtienen el ancho y alto de la imagen
histograma2 = cv2.calcHist([grises2], [0], None, [100], [0, 256]).flatten()/(grises2M*grises2N) # Se calcula el histograma de la imagen

imagen3 = cv2.resize(imagen, None, fx=0.25, fy=0.25) # Se cambia el tamaño de la imagen
grises3 = cv2.cvtColor(imagen3, cv2.COLOR_BGR2GRAY) # Se convierte a escala de grises
grises3M, grises3N = grises3.shape[0:2] # Se obtienen el ancho y alto de la imagen
histograma3 = cv2.calcHist([grises3], [0], None, [100], [0, 256]).flatten()/(grises3M*grises3N) # Se calcula el histograma de la imagen

# Se grafica el histograma de la imagen original
plt.figure(1)
plt.subplot(311)
plt.bar(range(len(histograma)), histograma)
plt.title("Imagen original")

# Se grafica el histograma de la imagen con escala de 0.5
plt.subplot(312)
plt.bar(range(len(histograma2)), histograma2)
plt.title("Imagen 1/2")

# Se grafica el histograma de la imagen con escala de 0.25
plt.subplot(313)
plt.bar(range(len(histograma3)), histograma3)
plt.title("Imagen 1/4")


plt.figure(2)
plt.subplot(131)
plt.bar(range(len(histograma)), histograma)
plt.title("Imagen original")

# Se grafica el histograma de la imagen con escala de 0.5
plt.subplot(132)
plt.bar(range(len(histograma2)), histograma2)
plt.title("Imagen 1/2")

# Se grafica el histograma de la imagen con escala de 0.25
plt.subplot(133)
plt.bar(range(len(histograma3)), histograma3)
plt.title("Imagen 1/4")

plt.show() # Se muestra el pyplot

# Se muestran las imagenes
cv2.imshow("Imagen original", imagen)
cv2.imshow("Imagen 1/2", imagen2)
cv2.imshow("Imagen 1/4", imagen3)

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

