'''
Generar un fichero nuevo con el mismo contenido pero serializado.
'''

import json

# Rutas de los archivos
fichero_original = "tema13/fichero.txt"
fichero_serializado = "tema13/fichero_serializado.json"

# Leemos el contenido del fichero original
with open(fichero_original, 'r') as f:
    contenido = f.readlines()

# Guardamos en JSON
with open(fichero_serializado, 'w') as f:
    json.dump(contenido, f, indent=4)

print(f"Archivo serializado guardado en: {fichero_serializado}")