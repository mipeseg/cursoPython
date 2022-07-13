"""
TIPOS DE ESTRUCTURA DE DATOS: TUPLA O TUPLE

  Es un tipo de estructura de datos muy parecida a la lista, con las siguientes características:

  a) Permite almacenar un grupo de datos (homogéneo o heterogéneo)
  B) INMUTABLES (Sus elementos no pueden ser modificados después de declararse)
  c) Ordenadas (los elementos mantienen el orden en el que fueron creados)
  d) Indexables mediante indice ( tupla[i])  OJO: Sólo para consulta, no para modificación de sus elementos
  e) Anidables ( podemos encontrar tuplas dentro de otras)
"""

# declaración de una tupla
tupla1 = (45, 690, -27)                   # 1º forma
tupla2 = 15, "Kilos", 690, "Litros"       # 2ª forma
print(tupla1, type(tupla1), "###", tupla2, type(tupla2))

# Comprobamos su inmutabilidad
# tupla1[1] = 1           # esto daría un error
print(tupla1[1])

# anidamiento de tuplas
tupla3 = (1, 2, ("antes", "b"), 3)
print(tupla3)             # (1, 2, ('antes', 'b'), 3)
print(tupla3[2][0])       # a

# conversión de un iterable en tupla -> tuple(iterable)
cad = "videojuegos"
lista = [1, 3, "ab", 6]
set1 = {1, 3, 5, 9}
dicci = {1: "hola", 2: "adios"}
print(tuple(cad))       # ('v', 'i', 'd', 'e', 'o', 'j', 'u', 'e', 'g', 'o', 's')
print(tuple(lista))     # (1, 3, 'ab', 6)
print(tuple(set1))      # (1, 3, 5, 9)
print(tuple(dicci))     # (1, 2)    SOLO TOMA LOS INDICES

# iterar o recorrer una tupla
tupla4 = (1, 2, 3, "a", "b", "c")
for t in tupla4:
    print(t, "", end="")        # 1 2 3 a b c

print("\n", end="")

# Asignar el valor de una tupla de N elementos a N variables
tupla5 = (-15, -16.5, -150)
x, y, z = tupla5
print(x, y, z)      # -15 -16.5 -150

# Métodos de la clase tuple
# index(obj) -> devuelve el indice de un elemento    index(obj,indice) -> empieza a buscar a partir de un indice
tupla6 = (7, 7, 7, 14.8, "Fin")
print(tupla6.index(7))    # 0   Mostrará el indice del primer 7 que encuentra buscando desde el principio
print(tupla6.index(7, 2))    # 0   Mostrará el indice del primer 7 que encuentra buscando desde el 3º elemento
# print(tupla6.index(20))   # si no encuentra el elemento buscado da error
# recordáis como hacer un control de errores?
try:
    print(tupla6.index("hola"))
except Exception as e:
    print(e)

# count(obj) -> cuenta el nº de veces que obj se ha encontrado en la tupla
print("El nº 7 aparece", tupla6.count(7), "veces")                    # El nº 7 aparece 3 veces
print("La cadena 'Hola' aparece", tupla6.count("Hola"), "veces")      # La cadena "Hola" aparece 0 veces

# a pesar de su inmutabilidad, las tuplas son dinámicas  ¿?
tupla6 += (1, 2)   # añadimos dos elementos a la tupla

# len(iterable) -> cuenta el nº de elementos de la tupla
print("tupla6 tiene %d elementos" % (len(tupla6)))                    # tupla6 tiene 7 elementos
