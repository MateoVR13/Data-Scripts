import os
import shutil

def mover_archivos_al_directorio_principal(directorio):
    # Normalizar la ruta del directorio
    directorio = os.path.normpath(directorio)

    # Recorrer todos los archivos y subdirectorios en el directorio dado
    for root, dirs, files in os.walk(directorio, topdown=False):
        for nombre_archivo in files:
            # Obtener la ruta completa del archivo
            ruta_archivo = os.path.join(root, nombre_archivo)
            
            # Obtener la ruta de destino en el directorio principal
            ruta_destino = os.path.join(directorio, nombre_archivo)
            
            # Mover el archivo al directorio principal, sobrescribiendo si ya existe
            shutil.move(ruta_archivo, ruta_destino)
            print(f"Movido: {ruta_archivo} -> {ruta_destino}")

        # Eliminar los subdirectorios vacíos
        for nombre_dir in dirs:
            ruta_dir = os.path.join(root, nombre_dir)
            try:
                os.rmdir(ruta_dir)
                print(f"Eliminado directorio vacío: {ruta_dir}")
            except OSError as e:
                print(f"No se pudo eliminar {ruta_dir}: {e}")

if __name__ == "__main__":
    # Solicitar la ruta del directorio al usuario
    ruta_directorio = input("Introduce la ruta del directorio: ")
    
    # Verificar si la ruta es válida
    if os.path.isdir(ruta_directorio):
        mover_archivos_al_directorio_principal(ruta_directorio)
        print("Proceso completado.")
    else:
        print("La ruta proporcionada no es un directorio válido.")