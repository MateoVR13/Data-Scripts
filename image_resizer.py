import os
from PIL import Image

def resize_images_in_directory(input_dir, output_dir, new_width):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        
        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    width, height = img.size
                    aspect_ratio = height / width
                    new_height = int(new_width * aspect_ratio)
                    
                    resized_img = img.resize((new_width, new_height))
                    
                    output_path = os.path.join(output_dir, filename)
                    resized_img.save(output_path)
                    print(f"Resized and saved {filename} to {output_dir}")
                    
            except Exception as e:
                print(f"Error processing {filename}: {e}")

input_directory = 'C:/Users/matth/Workspace/Raw_Images'
output_directory = 'C:/Users/matth/Workspace/rigidos_resized'
new_width = 600

resize_images_in_directory(input_directory, output_directory, new_width)