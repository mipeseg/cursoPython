# BUCLE while -> permite ejecutar el código del cuerpo mientras se cumplan la condición
# Recordemos: el nº de iteraciones del while es indefinido. El nº de iteraciones del for es definido
x = 5
while x > 0:
    x -= 1
    print(x, "", end="")  # Salida: 4,3,2,1,0

print("\n", end="")  # salto de línea manual y evitamos el automático

# equivalente al bucle anterior

for x in range(-4, 5):         # el rango será  -4 -3 -2 -1 0 1 2 3 4
    if x <= 0:
        print(abs(x), "", end="")  # Salida: 4,3,2,1,0

# alguien puede pensar en el ejemplo anterior : pero en este bucle while si que sabemos a priori
# el nº de iteraciones. Como es eso?. Pq era un uso numérico. Pero, mira el siguiente ejemplo

print("\n", end="")  # salto de línea manual y evitamos el automático

"""
password = 0
while password != "dodo":
    print("Introduce password: ", end="")
    password = input()
print("El password", password, "es correcto")
"""

# OJO CON LOS BUCLES INFINITOS
# while True:
#    print("Bucle infinito")

# WHILE - ELSE  (El cuerpo del else se ejecutará cuando el bucle termine naturalmente, es decir,
# porque la condición sea falsa, y no porque se ha hecho uso del break.
x = 5
while x > 0:
    x -= 1
    print(x, "", end="")     # Salida: 4 3 2 1 0
else:
    print("El bucle ha finalizado")

# Bucles while anidados
# Con 3 valores y 3 digitos podemos generar 3^3 = 27 combinaciones
i, j, k = 0, 0, 0
while i < 2:               # i tomará los valores 0,1   (2 iteraciones)
    while j < 1:           # j tomará los valores 0     (1 iteración)
        while k < 3:       # k tomará los valores 0,1,2 (3 iteraciones)
            print(i, j, k)
            k += 1
        k = 0
        j += 1
    j = 0
    i += 1

# Ejemplo 1: Arbol de navidad
z = 7
x = 1
while z > 0:
    print(" " * z + "*" * x + " " * z)
    x += 2
    z -= 1

# Ejemplo 2: Recorrer lista con while
text = "Bucle"
i = 0
while i < len(text):
    print(text[0:i + 1])
    i += 1

# Ejemplo 3: Sucesión de Fibonacci (sucesión infinita de números naturales,
# donde el siguiente es calculado sumando los dos anteriores)
a, b = 0, 1
while b < 50:
    print(b, "", end="")
    a, b = b, a + b


