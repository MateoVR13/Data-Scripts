import os
from PIL import Image
import imagehash
from collections import defaultdict
import shutil

def calcular_hash_imagen(ruta_imagen, hash_size=8):
    """Calcula el hash perceptual de una imagen."""
    imagen = Image.open(ruta_imagen)
    return imagehash.average_hash(imagen, hash_size=hash_size)

def encontrar_imagenes_similares(directorio, umbral_similitud=10):
    """Encuentra imágenes similares en un directorio."""
    hashes = {}
    for nombre_archivo in os.listdir(directorio):
        ruta_imagen = os.path.join(directorio, nombre_archivo)
        try:
            # Calcular el hash de la imagen
            hash_imagen = calcular_hash_imagen(ruta_imagen)
            hashes[nombre_archivo] = hash_imagen
        except Exception as e:
            print(f"No se pudo procesar {nombre_archivo}: {e}")

    # Agrupar imágenes similares
    grupos = defaultdict(list)
    for nombre_archivo, hash_imagen in hashes.items():
        agregado = False
        for grupo_hash in grupos:
            if hash_imagen - grupo_hash < umbral_similitud:
                grupos[grupo_hash].append(nombre_archivo)
                agregado = True
                break
        if not agregado:
            grupos[hash_imagen].append(nombre_archivo)

    return grupos

def eliminar_imagenes_similares(directorio, umbral_similitud=10):
    """Elimina imágenes similares en un directorio."""
    grupos = encontrar_imagenes_similares(directorio, umbral_similitud)

    # Crear una carpeta para mover las imágenes duplicadas
    carpeta_duplicados = os.path.join(directorio, "duplicados")
    os.makedirs(carpeta_duplicados, exist_ok=True)

    # Mover imágenes duplicadas a la carpeta de duplicados
    for grupo_hash, archivos in grupos.items():
        if len(archivos) > 1:
            print(f"Grupo de imágenes similares (hash {grupo_hash}):")
            for archivo in archivos[1:]:  # Mantener la primera imagen, mover las demás
                ruta_origen = os.path.join(directorio, archivo)
                ruta_destino = os.path.join(carpeta_duplicados, archivo)
                shutil.move(ruta_origen, ruta_destino)
                print(f"Movido: {archivo}")

if __name__ == "__main__":
    directorio_imagenes = "C:/Users/matth/Workspace/rigidos_resized"
    umbral_similitud = 10  # Ajusta este valor para controlar la sensibilidad (0 = idénticas)

    eliminar_imagenes_similares(directorio_imagenes, umbral_similitud)