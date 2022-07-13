"""
TIPOS DE ESTRUCTURA DE DATOS: DICCIONARIO

  Colección de elementos guardados por parejas clave:valor

  a) Permite almacenar un grupo de datos (homogéneo o heterogéneo)
  b) Dinámicos (el diccionario puede agregar elementos, eliminarlos, etc)
  c) Se pueden anidar diccionarios
  e) INDEXABLES (los elementos son accesibles a través de su Key
"""

# Creación de un diccionario
d1 = {"Nombre": "Sara", "Edad": 27, "DNI": "100388289K"}   # 1º forma
d2 = dict([("Nombre", "Luis"), ("Edad", 14), ("DNI", "509039725T")])  # usando la funcion dict()
d3 = dict(Nombre='Ana', Edad=70, DNI="10003882J")  # usando el constructor dict()
print(d1, type(d1))  # {'Nombre': 'Sara', 'Edad': 27, 'DNI': '100388289K'} <class 'dict'>
print(d2, type(d2))  # {'Nombre': 'Luis', 'Edad': 14, 'DNI': '509039725T'} <class 'dict'>
print(d3, type(d3))  # {'Nombre': 'Ana', 'Edad': 70, 'DNI': '10003882J'} <class 'dict'>

# Acceder a los elementos del diccionario
print(d1["Nombre"], d1.get("Nombre"))       # Mostrar un elemento de 2 formas  -> Sara Sara

# Modificar un elemento
d1["Edad"] = 28
print(d1)     # {'Nombre': 'Sara', 'Edad': 28, 'DNI': '100388289K'}

# Añadir elementos al final del diccionario -> si la key no existe se crea al final. Si existe modifica su valor
d2["Dirección"] = "No consta"
print(d2)

# Iterar un diccionario
# Acceder a las keys las keys
for x in d1:
    print(x, "", end="")

print("\n", end="")     # salto manual de línea y evitamos el automático

# Acceder a los valores
for x in d1:
    print(d1[x], "", end="")

print("\n", end="")     # salto manual de línea y evitamos el automático

# Acceder a keys y valores
for x, y in d1.items():
    print(x, ":", y, "### ", end="")

print("\n", end="")     # salto manual de línea y evitamos el automático

# diccionarios anidados
d5 = {"a": 1, "b": 2}
d6 = {"c": 3, "d": 4}
d7 = {
  "anidado1": d5,
  "anidado2": d6
}
print(d7)  # {'anidado1': {'a': 1, 'b': 2}, 'anidado2': {'c': 3, 'd': 4}}
print(d7["anidado1"])  # {'a': 1, 'b': 2}
print(d7["anidado2"]["d"])  # 4

# MÉTODOS DE LOS DICCIONARIOS
# clear() -> elimina el contenido del diccionario
d7.clear()
print(d7)  # {}

# get(key,Default) -> devuelve el valor asociado a una key. Si no se encuentra la clave, devuelve
# el valor por defecto
d6 = {"codigo": 100, "nombre": "Alberto"}
print(d6.get("codigo"))  # 100
print(d6.get("dirección", "Clave no encontrada"))  # Clave no encontrada

# items() -> devuelve un objeto dic_items que es una lista de tuplas (key,value)
#            con todos los elementos del diccionario. Debe de convertirse a lista pura con list() para poder acceder
d7 = {"a": 1, "b": 2}
obj_dic_items = d7.items()
lista = list(obj_dic_items)
print(obj_dic_items)           # dict_items([('a', 1), ('b', 2)])
print(lista)                   # [('a', 1), ('b', 2)]
print(lista[0][0])             # a

# keys() -> devuelve un objeto dict_keys, que es lista con todas las claves del diccionario. Debe convertirse
#           a list pura con list() para poder acceder
d8 = {'a': 1, 'b': 2}
obj_dict_keys = d8.keys()
claves = list(obj_dict_keys)
print(obj_dict_keys)       # dict_keys(['a', 'b'])
print(claves)               # ['a', 'b']
print(claves[1])            # b

# values() -> devuelve un objeto dict_values, que es lista con todas los valores del diccionario. Debe convertirse
#           a list pura con list() para poder acceder
obj_dict_values = d8.values()
valores = list(obj_dict_values)
print(obj_dict_values)        # dict_values([1, 2])
print(valores)                # [1, 2]
print(valores[1])             # 2

# pop(key,Default) -> busca y elimina la key y su valor asociado. Si no se encuentra devuelve el valor default
d9 = {'a': 1, 'b': 2}
print(d9)                              # {'a': 1, 'b': 2}
if d9.pop("a", -1) != -1:
    print(d9, "Elemento borrado")      # {'b': 2} Elemento borrado
else:
    print(d9, "Clave no encontrada")

# popitem( ) -> elimina el último elemento del diccionario
d10 = {"inicio": 100, "fin": 200}
print(d10)
d10.popitem()
print(d10)

# dic1.update(dic2) -> actualiza aquellos valores de dic1 con los valores de dic2 que tengan la misma clave
# si alguna clave de dic2 no está en dic, se añade la pareja clave:valor
d11 = {"a": 1, "b": 2}
d12 = {"a": 0, "d": 400}
print(d11)             # {'a': 2, 'b': 2}
d11.update(d12)
print(d11)             # {'a': 0, 'b': 2, 'd': 400}
