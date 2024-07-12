import os

def eliminar_archivo(nombre_archivo):
    nombre_completo = os.path.join("notas", nombre_archivo)
    if os.path.exists(nombre_completo):
        os.remove(nombre_completo)
        print(f"Archivo '{nombre_archivo}' eliminado.")
    else:
        print(f"El archivo '{nombre_archivo}' no existe.")


eliminar_archivo("casa.txt")
eliminar_archivo("trabajo.txt")
