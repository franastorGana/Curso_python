'''
A partir de los siguientes datos, calcular el peso medio del sexo masculino menores de edad.

data = [
    {'nombre': 'Juan', 'edad': 20, 'sexo': 'M', 'peso': 60},
    {'nombre': 'Sergio', 'edad': 13, 'sexo': 'M','peso': 45},
    {'nombre': 'Ana', 'edad': 18, 'sexo': 'F','peso': 50},
    {'nombre': 'Alba', 'edad': 14, 'sexo': 'F','peso': 35},
    {'nombre': 'Leo', 'edad': 6, 'sexo': 'M','peso': 23},
    {'nombre': 'Evan', 'edad': 9, 'sexo': 'M','peso': 26}
]

'''

from functools import reduce

data = [
    {'nombre': 'Juan', 'edad': 20, 'sexo': 'M', 'peso': 60},
    {'nombre': 'Sergio', 'edad': 13, 'sexo': 'M', 'peso': 45},
    {'nombre': 'Ana', 'edad': 18, 'sexo': 'F', 'peso': 50},
    {'nombre': 'Alba', 'edad': 14, 'sexo': 'F', 'peso': 35},
    {'nombre': 'Leo', 'edad': 6, 'sexo': 'M', 'peso': 23},
    {'nombre': 'Evan', 'edad': 9, 'sexo': 'M', 'peso': 26}
]

# Filtrar los hombres menores de edad
hombres_menores = filter(lambda x: x['sexo'] == 'M' and x['edad'] < 18, data)

# Obtener los pesos de los hombres menores
pesos = map(lambda x: x['peso'], hombres_menores)

# Calcular el peso medio usando reduce
peso_total = reduce(lambda x, y: x + y, pesos, 0)
numero_hombres = len(list(filter(lambda x: x['sexo'] == 'M' and x['edad'] < 18, data)))

# Evitar división por cero si no hay hombres menores
peso_medio = peso_total / numero_hombres if numero_hombres > 0 else 0

print(f"El peso medio de los hombres menores de edad es: {peso_medio}")