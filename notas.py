import os

def crear_notas():
    if not os.path.exists("notas"):
        os.makedirs("notas")
        print("Carpeta 'notas' creada.")
    else:
        print("La carpeta 'notas' ya existe.")

crear_notas()
