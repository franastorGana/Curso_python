'''
A partir de la siguiente matriz generada por una lista anidada, 
obtén una nueva lista con la diagonal izquierda (valores 1, 5 y 8).
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

'''
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
 #print(len(matriz))
# Extraemos la diagonal izquierda (valores donde fila == columna)
diagonal_izquierda = [matriz[i][i] for i in range(len(matriz))]

# Mostramos el resultado
print(diagonal_izquierda)  # Salida esperada: [1, 5, 9]