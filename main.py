# Ian Mu;oz Nu;ez

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import serial
import timeit
from time import sleep

angle_plot = np.array([[], []]) # Arreglo para guardar los angulos
error_plot = np.array([[], []]) # Arreglo para guardar el error
c_plot = np.array([[], []]) # Arreglo para guardar la posicion del centroide
t_plot = np.array([]) # Arreglo para guardar el tiempo transcurrido

captura = cv.VideoCapture(2) # Conexion con la camara 0/2
fps = int(captura.get(cv.CAP_PROP_FPS)) # Frames por segundo de la camara usada
fourcc = cv.VideoWriter_fourcc(*'mp4v') # Codec para guardar los videos

# Variables usadas para escribir los datos de los videos
outVideo = cv.VideoWriter('video.mp4', fourcc, fps, (180, 180))
outMask = cv.VideoWriter('mask.mp4', fourcc, fps, (180, 180))
outNoise = cv.VideoWriter('noise.mp4', fourcc, fps, (180, 180))
outFilter = cv.VideoWriter('filter.mp4', fourcc, fps, (180, 180))

kernel = np.ones((9, 9), dtype=np.uint8) # Kernel usado para la erosion
f = np.ones((11, 11), dtype=np.float32)*1/121 # Kernel para aplicar un filtro de desenfoque al video con ruido

uno = serial.Serial('/dev/ttyACM0', 9600, write_timeout=10) # Conexion serial con Arduino
sleep(2) # Espera de 2 segundos para realizar la conexion serial correctamente

angleY = chr(90) # Inicializacion del angulo 'y' en 90 grados
angleX = chr(90) # Inicializacion del angulo 'x' en 90 grados
minAngle = 45 # Angulo minimo al que deben girar los motores
maxAngle = 135 # Angulo maximo al que deben girar los motores

# Se toma el tiempo actual
start = timeit.default_timer()
end = start

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
    mask = cv.erode(mask, kernel) # Aplicacion de la erosion
    norm = cv.normalize(mask.astype(float), None, 0.0, 1.0, cv.NORM_MINMAX) # Normalizacion de 0 a 1

    posy, posx = np.where(norm==1) # Posiciones de los 1's
    try:
        cy = int(np.sum(posy)/np.sum(norm)) # Posicion del centroide en 'y'
        cx = int(np.sum(posx)/np.sum(norm)) # Posicion del centroide en 'x'
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

    outVideo.write(video) # Se escribe el video original
    outMask.write(cv.cvtColor(mask, cv.COLOR_GRAY2BGR)) # Se escribe la mascara del video
    outNoise.write(videoNoise) # Se escribe el video con ruido
    outFilter.write(videoFilter) # Se escribe el video filtrado

    end = timeit.default_timer() # Se toma el tiempo actual
    t = end - start # Diferencia de tiempo
    t_plot = np.hstack((t_plot, t)) # Se guarda el tiempo transcurrido
    angle_plot = np.hstack((angle_plot, np.array([[ord(angleX)], [ord(angleY)]]))) # Se guardan los angulos de los servos
    error_plot = np.hstack((error_plot, np.array([[e_x], [e_y]]))) # Se guarda el error
    c_plot = np.hstack((c_plot, np.array([[cx], [cy]]))) # Se guarda la posicion del centroide

uno.close() # Cierre de la conexion serial con la Arduino Uno
captura.release() # Se libera la captura
cv.destroyAllWindows() # Se cierran todas las ventanas

# Grafica de los angulos de los motores
plt.figure(1)
plt.grid()

plt.plot(t_plot, angle_plot[0, :], linewidth=2)
plt.plot(t_plot, angle_plot[1, :], linewidth=2)

plt.title("Angulos x/y", fontsize=20)
plt.xlabel('Tiempo (s)', fontsize=15)
plt.ylabel('Angulos', fontsize=15)
plt.legend(['$angle_x$', '$angle_y$'])

# Grafica del error
plt.figure(2)
plt.grid()

plt.plot(t_plot, error_plot[0, :], linewidth=2)
plt.plot(t_plot, error_plot[1, :], linewidth=2)

plt.title("Errores x/y", fontsize=20)
plt.xlabel('Tiempo (s)', fontsize=15)
plt.ylabel('Error', fontsize=15)
plt.legend(['$e_x$', '$e_y$'])

# Grafica del centroide
plt.figure(3)
plt.grid()

plt.plot(t_plot, c_plot[0, :], linewidth=2)
plt.plot(t_plot, c_plot[1, :], linewidth=2)

plt.title("Centroides x/y", fontsize=20)
plt.xlabel('Tiempo (s)', fontsize=15)
plt.ylabel('Centroides', fontsize=15)
plt.legend(['$c_x$', '$c_y$'])

plt.show()

