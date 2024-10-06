import os
import shutil

def move_files_to_main_folder(main_folder):
    # Recursively traverse the directory structure
    for root, dirs, files in os.walk(main_folder, topdown=False):
        # Move all files in the current folder to the main folder
        for file in files:
            file_path = os.path.join(root, file)
            shutil.move(file_path, main_folder)

        # After moving all files, remove empty directories
        for dir_ in dirs:
            dir_path = os.path.join(root, dir_)
            if not os.listdir(dir_path):  # Check if the folder is now empty
                os.rmdir(dir_path)
                print(f"Deleted empty folder: {dir_path}")

    # Finally, check if the top-level subfolders are empty and delete them
    for subfolder in os.listdir(main_folder):
        subfolder_path = os.path.join(main_folder, subfolder)
        if os.path.isdir(subfolder_path) and not os.listdir(subfolder_path):
            os.rmdir(subfolder_path)
            print(f"Deleted empty folder: {subfolder_path}")

if __name__ == "__main__":
    main_folder_path = input("Enter the path to the main folder: ")
    move_files_to_main_folder(main_folder_path)
    print("All files moved and empty folders deleted.")
