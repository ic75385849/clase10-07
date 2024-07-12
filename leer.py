import os

def leer_archivo(nombre_archivo):
    nombre_completo = os.path.join("notas", nombre_archivo)
    if os.path.exists(nombre_completo):
        with open(nombre_completo, 'r') as archivo:
            contenido = archivo.read()
            print(f"Contenido de '{nombre_archivo}':\n")
            print(contenido)
    else:
        print(f"El archivo '{nombre_archivo}' no existe.")


leer_archivo("trabajo.txt")
