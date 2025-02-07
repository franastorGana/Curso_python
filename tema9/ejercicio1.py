'''
A partir del siguiente código que calcula la raíz cubica 
de cada elemento de una lista y genera una nueva.
Crear uno equivalente con programación funcional.

def raiz_cubica(data):
    res = []
    for item in data:
        res.append(pow(item,1/3))
    return res
data = [8, 4, 6, 10, 7]
print(raíz_cubica(data)

'''

def raiz_cubica(data):
    return list(map(lambda item: pow(item, 1/3), data))

data = [8, 4, 6, 10, 7]
print(raiz_cubica(data))