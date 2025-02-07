'''
Crear una estructura de clases con las siguientes características:

Una clase padre abstracta llamada Coche.
 

Dos clases hijas de Coche llamadas Electrico y Combustion
 

La clase padre debe tener en su constructor la asignación del atributo marca y un método abstracto llamado gasto_cada_100_km.



La clase hija Electrico en su constructor debe asignar la marca y los atributos consumo_watios_hora y precio_watios_hora.
 

La clase hija Combustion en su constructor debe asignar la marca y los atributos consumo_litros_100 y precio_litro.
 

Cada clase hija debe implementar de forma obligatoria el método abstracto gasto_cada_100_km.

El método gasto_cada_100_km en la clase Electrico debe devolver el gasto con la siguiente formula:

Gasto = consumo_watios_hora * precio_watios_hora


El método gasto_cada_100_km en la clase Combustion debe devolver el gasto con la siguiente formula:

Gasto = consumo_litros_100 * precio_litro

'''
from abc import ABC, abstractmethod


class Coche(ABC):
    def __init__(self, marca):
        self.marca = marca
    
    @abstractmethod
    def gasto_cada_100_km(self):
        pass
        
# ahora genero las clases hija

class Electrico(Coche):

    def __init__(self, marca, consumo_watios_hora, precio_watios_hora):
        super().__init__(marca)
        self.consumo_watios_hora = consumo_watios_hora  # Consumo en kWh por km
        self.precio_watios_hora = precio_watios_hora  # Precio por kWh
    
    def gasto_cclearada_100_km(self):
        gasto = self.consumo_watios_hora * self.precio_watios_hora


class Combustion(Coche):
    def __init__(self, marca, consumo_litros_100, precio_litro):
        super().__init__(marca)
        self.consumo_litros_100 = consumo_litros_100  # Consumo en litros cada 100 km
        self.precio_litro = precio_litro  # Precio por litro de combustible
    
    def gasto_cada_100_km(self):
        gasto = self.consumo_litros_100 * self.precio_litro 

