import cv2 as cv
import numpy as np

captura = cv.VideoCapture(0) # Conexion con la camara 0/2

kernel = np.ones((9, 9), dtype=np.uint8) # Kernel usado para la erosion

while True:
    leido, video = captura.read() # Lectura de la camara

    if not leido: # Si hay un error con la lectura se termina el ciclo
        break

    if cv.waitKey(1) == 27: # Si se presiona 'esc' se termina el ciclo
        break

    video = cv.resize(video, None, fx=0.4, fy=0.4) # Redimension del video
    m, n = video.shape[0:2] # Dimensiones del video

    hsv = cv.cvtColor(video, cv.COLOR_BGR2HSV) # Espacio de color de BGR a HSV
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
    cv.circle(video, (cx, cy), 5, (0, 255, 0), -1) # Circulo del centroide en el video

    e_y = (m/2)-cy # Error del centroide en 'y' al centro de la imagen
    e_x = (n/2)-cx # Error del centroide en 'x' al centro de la imagen
    print(f'e_x: {e_x}')
    print(f'e_y: {e_y}')

    cv.imshow("Video", video) # Se muestra el video
    cv.imshow("Mask", mask) # Se muestra la mascara

captura.release() # Se libera la captura
cv.destroyAllWindows() # Se cierran todas las ventanas

