import cv2 # Se importa 'opencv'

def findObject(imagen, mask, color):
    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Se obtienen los contornos del objeto

    # Por cada contorno encontrado
    for c in cnts:
        area = cv2.contourArea(c) # Se obtiene el area del contorno

        if area > 300: # Si el area del contorno es mayor a 300
            cv2.drawContours(imagen, c, -1, color, 3) # Se dibuja el contorno

            x, y, w, h = cv2.boundingRect(c) # Se obtienen las posiciones y dimensiones del contorno

            cv2.rectangle(imagen, (x, y), (x+w, y+h), color, 3) # Se dibuja un rectangulo que que contenga al objeto

captura = cv2.VideoCapture(0) # Se inicia la captura del video

width = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH)) # Se obtiene el ancho del video
height = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Se obtiene el alto del video
fps = 10 # Se declaran los fps para grabar el video

fourcc = cv2.VideoWriter_fourcc(*"mp4v") # Se crea el codec para grabar el video

output = cv2.VideoWriter("out.mp4", fourcc, fps, (width, height)) # Se define el archivo de salida para grabar el video

# Se definen los valores minimo y maximo del color a identificar
yellowMin = (15, 100, 100)
yellowMax = (45, 255, 255)

# Ya que solo se quieren grabar 20 segundos de video...
i = 0 # Se crea un iterador
while i < 200: # Ya que los fps son 10, 10*20 = 200
    leido, frame = captura.read() # Se lee el contenido del video

    # Si ya no se puede leer el video, se termina el ciclo
    if not leido:
        break

    # Si se presiona la tecla 'esc' se termina el ciclo
    if cv2.waitKey(1) == 27:
        break

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Se convierte el frame de BGR a HSV

    mask = cv2.inRange(frameHSV, yellowMin, yellowMax) # Se obtiene la mascara del frame

    findObject(frame, mask, (0, 255, 255)) # Se llama a la funcion 'findObject' para dibujar los contornos y su cuadro delimitador

    cv2.putText(frame, "M. N. I. E.", (10, 100), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 0), 5) # Se imprime el mensaje 'M. N. I. E.' en el frame
    output.write(frame) # Se graba el frame

    frame = cv2.flip(frame, 1) # Se aplica un efecto de espejo al frame
    cv2.imshow("Video", frame) # Se muestra el frame con los contornos, el cuadro delimitador y el mensaje

    i += 1 # Incrementa el valor del iterador

captura.release() # Se libera la captura
cv2.destroyAllWindows() # Se cierran todas las ventanas

