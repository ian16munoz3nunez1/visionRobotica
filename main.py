import cv2 # Se importa 'opencv'
import numpy as np # Se importa 'numpy' como np
from time import sleep # Se importa el modulo 'sleep' de 'time'
from numpy.lib.function_base import copy # Se importa el modulo 'copy' de 'numpy'

captura = cv2.VideoCapture(0) # Se inicia la captura del video

width = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH)) # Se obtiene el ancho del video
height = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Se obtiene el alto del video
fps = 10 # Se definen los fps para grabar el video
escala = 1 # Se define el valor con el que se quiere escalar el video

fourcc = cv2.VideoWriter_fourcc(*"mp4v") # Se crea el codec para grabar el video
output = cv2.VideoWriter("out.mp4", fourcc, fps, (width, height)) # Se define el archivo de salida para grabar el video

# Ya que solo se quieren grabar 5 segundos de video...
i = 0 # Se crea un iterador
while i < 50: # Ya que los fps son 10, 10*5 = 50
    leido, frame = captura.read() # Se lee el contenido del video

    # Si ya no se puede leer el video, se termina el ciclo
    if not leido:
        break

    # Si se presiona la tecla 'esc' se termina el ciclo
    if cv2.waitKey(1) == 27:
        break

    harris = copy(frame) # Se crea una copia del frame

    grises = cv2.cvtColor(harris, cv2.COLOR_BGR2GRAY) # Se convierte el frame a escala de grises
    grises = np.float32(grises) # Se convierte el tipo de dato de uint8 a float32

    # Se aplica el algoritmo de Harris
    dst = cv2.cornerHarris(grises, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)
    harris[dst > 0.01*dst.max()] = [0, 255, 255]

    output.write(harris) # Se escribe la imagen con el algoritmo de Harris

    # Se cambian las dimensiones de la imagen
    frame = cv2.resize(frame, None, fx=escala, fy=escala)
    harris = cv2.resize(harris, None, fx=escala, fy=escala)

    cv2.imshow("Captura", frame) # Se muestra el video original
    cv2.imshow("Algoritmo de Harris", harris) # Se muestra el video con el algoritmo de Harris

    i += 1 # Incrementa el valor del iterador

captura.release() # Se libera la captura
cv2.destroyAllWindows() # Se cierran todas las ventanas

