import os
from PIL import Image

def resize_images_in_directory(input_dir, output_dir, new_width):
    # Recorre todos los archivos y subcarpetas en el directorio de entrada
    for root, dirs, files in os.walk(input_dir):
        # Calcula la ruta relativa para mantener la estructura de directorios
        relative_path = os.path.relpath(root, input_dir)
        output_subdir = os.path.join(output_dir, relative_path)
        
        # Crea la subcarpeta en el directorio de salida si no existe
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)
        
        # Procesa cada archivo en la carpeta actual
        for filename in files:
            file_path = os.path.join(root, filename)
            
            try:
                with Image.open(file_path) as img:
                    width, height = img.size
                    aspect_ratio = height / width
                    new_height = int(new_width * aspect_ratio)
                    
                    resized_img = img.resize((new_width, new_height))
                    
                    output_path = os.path.join(output_subdir, filename)
                    resized_img.save(output_path)
                    print(f"Resized and saved {filename} to {output_subdir}")
                    
            except Exception as e:
                print(f"Error processing {filename}: {e}")

input_directory = 'C:/Users/matth/Downloads/flexibles_agrupados'
output_directory = 'C:/Users/matth/Downloads/flexibles_resized'
new_width = 600

resize_images_in_directory(input_directory, output_directory, new_width)