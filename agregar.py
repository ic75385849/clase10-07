import os

def agregar_nota(nombre_archivo, nota):
    nombre_completo = os.path.join("notas", nombre_archivo)
    if os.path.exists(nombre_completo):
        with open(nombre_completo, 'a') as archivo:
            archivo.write(nota + "\n")
        print(f"Nota añadida al archivo '{nombre_archivo}'.")
    else:
        print(f"El archivo '{nombre_archivo}' no existe.")


agregar_nota("trabajo.txt", "16 de julio recordar santo de jeyson. fiestaaaaa")
agregar_nota("casa.txt", "el soat caduca el otro mes")
