import os
import cv2
import numpy as np
from skimage import exposure
from glob import glob

input_folder = "C:/Users/matth/Downloads/clasf_alexis"
output_folder = "output_folder_test"
reference_path = "reference.jpeg"

os.makedirs(output_folder, exist_ok=True)

# Cargar imagen de referencia
reference = cv2.imread(reference_path)
reference = cv2.cvtColor(reference, cv2.COLOR_BGR2RGB)

# Buscar imágenes en todas las subcarpetas
image_paths = glob(os.path.join(input_folder, "**", "*.jpg"), recursive=True) + \
              glob(os.path.join(input_folder, "**", "*.jpeg"), recursive=True)

for img_path in image_paths:
    # Leer imagen
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Igualar histograma
    matched = exposure.match_histograms(img, reference, channel_axis=-1)

    # Convertir de nuevo a BGR y guardar
    matched_bgr = cv2.cvtColor((matched * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)

    # Crear la ruta de salida manteniendo la estructura de carpetas
    relative_path = os.path.relpath(img_path, input_folder)  # Ruta relativa desde la carpeta de entrada
    output_path = os.path.join(output_folder, relative_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Crear subcarpeta si no existe
    cv2.imwrite(output_path, matched_bgr)

print("Procesamiento completado. Imágenes guardadas en:", output_folder)