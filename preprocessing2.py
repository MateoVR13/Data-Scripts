import os
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import numpy as np

def procesar_imagen(imagen_path, salida_path, umbral=95):
    # Abrir la imagen
    imagen = Image.open(imagen_path)
    
    # Convertir a escala de grises
    imagen = imagen.convert("L")
    
    # Convertir la imagen a un array de NumPy para manipulación
    imagen_array = np.array(imagen)
    
    # Aplicar el umbral: grises cercanos al negro se mantienen, el resto se convierten en blanco
    imagen_array = np.where(imagen_array < umbral, imagen_array, 255)
    
    # Aumentar el contraste de los grises que se mantuvieron (oscuros)
    imagen_array = np.where(imagen_array < umbral, imagen_array * 0.5, imagen_array)  # Ajusta el factor de contraste
    
    # Convertir de nuevo a imagen PIL
    imagen = Image.fromarray(imagen_array.astype(np.uint8))
    
    # Aumentar el contraste global
    enhancer = ImageEnhance.Contrast(imagen)
    imagen = enhancer.enhance(2.0)  # Ajusta el factor de contraste global
    
    # Guardar la imagen procesada
    imagen.save(salida_path)

def procesar_carpeta(carpeta_entrada, carpeta_salida, umbral=80):
    for root, dirs, files in os.walk(carpeta_entrada):
        # Crear la estructura de subcarpetas en la carpeta de salida
        estructura_salida = os.path.join(carpeta_salida, os.path.relpath(root, carpeta_entrada))
        os.makedirs(estructura_salida, exist_ok=True)
        
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                # Rutas completas de entrada y salida
                entrada_path = os.path.join(root, file)
                salida_path = os.path.join(estructura_salida, file)
                
                # Procesar la imagen
                procesar_imagen(entrada_path, salida_path, umbral)
                print(f"Procesada: {entrada_path} -> {salida_path}")

if __name__ == "__main__":
    # Especifica las carpetas de entrada y salida
    carpeta_entrada = "C:/Users/matth/Downloads/preprocessed_flexibles"
    carpeta_salida = "C:/Users/matth/Downloads/flexibles_binarized"
    
    # Definir el umbral (ajusta según sea necesario)
    umbral = 80  # Grises por debajo de este valor se consideran cercanos al negro
    
    # Procesar todas las imágenes en la carpeta de entrada
    procesar_carpeta(carpeta_entrada, carpeta_salida, umbral)