"""
TIPOS DE ESTRUCTURA DE DATOS: SET

  Es un tipo de estructura de datos parecida a la lista, con las siguientes características:

  a) Permite almacenar un grupo de datos (homogéneo o heterogéneo)
  b) Dinamicos: Pueden añadirse, borrarse, etc elementos al conjunto
  b) elementos inmutables (no pueden ser modificados después de declararse)
  c) No puede haber elementos iguales
  d) Desordenado (los elementos no mantienen el orden en el que fueron creados)
  e) NO INDEXABLES mediante indice
"""
# Creación de un set con {}
s = {51, 4, 6, 8, 8, 1, "Hola"}   # Consideraciones: un 8 se descartar. El orden es aleatorio?
print(s, type(s))                 # {1, 51, 4, 6, 'Hola', 8} <class 'set'>

# Creación con la funcion set(iterable), que convierte cualquier iterable en set
s2 = set("Hola")    # conversión de cadena a set
s3 = set([1, 2, 3])      # conversión de lista a set
s4 = set((4, 5, 6))      # conversión de tupla a set
print(s2, s3, s4)

# un set no es accesible mediante indice. Dará un error como este -> TypeError: 'set' object is not subscriptable
# print(s[0])

# Los elementos de un set, son inmutables. Por tanto no pueden ser ni listas ni diccionarios
lista = ["Perú", "Argentina"]
# s = set(["México", "España", lista])     # TypeError: unhashable type: 'list'

# iterar los elementos de un set
s5 = {5, 6, 7, 8}
for a in s5:
    print(a, "", end="")        # 8, 5, 6, 7

print("\n", end="")   # salto manual de linea y evitamos el automático

# con la función len(iterable) podemos saber la longitud del set
print("La longitud de s5 es %d elementos" % (len(s5)))

# comprobar si un elemento está incluído en el set
s6 = {"Guitarra", "Bajo"}
print("El elemento 'Guitarra' está en s?", "guitarra" in s6)      # True

# podemos unir sets con el operador |
s7 = {1, 2}
s8 = {"hola", "adiós"}
s9 = s7 | s8 | {100, 200}   # unimos set7, set8 y un set literal creado en el momento
print(s9)     # {1, 2, 100, 200, 'adiós', 'hola'}

# Métodos de la clase set
# add(elemento) -> permite añadir un elemento al set
s10 = {14.5, 153.67}
s10.add(12)
print(s10)

# remove(elemento) -> elimina el elemento del set. Si no se encuentra, se lanza la excepción KeyError
s10.remove(12)
print(s10)

# discard(elemento) -> elimina el elemento del set. Si no se encuentra, no provoca error
s10.discard(8)
print(s10)

# pop() -> elimina un elemento del set, elegido de forma aleatoria
s10.pop()
print(s10)

# clear() -> elimina todos los elementos del set
s10.clear()
print(s10)  # set()

# union e interseccion de sets
s11 = {1, 2, 3}
s12 = {3, 4, 5}
print(s11.union(s12))    # {1, 2, 3, 4, 5}
print(s11.intersection(s12))    # {3}

"""
OTROS MÉTODOS DE LOS SETS (Los veremos en un nivel más avanzado)

s1.union(s2[, s3 ...])
s1.intersection(s2[, s3 ...])
s1.difference(s2[, s3 ...])
s1.symmetric_difference(s2)
s1.isdisjoint(s2)
s1.issubset(s2)
s1.issuperset(s2)
s1.update(s2[, s3 ...])
s1.intersection_update(s2[, s3 ...])
s1.difference_update(s2[, s3 ...])
s1.symmetric_difference_update(s2)
"""

"""
TIPOS DE ESTRUCTURA DE DATOS: FROZENSET

  Es un set con estas características:

  a) Permite almacenar un grupo de datos (homogéneo o heterogéneo)
  b) Frozenset no es dinámico (no se puede usar add(), clear())
  b) El frozenset sus elementos son inmutables
  c) No puede haber elementos iguales
  d) Desordenado (los elementos no mantienen el orden en el que fueron creados)
  e) NO INDEXABLES mediante indice
"""
# Creación de un frozenset con la función frozenset()
fs = frozenset([1, 2, 3])
print(fs, type(fs))           # frozenset({1, 2, 3}) <class 'frozenset'>

# el siguiente código produce errores
# fs.add(4)        # Error! AttributeError
# fs.clear()       # Error! AttributeError
