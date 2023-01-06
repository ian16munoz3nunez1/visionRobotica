import cv2 # Se importa 'opencv'
from time import sleep # Se importa el modulo 'sleep' de la libreria 'time'

captura = cv2.VideoCapture("leon.mp4") # Se inicia la captura del video
fondo = cv2.imread("rotonda.jpg") # Se lee la imagen que se usara de fondo

width = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH)) # Se obtiene el ancho de la imagen
height = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Se obtiene el alto de la imagen
fps = int(captura.get(cv2.CAP_PROP_FPS)) # Se obtienen los fps del video
escala = 0.5 # Se declara el valor para escalar los frames del video

fourcc = cv2.VideoWriter_fourcc(*"mp4v") # Se crea el codec para grabar el video
output = cv2.VideoWriter("out.mp4", fourcc, fps, (width, height)) # Se define el archivo de salida para grabar el video

# Ya que solo se quieren grabar 5 segundos del video original...
i = 0 # Se crea un iterador
while i < 150: # Ya que los fps son 30, 30*5 = 150
    leido, frame = captura.read() # Se lee el contenido del video

    # Si ya no se puede leer el video, se termina el ciclo
    if not leido:
        break

    # Si se presiona la tecla 'esc' se termina el ciclo
    if cv2.waitKey(1) == 27:
        break

    fondo = cv2.resize(fondo, (frame.shape[1], frame.shape[0])) # Se cambia la dimension del fondo para coincidir con el video
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Se convierte el frame de BGR a HSV
    mask = cv2.inRange(frameHSV, (45, 100, 100), (60, 255, 255)) # Se obtiene la mascara del frame
    maskNegativa = cv2.bitwise_not(mask) # Se obtiene la negativa de la mascara
    frameMask = cv2.bitwise_and(frame, frame, mask=maskNegativa) # Se aplica la mascara al frame
    fondoMask = cv2.bitwise_and(fondo, fondo, mask=mask) # Se aplica la mascara al fondo

    frameFondo = cv2.bitwise_or(frameMask, fondoMask) # Se unen la imagen y el fondo
    output.write(frameFondo) # Se graba el frame con la mascara aplicada

    frame = cv2.resize(frame, None, fx=escala, fy=escala) # Se cambian las dimensiones del frame original
    frameFondo = cv2.resize(frameFondo, None, fx=escala, fy=escala) # Se cambian las dimensiones del resultado

    cv2.imshow("Frame", frame) # Se muestra el video original
    cv2.imshow("Frame-Fondo", frameFondo) # Se muestra el resultado

    sleep(1/fps) # El programa espera 1/fps, es decir, 1/30 segundos
    i += 1 # Incrementa el iterador

cv2.destroyAllWindows() # Se cierran todas las ventanas

