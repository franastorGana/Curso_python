'''
A partir de un fichero de texto con el siguiente contenido:

linea 1
linea 2
linea 3
linea 4
linea 5
linea 6

Generar uno nuevo que contenga únicamente las líneas pares.

'''
def es_par(numero):

    return numero % 2 == 0

#definimos la ruta del fichero

fichero_original = "tema13/fichero.txt"

#creamos el nuevo fichero donde guardaremos las lineas pares

fichero_pares = "tema13/fichero_pares.txt"

#ahora abrimos el fichero y vamos recorriendo las lineas

with open(fichero_original, 'r') as fichero, open(fichero_pares, 'w') as fichero_pares:
    contador = 1
    for line in fichero:
        if es_par(contador):
            fichero_pares.write(line)  # Guardamos solo líneas pares
        contador += 1  # 
    contador +=1
    