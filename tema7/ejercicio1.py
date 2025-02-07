'''
Ejercicio con listas

A partir de la siguiente lista, genera una lista nueva sin duplicados

mi_lista = [1,2,1,4,5,6,7,8,9,6,5]
'''

mi_lista = [1,2,1,4,5,6,7,8,9,6,5]
mi_lista_set = set(mi_lista)
mi_lista_nueva = list(mi_lista_set)

print(mi_lista_nueva)