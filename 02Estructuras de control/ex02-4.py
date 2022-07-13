# USO DE RANGE
"""
range(num) -> genera una secuencia de nº que va desde 0 hasta num-1
range(inicio, fin, salto) -> genera una secuencia de nº que va desde inicio hasta fin-1, sumando el salto
range(inicio,fin) -> genera una secuencia de nº que va desde inicio hasta fin-1, sumando un salto 1
"""
for i in (0, 1, 3, 4, 7):     # creamos una secuencia de nº manualmente
    print(i, "", end="")      # 0 1 3 4 7

print("\n", end="")  # salto manual de línea y evitamos el salto automático

for i in range(6):            # creamos una secuencia de nº de 0 a 5
    print(i, "", end="")                  # 0 1 2 3 4 5

print("\n", end="")  # salto manual de línea y evitamos el salto automático

# creamos una secuencia de 5 hasta 19, de 2 en 2. Después se convierte en lista y se almacena en c
c = list(range(5, 20, 2))
print(c)
c[3] = "a"
print(c)

# creamos una secuencia invertida, desde inicio hasta fin+1, restando el salto
for i in range(5, 0, -1):
    print(i, "", end="")                  # 5 4 3 2 1
