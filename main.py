import cv2 # Se importa 'opencv'

captura = cv2.VideoCapture(0) # Se inicia la captura del video

width = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH)) # Se obtiene el ancho de la captura
height = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Se obtiene el alto de la captura
fps = 10 # Se definen los fps para grabar el video

fourcc = cv2.VideoWriter_fourcc(*"mp4v") # Se crea el codec para grabar el video
output = cv2.VideoWriter("out.mp4", fourcc, fps, (width, height), 0) # Se define el archivo de salida para grabar el video

# Ya que solo se quieren grabar 5 segundos de video...
i = 0 # Se crea un iterador
while i < 50: # Ya que los fps son 10, 10*5 = 50
    leido, frame = captura.read() # Se lee el contenido del video

    # Si ya no se puede leer el video, se termina el ciclo
    if not leido:
        break

    # Si se presiona la tecla 'esc' se termina al ciclo
    if cv2.waitKey(1) == 27:
        break

    grises = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Se convierte el frame a escala de grises
    blur = cv2.GaussianBlur(grises, (3, 3), 0) # Se aplica una sombra Gaussiana al frame
    canny = cv2.Canny(image=grises, threshold1=10, threshold2=200) # Se aplica el algoritmo de Canny al frame

    output.write(canny) # Se graba el frame con el algoritmo de Canny

    cv2.imshow("Captura", frame) # Se muestra el frame original
    cv2.imshow("Algoritmo de Canny", canny) # Se muestra el algoritmo de Canny

    i += 1 # Incrementa el valor del iterador

captura.release() # Se libera la captura
cv2.destroyAllWindows() # Se cierran todas las ventanas

