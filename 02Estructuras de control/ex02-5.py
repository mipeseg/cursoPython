# USOS DE break y continue
"""
Permiten alterar el comportamiento habitual de los bucles while y for. En programación estructurada,
se recomienda no utilizarlos, ya que, existen otras formas mas "elegantes" de terminar el bucle.
 - break -> rompe y termina el bucle
 - continue -> termina con el ciclo actual pero no rompe el bucle
"""

# buscamos una letra en una cadena. En el momento que encontremos la primera se termina el bucle
cadena = 'Probablemente, hoy superemos las espectativas'
for letra in cadena:
    print(letra, end="")
    if letra == 'h':
        break

print("\n", end="")  # salto de linea manual y evitamos el salto de línea automático

# A priori, es un bucle infinito, pero que podemos terminar controladamente usando break
x = 5
while True:
    x -= 1
    print(x, "", end="")
    if x == 0:
        break

print("\n", end="")  # salto de linea manual y evitamos el salto de línea automático

# Sobra decir que en bucle anidados, break solo rompe el bucle en el que se encuentra
i = j = None
for i in range(0, 4):            # se generan los valores 0 1 2 3
    for j in range(0, 4):        # se generan los valores 0 1 2 3
        break                    # rompe antes que termine el primer ciclo
    print(i, j)

# Imprimimos todos los caracteres de una cadena menos una letra que elegimos
cadena = 'Python es el lenguaje más usado hoy día'
for letra in cadena:
    if letra == 'a':
        continue
    print(letra, end="")
