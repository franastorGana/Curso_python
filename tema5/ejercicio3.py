'''
Pedir al usuario por consola que introduzca números enteros, para ello mostrar un mensaje donde se pida un número,
y tras pulsar enter se vuelva a pedir otro, y así hasta que el usuario pulse cero.
 
Con los números introducidos, crear una lista de los que son primos, sin elementos duplicados y mostrarla por pantalla.


'''
import math

 # Funcion que nos dice si un numero es primo
def es_primo(numero):
    # Caso especial: los números menores o iguales a 1 no son primos
    if numero <= 1:
        return False
    
    # El número 2 es primo
    if numero == 2:
        return True
    
    # Los números pares mayores que 2 no son primos
    if numero % 2 == 0:
        return False
    
    # Comprobamos los divisores impares hasta la raíz cuadrada del número
    for i in range(3, int(math.sqrt(numero)) + 1, 2):
        if numero % i == 0:
            return False
    
    # Si no se encontró ningún divisor, es primo
    return True


# Aqui vamos a guardar los numeros que introduce el usuario
numeros = []

# Bucle para pedir números al usuario
while True:
    # Pedimos un número entero
    numero = int(input("Introduce un número (0 para salir): "))
    
    # Si el número es 0, salimos del bucle
    if numero != 0:
        numeros.append(numero)
    else:
        print(numeros)
        print("Has pulsado 0 finalizamos la introduccion de datos.")
        break


# Creamos una lista vacia para guardar los numeros primos
primos = []
#ahora convierto primos en un conjunto para eliminar duplicados

primos_set = set(primos)

for numero in numeros:
    # Si el número es primo y no está en la lista de primos, lo añadimos
    if es_primo(numero) and numero not in primos:
        primos_set.add(numero)

#ahora convertimos el conjunto en una lista

primos = list(primos_set)

print("Los números primos introducidos son:", primos)




