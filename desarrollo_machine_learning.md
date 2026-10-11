# Pixel art con K-Means

Este ejercicio utiliza un modelo de inteligencia artificial no supervisado: **K-Means**.

El objetivo es crear un pequeño software capaz de tomar imágenes normales, con muchos colores, y convertirlas en pixel art de alta calidad. K-Means agrupa los píxeles de color parecido y sustituye cada grupo por un color sólido. Así se obtiene una paleta reducida y una imagen en bloques nítidos, sin mezclar tonos.

## Cómo funciona

1. Se carga una imagen de entrada.
2. Se reduce a una cuadrícula de 32×32. Cada píxel resume una zona de la foto original.
3. K-Means agrupa esos píxeles en la cantidad de colores indicada (por ejemplo, 5).
4. Cada píxel se reemplaza por el color sólido de su grupo.
5. El resultado se amplía con vecinos más cercanos para verse como pixel art, y se guarda junto con la paleta de colores.

## Archivos

- `desarrollo_machine_learning.ipynb`: cuaderno del ejercicio. Descarga la imagen, la convierte en pixel art de 32×32 con K-Means y guarda la imagen reducida y la paleta.
- `modelos_no_supervisados_kmeans.py`: script que aplica el mismo agrupamiento sobre una imagen local y escribe el resultado con la paleta de colores sólidos.
