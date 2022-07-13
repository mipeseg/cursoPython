"""
TIPOS DE ESTRUCTURA DE DATOS: LISTAS ( Si venimos de otros lenguajes, es algo parecido a un array o vector

  Es un tipo de estructura de datos con las siguientes características:

  a) Permite almacenar un grupo de datos (homogéneo o heterogéneo)
  b) Mutables (Sus elementos pueden ser modificados)
  c) Dinámicas (En tiempo de ejecución podemos cambiarlas: modificar, añadir o eliminar elementos)
  d) Ordenadas (los elementos mantienen el orden en el que fueron creados)
  e) Indexables mediante indice ( lista[i])
  f) Anidables ( podemos encontrar listas dentro de otros)

"""
# Creación de listas
lista1 = ["Maria", "Oscar", "Sandra"]
lista2 = list("1234abc")   # mediante la función list(objeto_iterable)
print(lista1, type(lista1))
print(lista2, type(lista2))

# Acceso y modificación de listas
a = [90, "Python", 3.87]
print(a[0], a[1], a[2])      # Acceso mediante índice             90 Python 3.87
print(a[-1], a[-2], a[-3])   # Acceso invertido mediante índice   3.87 Python 90
# print(a[3])                # Error por índice fuera de rango
# modificacion de un elemento
a[0] = -4
print(a)

# eliminar elemento de una lista
del a[1]    # borramos el segundo elemento de la lista a -> [-4, 'Python', 3.87]
print(a)    # [-4, 3.87]

# listas anidadas
x = [45, -23, 33, ['p', 'r', [5, 6, 7]]]     # el 4º elemento de x es una lista cuyo 3º elemento es otra lista
print(x[3][0], x[3][2][0], x[3][2][2])       # p 5 7
print(x[3], "####", x[3][2])                 # ['p', 'r', [5, 6, 7]] #### [5, 6, 7]

# creación de una sublista     elemento inicial : elemento final q no se incluirá
lista3 = [400, 500, 600, 700, 800, 900]
sublist1 = lista3[0:2]        # [400, 500]
sublist2 = lista3[2:5]        # [600, 700, 800]
sublist3 = lista3[3:20]       # [700, 800, 900]
print(sublist1, sublist2, sublist3)

# modificación de multiples valores
lista3[0] = "sold"                 # ['sold', 500, 600, 700, 800, 900]
print(lista3)
lista3[2:4] = ["sold", 701]     # ['sold', 500, 'sold', 701, 800, 900]
print(lista3)

# añadir elementos a una lista
listaB = [140, 150, 160, 170, 180]
listaB.append(190)    # mediante el metodo append añadimos un elemento al final de la lista
print(listaB)
listaB += [200, 210]            # mediante el operador +=
listaB = listaB + [220, 230]
print(listaB)

# asignar una lista de N elementos a N variables
precios = [1250, 3200, 215]
pvp1, pvp2, pvp3 = precios
print(pvp1, pvp2, pvp3)

# iterar o recorrer una lista
print("Los precios son: ", end="")
for pvp in precios:
    print(pvp, "", end="")

print("\n", end="")   # salto manual y evitar el automático

# iterar o recorrer una lista mostrando el indice de los elementos
print("Los precios son: ", end="")
for index, pvp in enumerate(precios):
    print(index, "-", pvp, "", end="")

print("\n", end="")   # salto manual y evitar el automático

# iterar dos listas a la vez
codigos = [2001, 3027, 4567]
productos = ["PlayStation 5", "Nintendo Switch OLED", "SoundBlaster X7"]
codigosYproductos = []   # definimos una lista vacia
for l1, l2 in zip(codigos, productos):
    codigosYproductos += [[l1, l2]]  # rellenamos la lista con listas [codigo, producto]
print(codigosYproductos)
print("El código del producto %s es %d" % (codigosYproductos[0][1], codigosYproductos[0][0]))
for i in range(3):
    for j in range(1):
        print("El código del producto %s es %d" % (codigosYproductos[i][j+1], codigosYproductos[i][j]))

# métodos de la clase lista
# append(obj) -> permite añadir un elemento al final de la lista
# extend(iterable) -> permite añadir un iterable a la lista
# insert(indice, obj) -> añade un elemento en la posición de la lista indica por el indice
# remove(obj) -> borra de la lista el elemento indicado. OJO: Sólo borra la primera coincidencia
#                Si no lo encuentra en la lista, da un error
# pop( ) -> elimina el último elemento de la lista   pop(indice) -> elimina el elemento que indica el indice
# reverse(obj) -> invierte los elementos de la lista
# sort( ) -> ordena los elementos de menor a mayor  sort(reverse=True) -> ordena los elementos de mayor a menor
# index(obj) -> devuelve el indice de un elemento    index(obj,indice) -> empieza a buscar a partir de un indice
# count(obj) -> cuenta el nº de veces que obj se ha encontrado en la lista

ultima = [25, "rosa", 50, 75, "rojo"]
ultima.append(1245)             # [25, 'rosa', 50, 75, 'rojo', 1245]
ultima.extend([-5, -8])         # [25, 'rosa', 50, 75, 'rojo', 1245, -5, -8]
ultima.insert(2, "rojo")        # [25, 'rosa', 'rojo', 50, 75, 'rojo', 1245, -5, -8]
ultima.remove("rojo")           # [25, 'rosa', 50, 75, 'rojo', 1245, -5, -8]
ultima.pop()                    # [25, 'rosa', 50, 75, 'rojo', 1245, -5]
ultima.pop(1)                   # [25, 50, 75, 'rojo', 1245, -5]
ultima.reverse()                # [-5, 1245, 'rojo', 75, 50, 25]
print(ultima)
print(ultima.index("rojo"))
ultima[ultima.index("rojo")] = 100   # [-5, 1245, 100, 75, 50, 25]    cambiamos rojo para que no de sort() error
ultima.sort()                        # [-5, 25, 50, 75, 100, 1245]
print(ultima)
ultima.sort(reverse=True)            # [1245, 100, 75, 50, 25, -5]
print(ultima)
print(ultima.count("hola"))
