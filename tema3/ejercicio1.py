'''
Ejercicio balance de gastos

Definir la expresión para calcular el balance de ingresos y gastos donde:

Ingresos Totales = 2000.60 euros

Gasto1 = 500.30 euros

Gasto2 = 400.20 euros

Gasto3 = 100.10 euros

El resultado final debe ser igual a 1000.0
'''
from decimal import Decimal
# Ingresos totales
ingresos_totales = Decimal("2000.60")
# Gasto 1
gasto1 = Decimal("500.30")
# Gasto 2
gasto2 = Decimal("400.20")
# Gasto 3
gasto3 = Decimal("100.10")
# Calcular el balance de ingresos y gastos
balance = round(ingresos_totales - gasto1 - gasto2 - gasto3,1)
print(balance)
