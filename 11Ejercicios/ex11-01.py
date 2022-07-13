"""
VALORES ALEATORIOS
"""
import random

print(random.randint(0, 30))  # numero aleatorio entre 0 y n
print(random.uniform(0, 30))  # numero aleatorio decimal entre 0 y n
print(random.random())  # numero aleatorio decimal entre 0 y 1
print(random.choice(["A", "B", "C"]))   # elemento aleatorio de una lista

print()

"""
MEDIR TIEMPO DE EJECUCIÓN

Programar no es hacer sólo código que funcione, sino que lo haga en el menor tiempo de ejecución posible
Ej= imagináis 5 horas para consultar el saldo bancario?

CONSEJOS:
  - no perdamos el tiempo optimizando código que usan pocos usuarios
  - Dependiendo de múltiples factores (SO, carga del sistema, etc...) los tiempos nunca serán identicos
    Por ello, haz varias medidas y calcula el promedio
"""

# EJEMPLO 1
import time
inicio = time.time()   # el método time() indica los segundos transcurridos desde 01/01/1970

# Código a medir
time.sleep(3)          # el método sleep detiene la ejecución del programa x segundos
# -------------

fin = time.time()      # el método time() indica los segundos transcurridos desde 01/01/1970
print(inicio, fin, fin-inicio)    # 1.0005340576171875

# EJEMPLO 2: tiempo que tarda en calcular los primeros 10000000 números pares.

inicio = time.time()  # el método time() indica los segundos transcurridos desde 01/01/1970

# Código a medir
lista = [i for i in range(10000000) if i % 2 == 0]
# -------------

fin = time.time()   # el método time() indica los segundos transcurridos desde 01/01/1970

print(fin-inicio)   # 0.4796144962310791 segundos
