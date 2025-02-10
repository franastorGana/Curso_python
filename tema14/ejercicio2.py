'''
A partir del siguiente endpoint relativo a un API público de libros:

 

https://www.anapioficeandfire.com/api/books

 

Recuperar la información del libro cuyo nombre es:

‘A Game of Thrones’

 

Nota: El parámetro a usar en la petición GET es name.


'''
import requests

API_URL = "https://www.anapioficeandfire.com/api/books"


respuesta = requests.get(API_URL, params={"name": "A Game of Thrones"})


if respuesta.status_code == 200:
    print(respuesta.json())
else:
    print("Error al recuperar los datos")
