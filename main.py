import cv2 # Se importa opencv
import matplotlib.pyplot as plt # Se importa matplotlib como plt

imagen = cv2.imread("imagen.jpg", 0) # Se lee la imagen en escala de grises

imagen = cv2.resize(imagen, None, fx=0.5, fy=0.5) # Se escala el tamaño de la imagen

M, N = imagen.shape[0:2] # Se obtiene el ancho y alto de la imagen

# Se crea el histograma de la imagen con el canal 0, sin mascara, con terciales
# y con un rango de 0 a 256, se usa la función 'flatten' para regresar un arreglo
# sin subarreglos. Todo el arreglo se divide entre el area de la imagen
histograma = cv2.calcHist([imagen], [0], None, [3], [0, 256]).flatten()/(M*N)

plt.bar(range(len(histograma)), histograma) # Se agrega la gráfica del histograma al pyplot
plt.show() # Se muestra el pyplot

# Se muestra la imagen
cv2.imshow("Imagen", imagen)

# Se espera a que el usuario persione le tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

