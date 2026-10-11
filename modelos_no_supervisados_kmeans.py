from pathlib import Path
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

CANTIDAD_COLORES = 10
RUTA_IMAGEN = Path("colores.jpg")

image = Image.open(RUTA_IMAGEN).convert("RGB")
pixeles=np.array(image)
alto,ancho,canales = pixeles.shape

#Cada fila es un color 
colores = pixeles.reshape(-1,canales)
k_means = KMeans(n_clusters=CANTIDAD_COLORES,random_state=42,n_init=10)
etiquetas = k_means.fit_predict(colores)

#El centro de cada grupo es el color solido
paleta = k_means.cluster_centers_.astype(np.uint8)
colores_reducidos = paleta[etiquetas]

imagen_reducida = colores_reducidos.reshape(alto,ancho,canales)
Image.fromarray(imagen_reducida).save("imagen_7_colores.jpg")

print("colores solidos:")
for indice, color in enumerate(paleta):
    print(f"{indice}: RGB{tuple(int(valor) for valor in color)}")
