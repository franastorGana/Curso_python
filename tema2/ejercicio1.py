#creamos una lista con los dias de diario en orden
dias = ["lunes","martes","miercoles","jueves","viernes"]
#añadmos el domingo
dias.append("domingo")
#añadimos el sabado antes del domingo
dias.insert(5,"sabado")
#A partir de la lista crear una nueva solo con lunes, miércoles y  viernes
dias2 =dias[0:5:2]
#De la última lista, ordenar los días de la semana por orden alfabético
dias2.sort()
