'''
Crear una clase Calculadora con los siguientes requisitos:

Que admita un número indefinidos de números en el constructor.
 
Que tenga un método público suma, que devuelva la suma de todos los números.


'''

class Calculadora:
    def __init__(self, *args):
        self.numeros = args

    def suma(self):
        return sum(self.numeros)
    
calculadora = Calculadora(1, 2, 3, 4, 5)

print(calculadora.suma())