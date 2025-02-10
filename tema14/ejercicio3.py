'''
A partir del siguiente endpoint relativo a un API público de libros:

 

https://www.anapioficeandfire.com/api/books

 

Devolver el número de páginas del libro: ‘'A Feast for Crows’’

 

Nota: El atributo que se debe consultar es: 'numberOfPages'
'''

import requests

API_URL = "https://www.anapioficeandfire.com/api/books"

respuesta = requests.get(API_URL, params={"name": "A Feast for Crows"})

if respuesta.status_code == 200:
    libro = respuesta.json()
    print(f"El número de páginas del libro es: {libro[0]['numberOfPages']}")
else:
    print("Error al recuperar los datos")