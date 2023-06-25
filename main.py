# Ian Mu;oz Nu;ez

import cv2 as cv
import numpy as np
import serial
from time import sleep

captura = cv.VideoCapture(2) # Conexion con la camara 0/2

kernel = np.ones((9, 9), dtype=np.uint8) # Kernel usado para la erosion
f = np.ones((11, 11), dtype=np.float32)*1/121 # Kernel para aplicar un filtro de desenfoque al video con ruido

uno = serial.Serial('/dev/ttyACM0', 9600, write_timeout=10) # Conexion serial con Arduino
sleep(2) # Espera de 2 segundos para realizar la conexion serial correctamente

angleY = chr(90) # Inicializacion del angulo 'y' en 90 grados
angleX = chr(90) # Inicializacion del angulo 'x' en 90 grados
minAngle = 45 # Angulo minimo al que deben girar los motores
maxAngle = 135 # Angulo maximo al que deben girar los motores

while True:
    leido, video = captura.read() # Lectura de la camara

    if not leido: # Si hay un error con la lectura se termina el ciclo
        break

    if cv.waitKey(1) == 27: # Si se presiona 'esc' se termina el ciclo
        break

    video = cv.resize(video, (180, 180)) # Redimension del video
    video = cv.flip(video, 0) # Voltear el video en el eje 'x'
    m, n = video.shape[0:2] # Dimensiones del video

    noiseMatrix = np.random.normal(-0.5, 0.5, video.size) # Matriz de numeros aleatorios
    noiseMatrix = noiseMatrix.reshape(video.shape[0], video.shape[1], video.shape[2]).astype('uint8') # Redimension de la matriz
    videoNoise = cv.add(video, noiseMatrix) # Aplicacion del ruido al video
    videoFilter = cv.filter2D(videoNoise, -1, f) # Filtro de desenfoque para disminuir el ruido

    hsv = cv.cvtColor(videoFilter, cv.COLOR_BGR2HSV) # Espacio de color de BGR a HSV
    mask = cv.inRange(hsv, (40, 20, 20), (80, 250, 250)) # Mascara de color
    mask = cv.normalize(mask.astype(float), None, 0.0, 1.0, cv.NORM_MINMAX) # Normalizacion de 0 a 1
    mask = cv.erode(mask, kernel) # Aplicacion de la erosion

    posy, posx = np.where(mask==1) # Posiciones de los 1's
    try:
        cy = int(np.sum(posy)/np.sum(mask)) # Posicion del centroide en 'y'
        cx = int(np.sum(posx)/np.sum(mask)) # Posicion del centroide en 'x'
    except:
        cy = int(m/2) # Posicion del centroide en 'y'
        cx = int(n/2) # Posicion del centroide en 'x'
    cv.circle(videoFilter, (cx, cy), 5, (0, 255, 0), -1) # Circulo del centroide en el video

    e_y = -((m/2)-cy) # Error en 'y'
    e_x = -((n/2)-cx) # Error en 'x'

    if abs(e_y) > 10: # Si el error de 'y' es mayor a 10
        angleY = ord(angleY) # Convertir 'angleY' de chr a int
        angleY = angleY + int(e_y*0.05) # Accion de control para el angulo en 'y'
        angleY = max(minAngle, angleY) # Cota minima del angulo en 'y'
        angleY = min(maxAngle, angleY) # Cota maxima del angulo en 'y'
        angleY = chr(angleY) # Convertir 'angleY' de int a chr

    if abs(e_x) > 10: # Si el error de 'x' es mayor a 10
        angleX = ord(angleX) # Convertir 'angleX' de chr a int
        angleX = angleX + int(e_x*0.05) # Accion de control para el angulo en 'x'
        angleX = max(minAngle, angleX) # Cota minima del angulo en 'x'
        angleX = min(maxAngle, angleX) # Cota maxima del angulo en 'x'
        angleX = chr(angleX) # Convertir 'angleX' de int a chr

    uno.write(f'{angleX}'.encode()) # Se envia el angulo 'x' al Arduino
    uno.write(f'{angleY}'.encode()) # Se envia el angulo 'y' al Arduino

    cv.imshow("Video", video) # Se muestra el video
    cv.imshow("Mask", mask) # Se muestra la mascara
    cv.imshow("VideoNoise", videoNoise) # Se muestra el video con ruido
    cv.imshow("VideoFilter", videoFilter) # Se muestra el video con filtro aplicado

uno.close() # Cierre de la conexion serial con la Arduino Uno
captura.release() # Se libera la captura
cv.destroyAllWindows() # Se cierran todas las ventanas

