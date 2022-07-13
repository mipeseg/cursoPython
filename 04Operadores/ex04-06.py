"""
OPERADORES DE IDENTIDAD ( identity operators)
 is -> indica si 2 variables hacen referencia a la misma dirección de memoria, vamos si tienen la misma id
 is not -> indica si 2 variables NO HACEN referencia a la misma dirección de memoria, vamos q tiene distinta id

Reglas de prioridad (de mayor a menor prioridad) ->
mas info: https://docs.python.org/3/reference/expressions.html#operator-precedence
"""
# EJEMPLOS
a = 10
b = 10

print(a is b)  # True
print(id(a), id(b))  # Tienen el mismo id, pq Python aprovecha que tienen el mismo valor para
# ahorrar memoria. El usuario no se entera. Eso sí, en el momento que una de las dos cambie su valor, ya
# ya se reservan dos direcciones de memoria distintas
b = 5
print(a is b)  # False
print(id(a), id(b))


a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True    porque el contenido de ambas listas es el mismo
print(a is b)   # False   porque las direcciones de memoria son distintas
print(id(a), id(b))

print(a is not b)   # True

x = 5
y = 5
print(id(x), id(y))
print(x is not y)  # False

"""
OPERADORES DE MEMBRESÍA ( merbership operators)
  in -> Permite saber si un elemento está contenido en una secuencia. NOTA: el elemento a la
        derecha del in debe ser iterable
  not in -> Permite saber si un elemento NO ESTÁ contenido en una secuencia
  
Reglas de prioridad (de mayor a menor prioridad) ->
mas info: https://docs.python.org/3/reference/expressions.html#operator-precedence
"""

# EJEMPLOS
print(3 in [1, 2, 3])  # True
print(12 in range(0, 5))  # False
# print(3 in 3) # Error! TypeError  El 3 de la derecha del in no es un iterable
print([1, 2] in [4, [1, 2], 7])  # True

print(3 not in [1, 2, 4, 5])  # True

# En otros lenguajes no existen los operadores is o not is
# Si en Python no existiera lo podríamos programar nosotros
x = 2
lista2 = [1, 2, 3, 4, 5]

# Función que implementa "is" y "is not"


def esta(num, lista):
    for i in lista:
        if i == num:
            return True
    return False


print(esta(x, lista2))
