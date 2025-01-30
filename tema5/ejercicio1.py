'''
Ejercicio sobre variables globales y locales

Sobre el siguiente extracto de código, introduce las sentencias necesarias dentro de la funcion my_function_1 para que el valor de a que muestre el print sea de 25.

Ejercicio 1

a = 20

def my_funcion_1():
……….
……….

my_funcion_1() 
print(a)

'''
a = 20

def my_funcion_1():
 global a
 a = 25

my_funcion_1()
print(a)