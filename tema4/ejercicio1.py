'''
A partir del siguiente texto, realizar las transformaciones necesarias para que: el texto:

'       el año 2022    está teniendo un     gran conflicto    internacional  '

No haya espacios al principio ni al final
Las palabras estén separadas por espacios simples
La primera letra del texto esté en mayúsculas.
'''
texto='       el año 2022    está teniendo un     gran conflicto    internacional  '

textoSinEspacios=texto.strip()
textoPrimerMayuscula = textoSinEspacios.capitalize()
print(textoSinEspacios)
print(textoPrimerMayuscula)