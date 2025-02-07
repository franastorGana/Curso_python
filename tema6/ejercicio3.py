'''
Crear una aplicación con los siguientes requisitos:

Que pida el nombre y la edad por consola.
 
Si el nombre no es alfanumérico que se lance un error personalizado que le informe al usuario con un print.

Si la edad no es numérica que se lance un error personalizado que le informe al usuario con un print.
 
En caso de que ambos sean correctos, informarlo con un print al usuario. 
 
En caso de que alguno de los dos, o los dos sean incorrectos. Pedir los datos de nuevo.



'''
# Creamos una funcion que nos dice si un string es alfanumerico
def es_alfanumerico(cadena):
    return cadena.isalnum()
def es_numerico(cadena):
    return cadena.isnumeric()

# Bucle infinito hasta que el usuario ingrese datos correctos
while True:
    nombre = input("Introduce tu nombre: ")
    edad = input("Introduce tu edad: ")

    # Verificamos si los datos son incorrectos
    if not es_alfanumerico(nombre):
        print("❌ Error: El nombre no es alfanumérico. Inténtalo de nuevo.")
        continue  # Volver a pedir los datos

    if not es_numerico(edad):
        print("❌ Error: La edad no es numérica. Inténtalo de nuevo.")
        continue  # Volver a pedir los datos

    # Si ambas verificaciones son correctas, salimos del bucle
    print(f"✅ Nombre: {nombre}, Edad: {edad}. Datos correctos.")
    break  # Salimos del bucle
