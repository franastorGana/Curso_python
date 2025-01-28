#crear un set vacio
primerSet = set()
#añadir al set los numeros del 1 al 10
primerSet.update(range(1,11))
#Crear un segundo set con números del 5 al 15
segindoSet = set(range(5,16))
#Crea un nuevo set que tenga los números de ambos set
tercerSet = primerSet.union(segindoSet)
#Sobre el último set dejar sólo los elementos que no estén en el segundo set
tercerSet = tercerSet.difference(segindoSet)
