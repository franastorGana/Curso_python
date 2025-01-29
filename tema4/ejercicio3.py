'''
Realizar las siguientes operaciones:

Pedir por consola el año de nacimiento
Calcular la edad
Mostrar con un print la edad calculada

'''

import datetime
# Obtener el año de nacimiento del usuario
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))
anio_actual = datetime.datetime.now().year
edad = anio_actual - anio_nacimiento

print("Tu edad es:", edad)
