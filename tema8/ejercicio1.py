'''
Crear un programa que a partir de los datos numéricos de una lista L,

 cree una nueva estructura de datos con los números de la lista que sean múltiplos de X.

La lista L se creará en tiempo de ejecución y tendrá valores del 1 al 100 incluidos.
 

X será un entero solicitado por consola, cuyo valor sea entre 2 y 10.

'''
def es_numerico(cadena):
  return cadena.isnumeric() and 2 <= int(cadena) <= 10
def doy_multiplo(numero, multiplo):
    return numero * multiplo    




while True:

    numero = input("Introduce un número entre 2 y 10: ")
    if es_numerico(numero):
        # Si es válido, salimos del bucle
        break
    print("❌ Error: El número introducido no es correcto. Inténtalo de nuevo.")


numero = int(numero)
#Creamos una lista de 1 a 100
L = list(range(1,101))
multiplo  = list()

for i in L:
    multiplo.append(doy_multiplo(i, numero))

print(multiplo)
