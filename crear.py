import os

def crear_archivo(nombre_archivo):
    nombre_completo = os.path.join("notas", nombre_archivo)
    if not os.path.exists(nombre_completo):
        with open(nombre_completo, 'w') as archivo:
            archivo.write("hola que tal bienvenido a:{}!\n\n".format(nombre_archivo))
        print(f"Archivo '{nombre_archivo}' creado en 'notas'.")
    else:
        print(f"El archivo '{nombre_archivo}' ya existe en 'notas'.")


crear_archivo("casa.txt")
crear_archivo("trabajo.txt")
