# Visión Robótica

=
## Actividad 1

En esta actividad se observa como funciona el modelo
***RGB*** y la escala de grises en una imagen
digital.

Algunas imágenes de ejemplo son las siguientes.

<div style='text-align: center'>
    <img width=20% src='.src/actividad1_a.png'>
    <img width=20% src='.src/actividad1_b.png'>
    <img width=20% src='.src/actividad1_c.png'>
    <img width=20% src='.src/actividad1_d.png'>
</div>

Las primeras 2 son imágenes en escala de grises, mientras que las
últimas 2 usan el modelo ***RGB***.

=
## Actividad 2

La imagen usada para esta actividad es

<div style='text-align: center'>
    <img width=50% src='.src/actividad2_a1.png'>
</div>

En la actividad 2 se usan filtros ***RGB*** como este

<div style='text-align: center'>
    <img width=30% src='.src/actividad2_a2.png'>
</div>

o este

<div style='text-align: center'>
    <img width=30% src='.src/actividad2_b2.png'>
</div>

En estos filtros se extre o elimina alguno de los canales ***RGB*** de la imagen,
así, se obtienen filtros como los anteriores.

En esta actividad también se usan filtros para convertir las imagenes a escala de
grises. Se usaron 3, por escala de grises por promedio, y las ponderaciones
*BT.601* y *BT.709*.

En la siguiente imagen se muestran las 3 formas usadas para convertir una imagen
a escala de grises, además usando también el método ***RGB*** anterior.

<div style='text-align: center'>
    <img width=30% src='.src/actividad2_d1.png'>
    <img width=30% src='.src/actividad2_d2.png'>
    <img width=30% src='.src/actividad2_d3.png'>
</div>

La primer imagen es la original, en la segunda se muestra el método ***RGB*** y
en la tercera son los métodos por promedio, *BT.601* y *BT.709*.

=
## Actividad 3

En la actividad 3 se ve la manera de obtener la versión negativa de una imagen
y funciones de **open** para poder rotar una imagen.

<div style='text-align: center'>
    <img width=25% src='.src/actividad3_1.png'>
    <img width=25% src='.src/actividad3_2.png'>
    <img width=25% src='.src/actividad3_3.png'>
</div>

=
## Actividad 4

En la actividad 4 se crean y observan histogramas de imágenes con **numpy** y
**matplotlib**.

<div style='text-align: center'>
    <img width=44% src='.src/actividad4_1.png'>
    <img width=40% src='.src/actividad4_2.png'>
</div>

=
## Actividad 5

En esta actividad se ecualizan las imágenes y se observan sus histogramas, para
ver el cambio que tienen al manipular sus valores.

### Imagen original
<div style='text-align: center'>
    <img width=30% src='.src/actividad5_1.png'>
</div>

### Imagen con cambios iguales en los canales *RGB*
<div style='text-align: center'>
    <img width=30% src='.src/actividad5_2.png'>
</div>

### Imagen ecualizada
<div style='text-align: center'>
    <img width=30% src='.src/actividad5_3.png'>
</div>

### Histogramas de la imagen
<div style='text-align: center'>
    <img width=40% src='.src/actividad5_4.png'>
    <img width=40% src='.src/actividad5_4.png'>
</div>

=
## Actividad 6

En la actividad 6 se hacen pruebas con el modelo ***HSV***.

### Prueba con el parámetro *'Hue'*
<div style='text-align: center'>
    <img width=25% src='.src/actividad6_1.png'>
    <img width=25% src='.src/actividad6_2.png'>
    <img width=25% src='.src/actividad6_3.png'>
</div>

### Prueba con el parámetro *'Saturation'*
<div style='text-align: center'>
    <img width=25% src='.src/actividad6_4.png'>
    <img width=25% src='.src/actividad6_5.png'>
    <img width=25% src='.src/actividad6_6.png'>
</div>

### Prueba con el parámetro *'Value'*
<div style='text-align: center'>
    <img width=25% src='.src/actividad6_7.png'>
    <img width=25% src='.src/actividad6_8.png'>
    <img width=25% src='.src/actividad6_9.png'>
</div>

=
## Actividad 7

En esta actividad se aplican máscaras a imágenes para detectar un color usando
el espacio de color *HSV*.

