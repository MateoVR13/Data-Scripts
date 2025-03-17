import os
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

def procesar_imagen(imagen_path, salida_path):
    # Abrir la imagen
    imagen = Image.open(imagen_path)
    
    # Convertir a blanco y negro
    imagen = imagen.convert("L")
        


    # Aumentar el contraste en un 100%
    enhancer = ImageEnhance.Contrast(imagen)
    imagen = enhancer.enhance(4.0)  # 2.0 significa un aumento del 100%

    # Invertir colores
    imagen = ImageOps.invert(imagen)
    
    # # Aplicar un filtro para resaltar bordes (detectar grietas y baches)
    # imagen_bordes = imagen.filter(ImageFilter.FIND_EDGES)
    
    # # Combinar la imagen original con los bordes resaltados
    # imagen = Image.blend(imagen, imagen_bordes, alpha=0.7)

    enhancer2 = ImageEnhance.Brightness(imagen)
    imagen = enhancer2.enhance(0.65) 

    # Aumentar el contraste en un 100%
    enhancer = ImageEnhance.Contrast(imagen)
    imagen = enhancer.enhance(2.0)  # 2.0 significa un aumento del 100%

    # Invertir colores
    imagen = ImageOps.invert(imagen)

    # Guardar la imagen procesada
    imagen.save(salida_path)

def procesar_carpeta(carpeta_entrada, carpeta_salida):
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
                procesar_imagen(entrada_path, salida_path)
                print(f"Procesada: {entrada_path} -> {salida_path}")

if __name__ == "__main__":
    # Especifica las carpetas de entrada y salida
    carpeta_entrada = "C:/Users/matth/Downloads/flexibles_grouped_resized"
    carpeta_salida = "C:/Users/matth/Downloads/preprocessed_flexibles"
    
    # Procesar todas las imágenes en la carpeta de entrada
    procesar_carpeta(carpeta_entrada, carpeta_salida)