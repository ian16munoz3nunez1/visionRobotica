# Parametros de la funcion putText():
# 1: Imagen en la que se imprime el mensaje
# 2: Mensaje a mostrar
# 3: Coordenadas en las que se imprime el mensaje
# 4: Tipo de letra para el mensaje
# 5: Tamaño del mensaje
# 6: Color del mensaje
# 7: Grosor de las letras del mensaje

import cv2 # Se importa 'opencv'
import numpy as np # Se importa 'numpy' como np
import matplotlib.pyplot as plt # Se importa pyplot como plt

imagen = cv2.imread("sobreexpuesta.jpg") # Se lee la imagen

escala = 0.5
imagen = cv2.resize(imagen, None, fx=escala, fy=escala) # Se cambian las dimensiones de la imagen

grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) # Se convierte la imagen a escala de grises

alto, ancho = imagen.shape[0:2] # Se obtienen el alto y ancho de la imagen

histograma = cv2.calcHist([grises], [0], None, [5], [0, 256]).flatten()/(alto*ancho) # Se calcula el histograma de la imagen

maximo = np.argmax(histograma) # Se obtiene el valor maximo del histograma

if maximo == 4 and histograma[4] > 0.3:
    b, g, r = cv2.split(imagen) # Se separan los canales de la imagen

    # Se ecualizan los canales de la imagen
    r = cv2.equalizeHist(r)
    g = cv2.equalizeHist(g)
    b = cv2.equalizeHist(b)

    equalize = cv2.merge((b, g, r)) # Se mezclan los canales de la imagen

    cv2.imshow("Imagen", imagen) # Se muestra la imagen original

    # Se imprime en la imagen el mensaje 'Sobreexpuesta'
    cv2.putText(equalize, "Sobreexpuesta", (40, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)
    cv2.imshow("Imagen ecualizada", equalize) # Se muestra la imagen ecualizada

elif maximo == 0 and histograma[0] > 0.3:
    b, g, r = cv2.split(imagen) # Se separan los canales de la imagen

    # Se ecualizan los canales de la imagen
    r = cv2.equalizeHist(r)
    g = cv2.equalizeHist(g)
    b = cv2.equalizeHist(b)

    equalize = cv2.merge((b, g, r)) # Se mezclan los canales de la imagen

    cv2.imshow("Imagen", imagen) # Se muestra la imagen original

    # Se imprime en la imagen el mensaje 'Subexpuesta'
    cv2.putText(equalize, "Subexpuesta", (40, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)
    cv2.imshow("Imagen ecualizada", equalize) # Se muestra la imagen ecualizada

else:
    # Se imprime en la imagen el mensaje 'Buena exposicion'
    cv2.putText(imagen, "Buena exposicion", (40, 40), cv2.FONT_HERSHEY_COMPELX, 1, (50, 50, 255), 2)
    cv2.imshow("Imagen", imagen) # Se muestra la imagen original

# Se espera a que el usuario presione la tecla 'esc'
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows() # Se cierran todas las ventanas

plt.bar(range(len(histograma)), histograma) # Se grafica el histograma en el pyplot
plt.show() # Se muestra el pyplot