### Imagen 1
<div style='text-align: center'>
    <img width=40% src='.src/actividad7_1.png'>
    <img width=40% src='.src/actividad7_2.png'>
</div>

### Imagen 2
<div style='text-align: center'>
    <img width=40% src='.src/actividad7_3.png'>
    <img width=40% src='.src/actividad7_4.png'>
</div>

### Imagen 3
<div style='text-align: center'>
    <img width=40% src='.src/actividad7_5.png'>
    <img width=40% src='.src/actividad7_6.png'>
</div>

En este caso, se buscaba aplicar la máscara para el color verde.

=
## Actividad 8

En la actividad 8 se continúa con lo que se hizo en la actividad 7, pero aquí se
busca obtener el objeto o sujeto que se encuentra cubierto por el color deseado.

<div style='text-align: center'>
    <img width=20% src='.src/actividad8_1.png'>
    <img width=20% src='.src/actividad8_2.png'>
    <img width=20% src='.src/actividad8_3.png'>
    <img width=20% src='.src/actividad8_4.png'>
</div>

Primero se obtiene la máscara, después la negativa de esta, y por último, se
cambian los pixeles que se encuentran en blanco por la los pixeles de la imagen
original.

=
## Actividad 9

Luego de lo realizado en la actividad 8, en esta actividad se cambia el fondo de
la imagen.

### Imágenes originales
<div style='text-align: center'>
    <img width=30% src='.src/actividad9_1.png'>
    <img width=30% src='.src/actividad9_2.png'>
</div>

### Imágenes obtenidas
<div style='text-align: center'>
    <img width=25% src='.src/actividad9_3.png'>
    <img width=25% src='.src/actividad9_4.png'>
    <img width=25% src='.src/actividad9_5.png'>
</div>

La idea es similar a la actividad anterior, esta vez se sustituyen los pixeles
del color por los pixeles del fondo que se quiere y al final se mezclan las
imágenes con el objeto y el fondo.

=
## Actividad 10

En esta actividad se hace lo mismo que con las actividades 7 y 8, pero esta vez
aplicadas a un video.

<div style='text-align: center'>
    <img width=40% src='.src/actividad10.jpg'>
</div>

=
## Actividad 11

En la actividad 11 se hace lo mismo que con la actividad 9, pero esta vez
aplicado a un video.

<div style='text-align: center'>
    <img width=40% src='.src/actividad11.jpg'>
</div>

=
## Actividad 12

En esta actividad se usa un algoritmo para rellenar espacios que quedaron al
segmentar el color de una imagen, esto para rellenar las figuras y después poder
hacer un etiquetado de objetos.

### Imagen original
<div style='text-align: center'>
    <img width=30% src='.src/actividad12_1.png'>
</div>

### Imágenes obtenidas con el algoritmo
<div style='text-align: center'>
    <img width=20% src='.src/actividad12_2.png'>
    <img width=20% src='.src/actividad12_3.png'>
    <img width=20% src='.src/actividad12_4.png'>
    <img width=20% src='.src/actividad12_5.png'>
</div>

Para este algoritmo primero se hace la segmentación del color, luego se obtienen
los pixeles que se van a rellenar, después se crea la imagen negativa y se
agrega a la máscara del inicio.

## Actividad 13

En la actividad 13 se usa el algoritmo para rellenar pixeles para poder
etiquetar objetos de color de mejor manera.

### Imagen original
<div style='text-align: center'>
    <img width=40% src='.src/actividad13_1.png'>
</div>

### Imagen original
<div style='text-align: center'>
    <img width=30% src='.src/actividad13_2.png'>
    <img width=30% src='.src/actividad13_3.png'>
    <img width=30% src='.src/actividad13_4.png'>
</div>

Primero se muestra la imagen con el algoritmo de rellenado aplicado, después se
muestra la imagen con el objeto al que le corresponde la etiqueta 1 y después el
de la etiqueta 2.

=
## Actividad 14

En esta actividad se detectan contornos de objetos sementados

<div style='text-align: center'>
    <img width=40% src='.src/actividad14_1.png'>
    <img width=40% src='.src/actividad14_2.png'>
</div>

=
## Actividad 15

En la actividad 15 se aplican filtros a la imagen usando ***kernels***.

