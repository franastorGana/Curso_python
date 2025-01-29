'''
Ejercicio con operaciones numéricas y booleanas

Definir la expresión que devuelve si:

5 se encuentra en la lista formada por los números 2, 3, 4 y 5


Y además:

Si 1 entre la raíz cuadrada de 2 es igual 0.25


El resultado final debe ser True

'''
# primero definimos la lista

numeros = [2, 3, 4, 5]

comprobar = 5

#ahora comprobamos si el numero 5 esta en la lista

indice = numeros.index(comprobar)
print(comprobar)
print(indice)
resultado = comprobar == indice

print(resultado)

#comprobar 5 se encuentra en la lista formada por los números 2, 3, 4 y 5

lista = [2, 3, 4, 5]
#ahora comprobamos si el numero 5 esta en la lista
indice = lista.index(5)
numero = lista[indice]
#si esta devolvemos un true
resultado = numero == 5
print(resultado)

#Si 1 entre la raíz cuadrada de 2 es igual 0.25
resultado = 1 / (2**0.5) == 0.25
print(resultado)
