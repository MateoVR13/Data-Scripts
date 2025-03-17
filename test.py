import os
import cv2
import numpy as np
from skimage import exposure
from glob import glob


input_folder = "C:/Users/matth/Downloads/rigidos_grouped_resized"
output_folder = "output_folder_test"
reference_path = "reference.jpeg"

os.makedirs(output_folder, exist_ok=True)

reference = cv2.imread(reference_path)
reference = cv2.cvtColor(reference, cv2.COLOR_BGR2RGB)


image_paths = glob(os.path.join(input_folder, "*.jpg")) + glob(os.path.join(input_folder, "*.jpeg"))

for img_path in image_paths:

    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    matched = exposure.match_histograms(img, reference, channel_axis=-1)

    matched_bgr = cv2.cvtColor((matched * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
    output_path = os.path.join(output_folder, os.path.basename(img_path))
    cv2.imwrite(output_path, matched_bgr)

print("Procesamiento completado. Imágenes guardadas en:", output_folder)
