'''
A partir del siguiente endpoint relativo a un API público de libros:

 

https://www.anapioficeandfire.com/api/books

 

Recuperar el número de libros que hay almacenados a partir de una petición GET

'''
import requests

API_URL = "https://www.anapioficeandfire.com/api/books"

respuesta = requests.get(API_URL)
if respuesta.status_code == 200:
    libros = respuesta.json()
    print(f"El número de libros almacenados es: {len(libros)}")
else:
    print("Error al recuperar los datos")