Usando el ***kernel***

$$
k =
\begin{bmatrix}
    1 & 1 & 1 & 1 & 1 & 1 & 1 \\
    1 & 1 & 1 & 1 & 1 & 1 & 1 \\
    1 & 1 & 1 & 1 & 1 & 1 & 1 \\
    1 & 1 & 1 & 1 & 1 & 1 & 1 \\
    1 & 1 & 1 & 1 & 1 & 1 & 1 \\
    1 & 1 & 1 & 1 & 1 & 1 & 1 \\
    1 & 1 & 1 & 1 & 1 & 1 & 1
\end{bmatrix} \dfrac{1}{49}
$$

se tiene la imagen de la derecha
<div style='text-align: center'>
    <img width=40% src='.src/actividad15_1.png'>
    <img width=40% src='.src/actividad15_2.png'>
</div>

=
## Actividad 16

En esta actividad se usa el ***Filtro de Harris***, que sirve para detectar
esquinas en la imagen.

<div style='text-align: center'>
    <img width=40% src='.src/actividad16.jpg'>
</div>

=
## Actividad 17

En esta actividad se usa el ***Filtro de Canny***, que sirve para detectar
bordes en la imagen.

<div style='text-align: center'>
    <img width=40% src='.src/actividad17.jpg'>
</div>

=
## Actividad 18

En esta actividad se usan operaciones morfológicas a la imagen.

- Erosión
- Dilatación
- Opening
- Closing

### Imagen original
<div style='text-align: center'>
    <img width=40% src='.src/actividad18_1.png'>
</div>

### Imágenes obtenidas
<div style='text-align: center'>
    <img width=40% src='.src/actividad18_2.png'>
    <img width=40% src='.src/actividad18_3.png'>
</div>

La primer imagen tiene una operación de erosión, mientras que la segunda tiene
una operación de dilatación.

=
## Actividad 19

En la actividad 19 se usa la ***Transformada Hough***, que también sirve para
detectar bordes de una imagen.

<div style='text-align: center'>
    <img width=30% src='.src/actividad19_1.png'>
    <img width=30% src='.src/actividad19_2.png'>
    <img width=30% src='.src/actividad19_3.png'>
</div>

<div style='text-align: center'>
    <img width=30% src='.src/actividad19_4.png'>
    <img width=30% src='.src/actividad19_5.png'>
    <img width=30% src='.src/actividad19_6.png'>
</div>

=
## Proyecto 1

En el proyecto 1 se obtuvo el histograma de 3 imágenes y con este, su
exposición, si se tiene una imagen sub o sobre-expuesta la imagen se ecualiza
y se muestra en la imagen un mensaje, si no, solo se muestra un mensaje en la
imagen.

### Imagen sub-expuesta
<div style='text-align: center'>
    <img width=33% src='.src/proy1_1.png'>
    <img width=33% src='.src/proy1_2.png'>
    <img width=27% src='.src/proy1_3.png'>
</div>

### Imagen sobre-expuesta
<div style='text-align: center'>
    <img width=33% src='.src/proy1_4.png'>
    <img width=33% src='.src/proy1_5.png'>
    <img width=27% src='.src/proy1_6.png'>
</div>

### Imagen con buena exposición
<div style='text-align: center'>
    <img width=39% src='.src/proy1_7.png'>
    <img width=33% src='.src/proy1_8.png'>
</div>

=
## Proyecto 2

En el proyecto 2 se realizó la segmentación del color, pero desde un video
tomado desde la web cam de la computadora, en el video se muestra el contorno de
un objeto de color detectado.

<div style='text-align: center'>
    <img width=39% src='.src/proy2.jpg'>
</div>

=
## Proyecto 3

En este proyecto se hizo una cámara que pueda seguir un objeto de color, esto
gracias a una conexión serial con un ***Arduino*** y dos servomotores.

## Imágenes del prototipo
<div style='text-align: center'>
    <img width=40% src='.src/proy3_4.jpg'>
    <img width=40% src='.src/proy3_5.jpg'>
</div>

### Resultados obtenidos
<div style='text-align: center'>
    <img width=30% src='.src/proy3_1.png'>
    <img width=30% src='.src/proy3_2.png'>
    <img width=30% src='.src/proy3_3.png'>
</div>
