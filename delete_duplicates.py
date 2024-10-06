import os
import hashlib
from pathlib import Path

def get_file_hash(file_path):
    """Generate MD5 hash for a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates_in_main_directory(main_directory):
    """Find and delete duplicate files across subfolders in the same main directory."""
    seen_files = {}
    main_dir_path = Path(main_directory)

    if not main_dir_path.exists():
        print(f"Main directory {main_directory} does not exist.")
        return

    for folder in main_dir_path.iterdir():
        if folder.is_dir():
            for file_path in folder.rglob('*'):
                if file_path.is_file():
                    file_hash = get_file_hash(file_path)

                    if file_hash not in seen_files:

                        seen_files[file_hash] = file_path
                    else:
                        # Duplicate file, delete it
                        print(f"Duplicate found: {file_path}. Deleting.")
                        file_path.unlink()  # Deletes the file

if __name__ == "__main__":
    # Specify the main directory containing the subfolders
    main_directory = 'C:/Users/matth/Workspace/TodasLasImagenes'
    
    find_duplicates_in_main_directory(main_directory)
