import cv2 # Se importa 'opencv'
import numpy as np # Se importa 'numpy' como np

def etiquetas(imagen, numeroObjeto):
    imagen = imagen.astype(np.int32) # Se cambia el tipo de dato de 'uint8' a 'int32'

    height = imagen.shape[0] # Se obtiene la altura de la imagen
    width = imagen.shape[1] # Se obtiene el ancho de la imagen

    # Se convierten todos los pixeles con valor de 255 a -1
    for i in range(height):
        for j in range(width):
            if imagen[i, j] == 255:
                imagen[i, j] = -1

    cont = 0
    for i in range(height):
        for j in range(width):
            if imagen[i, j] == -1:
                cont += 1
                cv2.floodFill(imagen, None, (j, i), cont)

    # Se obtiene la mascara de la etiqueta que tenga el mismo numero
    # que recibe en la funcion
    mask = imagen == numeroObjeto

    etiqueta = imagen.copy() # Se crea una copia de la imagen

    # Se aplica la mascara a la copia de la imagen
    etiqueta[mask] = 255
    etiqueta[~mask] = 0

    # Se convierte el tipo de dato de 'int32' a 'uint8'
    imagen = imagen.astype(np.uint8)
    etiqueta = etiqueta.astype(np.uint8)

    return etiqueta, cont # Se regresa la imagen y el numero de objetos en la imagen

