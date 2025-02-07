'''
Crear un programa que cree una guía telefónica a modo de diccionario donde 

la clave sea el nombre de la persona y el valor el número de móvil. Sobre la guía final 

se aplicará una ordenación por nombre.

El nombre y el móvil se pedirán por consola.
 

Se pedirán de forma recurrente nombre y móvil hasta que se pulse enter sin introducir ningún valor en el nombre.
'''

def ordenar_por_nombre(diccionario):
    return dict(sorted(diccionario.items()))

# Creamos un diccionario vacio

guia = {}

# Bucle infinito hasta que el usuario pulse enter sin introducir ningún valor en el nombre

while True:

    nombre = input("Introduce el nombre de la persona: ")
    if nombre == "":
        break
    telefono = input("Introduce el número de teléfono: ")
    guia[nombre] = telefono

guia = ordenar_por_nombre(guia)

print(guia)