'''
'el movil de ella fue encontrado en el parque’
Sustituir con una expresión regular la palabra parque por cine
Imprimir por pantalla el número de veces que se ha hecho el reemplazo

'''
import re
frase = 'el movil de ella fue encontrado en el parque'
resultado = re.sub('parque', 'cine', frase)
print(resultado)
print(resultado.count('cine'))
