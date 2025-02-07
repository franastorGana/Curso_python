'''
A partir del siguiente código que calcula la suma parcial de cada elemento y después la total.

 Crear uno equivalente con programación funcional.

data = [[1,2], [3,4], [5,6]]
res1 = []
for item in data:
    res1.append(sum(item))
print(sum(res1))

 
 '''

data = [[1, 2], [3, 4], [5, 6]]

resultado = sum(map(sum, data))

print(resultado)