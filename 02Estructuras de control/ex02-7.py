"""
LIST COMPREHENSION
Las list comprehension (comprensión de listas) es un tipo de Idiomatic Expression (expresión ideomática
que nos brinda Python para hacer lo mismo escribiendo menos código. Permite crear iterables

        Sintaxis de una list Comprehension ->  lista = [expresión for elemento in iterable]
        - for elemento in iterable -> recorre un iterable almacenando sus valores en elemento
        - expresión -> es el valor que se añade al iterable que crearemos
"""

# Haremos una lista con el cuadrado de los cinco primeros nº naturales
# 1º Caso: Forma tradicional
cuadrados = []         # definimos una lista vacía
for i in range(5):     # i toma valores de rango 0..4
    cuadrados.append(i**2)  # el i^2 se añade con append() al final de la lista
print(cuadrados)       # Se imprime la lista  [0, 1, 4, 9, 16]

# 2º Caso: usando List Comprenhensions
cuadrados = [i**2 for i in range(5)]    # i toma los valores del rango 0..4, después i^2 se almacena en la lista
print(cuadrados)       # Se imprime la lista  [0, 1, 4, 9, 16]

# El caso anterior tb se puede hacer utilizando funciones


def cuad(p1):
    return p1**2


cuadrados = [cuad(i) for i in range(5)]   # i = 0..4, Después llamamos a la funcion cuad(i)
print(cuadrados)

# rellenar una lista con 5 cadenas iguales
nombres = ["Sonia" for i in range(5)]
print(nombres)     # ['Sonia', 'Sonia', 'Sonia', 'Sonia', 'Sonia']

# En los ejemplos anteriores hemos iterado el iterable rango. En el siguiente ejemplo
# iteraremos una lista
lista1 = [10, 20, 30, 40, 50]
print(lista1)  # [10, 20, 30, 40, 50]
lista2 = [int(i/10) for i in lista1]
print(lista2)  # [1, 2, 3, 4, 5]

# AÑADIENDO CONDICIONALES
"""
 Sintaxis de una list Comprehension ->  lista = [expresión for elemento in iterable if condicion]
        - for elemento in iterable -> recorre un iterable almacenando sus valores en elemento
        - expresión -> es el valor que se almacenará en el iterable que crearemos
        - if condición -> si es verdadera, almacenamos el valor de expresión
"""
# vamos a crear una lista con una determinada letra que aparezca en un cadena
frase = "En un lugar de la Macha de cuyo nombre no quiero acordarme"
letras = [i for i in frase if i == "e"]
print(letras)        # mostramos la lista de letras creada
print("El nº de letras encontradas es:", len(letras))   # obtenemos la longitud o nº de elementos de la lista

# SETS COMPREHENSIONS Son similares a las listas, pero no permiten añadir más de un elemento igual. No dará error,
# pero no se añadiran

frase = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
set_letras = {i for i in frase if i == "e"}
print(set_letras)        # mostramos el set de letras creado, en este caso concreto, de solamente una letra

# observa como el set no almacena más de un elemento igual
lista_f = ["a", "m", "p", "a", "r", "a", "r", 10, 10, 15, 16]   # creamos una lista de elementos heterogeneos
print(lista_f)
set_f = {"a", "m", "p", "a", "r", "a", "r", 10, 10, 15, 16}   # creamos un set de elementos heterogeneos
print(set_f)

# DICTIONARY COMPREHEMSIONS -> Vamos a crear un diccionario a partir de 2 listas
keys = ['nombre', 'edad', 'región']     # lista de cadenas
datos = ['Pelayo', 30, 'Asturias']      # lista heterogenera

# zip genera las tuplas ('nombre', 'Pelayo') ('edad', 30) ('región', 'Asturias')
# con el for recorremos cada tuplas almacenando sus elementos en i y j
# con la expresión i:j asinamos un valor a un key
mi_dict = {i: j for i, j in zip(keys, datos)}
print(mi_dict)   # {'nombre': 'Pelayo', 'edad': 30, 'región': 'Asturias'}
