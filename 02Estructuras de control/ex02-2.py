# BUCLE FOR vs BUCLE WHILE
# El nº de iteraciones o ciclos de un bucle FOR se sabe a priori. En un WHILE no
# En el bucle FOR existe un iterable. En el bucle WHILE una condición logica es la que evalua cuando terminar el bucle

# Bucle que se ejecuta 5 veces
for i in range(0, 5):              # i tomará los valores del rango desde Vi hasta vf-1
    print(i, "", end="")           # Salida:  0 1 2 3 4

print("\n", end="")  # Salto de linea manual y evitamos el automático

# Bucle que se ejecuta 2 veces
for i in range(1, 3):              # i tomará los valores del rango desde Vi hasta vf-1
    print(i, "", end="")           # Salida:  1 2

print("\n", end="")  # Salto de linea manual y evitamos el automático

# El bucle for no solo permite iterar numeros, sino practicamente cualquier cosa
for i in "Python":
    print(i, ".", end="")  # Salida: P.y.t.h.o.n.

# Iterables e iteradores
"""
- iterable -> objeto que puede ser iterado = indexado = recorrido. Por ejemplo un array (o list en Python), 
es iterable, pq sus elementos son accesibles usando un indice.
Ej) lista [1, 2, 3]   ->  print(lista[1]) mostrará 2    lista[2] = 5 machacará el 3 
Ej Otros iterables en Python: tuplas, cadenas, lista, sets, diccionarios, ficheros ...

- iterador -> objeto que hace referencia a un elemento, y que tiene un método next que permite 
  hacer referencia al siguiente. La funcion iter(iterable) nos devuelve un iterador

Una vez sabido esto volvemos a ver la estructura del for:

for <variable> in <iterable>:
    ......
"""

print("\n", end="")  # Salto de linea manual y evitamos el automático

# como saber si un objeto es iterable?. Usando la función isinstance(objeto,tipo)
from collections.abc import Iterable  # de un modulo importa una determinada sección

lista = [1, 2, 3, 4]
cadena = "Python"
numero = 10
print(isinstance(lista, Iterable))    # True
print(isinstance(cadena, Iterable))   # True
print(isinstance(numero, Iterable))   # False

# uso de la funcion iter(iterable) y devuelve un iterador de la clase list_iterator
lista2 = [5, 6, 3, 2]
iterador = iter(lista2)   # iterador apunta al principio-1 de la lista
print(iterador, type(iterador))        # <list_iterator object at 0x....>  <class 'list_iterator'>
print(next(iterador))     # muestra el 1º elemento  5
print(next(iterador))     # muestra el 2º elemento  6
print(next(iterador))     # muestra el 3º elemento  3
print(next(iterador))     # muestra el 4º elemento  2
# print(next(iterador))     # da error pq nos salimos de la lista
# No existe de momento opcion para volver a elemento anteriores. prev(iterador)???

"""Existen otras clases de iteradores
str_iterator para cadenas   tuple_iterator para tuplas
set_iterator para sets  dict_keyiterator para diccionarios
"""
cadena = "Python"
iterador2 = iter(cadena)
print(iterador2, type(iterador2))        # <str_iterator object at 0x....>  <class 'str_iterator'>
print(next(iterador2), next(iterador2))  # Vemoa como avanzamos por la cadena

# FOR anidados -> Es posible anidar las estructuras, es decir, meter una dentro de otra.
lista = [[56, 34, 1], [12, 4, 5], [9, 4, 3]]     # lista de 3 listas (matriz)
for i in lista:
    print(i, "", end="")  # Salida: [56,34,1] [12,4,5] [9,4,3]
print(lista[1][0])

print("\n", end="")  # salto de línea manual y evitamos el salto de línea automático

for i in lista:
    for j in i:
        print(j, "", end="")  # Salida: 56,34,1,12,4,5,9,4,3

print("\n", end="")  # salto de línea manual y evitamos el salto de línea automático

# recorrer una cadena normalmente, en orden inverso y de 2 en 2 caracteres
texto = "Python"
for i in texto:
    print(i, "", end="")   # P y t h o n

print("\n", end="")  # salto de línea manual y evitamos el salto de línea automático

for i in texto[::-1]:
    print(i, "", end="")   # n o h t y P

print("\n", end="")  # salto de línea manual y evitamos el salto de línea automático

for i in texto[::2]:
    print(i, "", end="")   # P t o

print("\n", end="")  # Salto de linea manual y evitamos el automático

# funciones list(), sum() y cadena.join() que usamos con iterable
"""
- list(iterable) -> convierte cualquier objeto iterable en una lista que se puede almacenar o mostrar
- sum(iterable) -> para sumar todos los elementos de un iterable. Excepciones: cadenas
- cadena.join(iterable) -> Crea una cadena uniendo los elementos de una lista de caracteres, intercalandolos 
  con otra cadena.
"""
# crearemos varios tipos de iterables y mostraremos info
rango = range(5)       # 0..4
lista = list("Hola")   # ["H","o","l","a"]
tupla = (1, 2, 3)      # (1, 2, 3)
mi_set = {4, 6, 8}     # {8, 4, 6}
mi_dict = {0: "Renault", 1: "Ford", 2: "Opel"}  # {0: 'Renault', 1: 'Ford', 2: 'Opel'}

print(rango, type(rango), sum(rango))
print(lista, type(lista), "**".join(lista))
print(tupla, type(tupla), sum(tupla))
print(mi_set, type(mi_set), sum(mi_set))
print(mi_dict, type(mi_dict), sum(mi_dict))
