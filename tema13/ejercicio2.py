'''
Generar uno nuevo que contenga únicamente las líneas pares, 
pero filtrando el contenido del fichero original con programación funcional, 
sin usar en la solución estructuras for ni while
'''
def es_par(numero):

    return numero % 2 == 0

#definimos la ruta del fichero

fichero_original = "tema13/fichero.txt"

#creamos el nuevo fichero donde guardaremos las lineas pares

fichero_pares = "tema13/fichero_pares2.txt"

# Leemos todas las líneas del fichero original
with open(fichero_original, 'r') as f:
    lineas = f.readlines()

# Filtramos las líneas pares utilizando programación funcional
lineas_pares = list(map(lambda x: x[1], filter(lambda x: es_par(x[0] + 1), enumerate(lineas))))

# Guardamos las líneas pares en un nuevo fichero
with open(fichero_pares, 'w') as f:
    f.writelines(lineas_pares)