'''
Dados dos módulos en la misma carpeta con nombres modulo_1 y modulo_2, y siendo el contenido de cada uno:

	
#modulo_1
x = 2
y = 3
print(s_func(2, 3, z))


#modulo_2
def sumatorio(a, b, c):
    return a + b + c
c = 20


Añadir al modulo_1 los imports que faltan para que el print funcione y muestre 25.

Considerando que s_func representa la funcion sumatorio de modulo_2 y z representa la variable c de modulo_2

'''


from modulo_2 import c as z , sumatorio as s_func
#modulo_1
x = 2
y = 3
print(s_func(2, 3, z))