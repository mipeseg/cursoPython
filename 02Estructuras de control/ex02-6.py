# La funcion ZIP(iterable1,it2, ... itN) permite generar tuplas donde se combinan elemento a elemento

vehiculo = [1, 2, 3]                        # lista de numeros
marca = ["Seat", "Ford", "Renault"]         # lista de cademas
c = zip(vehiculo, marca)                    # genera tuplas de 2 elementos a las que apunta el iterador c
print(list(c))                              # Mostramos una lista de tuplas:  [(1,'Seat'),(2,'Ford'),(3,'Renault')]

# usando zip() y for podemos iterar dos listas en paralelo
vehiculo = [1, 2, 3]                          # lista de numeros
marca = ["Seat", "Ford", "Renault"]           # lista de cademas
c = zip(vehiculo, marca)                      # genera tuplas de 2 elementos a las que apunta el iterador c
for num, text in c:
    print("Vehículo:", num, "Marca:", text)

# Otro ejemplo de uso
numeros = [1, 2]
espanol = ["Uno", "Dos"]
ingles = ["One", "Two"]
frances = ["Un", "Deux"]
c = zip(numeros, espanol, ingles, frances)    # Tuplas de 4 elementos -> (1,'Uno','One','Un'), (2,'Dos','Two','Deux')]
for n, e, i, f in c:
    print(n, e, i, f)

# Si usamos iterables de distintas longitudes, zip() termina cuando se acaba el iterable de menor longitud
numeros = [11, 12, 13, 14, 15]
espanol = ["Once", "Doce"]
for n, e in zip(numeros, espanol):        # se generan tuplas de 2 elementos (11,"Once") (12,"Doce")
    print(n, e)

# Podemos usar zip() con un solo iterable de entrada para generar tuplas de 1 sólo elemento
numeros = [1, 2, 3, 4, 5]
zz = list(zip(numeros))     # zz contiene una lista de tuplas de 1 elemento  (1,),(2,),(3,),(4,),(5,)
print(zz)   # [(1,),(2,),(3,),(4,),(5,)]

# uso de zip con diccionarios
"""
Ahora no es el momento de explicar que es un diccionario. Sólo sepamos que zip() funciona con cualquier iterable, no
solo con listas y que la estructura de un diccionario es esta:
nombre_diccionario = {key:valor,key:valor....}
"""
dic_esp = {1: 'Uno', 2: 'Dos', 3: 'Tres'}
dic_eng = {'100': 'One', '200': 'Two', '300': 'Three'}
for a, b in zip(dic_esp, dic_eng):       # a y b almacenan los valores de las Keys de cada diccionario
    print(a, b)

# la funcion items() nos permite acceder al key y valor de cada elemento del diccionario
for (k1, v1), (k2, v2) in zip(dic_esp.items(), dic_eng.items()):
    print(k1, v1, k2, v2)

# zip(*Iterable) --> nos permite deshacer (* es unpacking) un iterable en los iterables iniciales
listaDeTuplas = [(1, 'One'), (2, 'Two'), (3, 'Three')]
print(listaDeTuplas, type(listaDeTuplas))
a, b = zip(*listaDeTuplas)
print(a, type(a))  # (1, 2, 3)
print(b, type(b))  # ('One', 'Two', 'Three')

# ENUMERATE(iterable) -> crea tuplas (indice, valor) de todos los elementos de un iterable
nombres = ["Andrés", "Ana", "Silvia"]
for indice, nom in enumerate(nombres):    # Enumerate() crear tuplas  (0, 'Andrés') (1, 'Ana') (2, 'Silvia')
    print(indice, nom)
listTuplas = list(enumerate(nombres))  # también podemos crear una lista de tuplas (indice,valor)
print(listTuplas)
print(type(enumerate(nombres)))
