"""
FUNCIONES DEFINIDAS POR EL USUARIO
Desde que empezamos el curso hemos estado usando funciones nativas de Python. Ej: len(), bin(), list()....
Un lenguaje de programación debe permitir al usuario crear sus propias funciones:

    def nombreFuncion(p1,p2...p3):   los parametros de entrada son opcionales
        ....
        ....
        return ....    # OJO: los parámetros de salida también son opcionales

Con lo visto hasta ahora decimos que Python (y los lenguajes de programación modernos) siguen tres principios
básicos:

 a) lenguaje estructurado
    el flujo de ejecución del código se maneja a voluntad con las estructuras de control (if, for, while...)
 b) lenguaje modular
    "Divide y vencerás" -> Para resolver un problema codificamos un algoritmo. Si es un problema largo, mejor
                           dividirlo en subproblemas y codificar funciones o modulos que den solución específica
                           a cada uno de los problemas.  VENTAJAS: El código es más legible, los errores se
                           encuentran más facilmente, mejora la reusabilidad del código

 c) lenguaje reusable -> Si en otro momento necesitamos resolver el mismo problema, podemos reutilizar o llamar
                         a una función que tenemos programada y lo resuelve, en lugar de volverla a escribir.
                         Además si en un programa se repite varias veces el mismo código, deberíamos de integrarlo
                         en una función y llamarla cada vez que la necesitemos.
"""

# EJEMPLOS
# Función sin argumentos de entrada ni de salida


def saludo_grupal():
    print("Hola a todos")  # Hola a todos


saludo_grupal()


# Función con argumentos de entrada

def saludo_personal(nombre):
    print("Hola", nombre)


saludo_personal("Marcos")   # Hola Marcos

"""
AL llamar a una función, podemos pasarle parámetros de entrada de tres formas:
a) por posición -> los valores se asignan por posición. El nº de parámetros posicionales deber ser
                   fijo, pq sino al llamar a la función dará error
b) por nombre -> en la llamada indicamos nombreArg = valor. El nº de parámetros nominales deber ser
                   fijo, pq sino al llamar a la función dará error
c) por defecto -> cuando nos interesa programar una función con parámetros opcionales. Cuando un 
                  parámetro opcional no recibe valor de entrada, usa un por default
"""

# Paso de argumentos por posición y por nombre


def resta(a, b):
    return a-b


print(resta(5, 3))            # 2  Paso de parámetros por posición
# print(resta(5))             #    TypeError: resta() missing 1 required positional argument: 'b'
print(resta(b=-1, a=15))      # 16 Paso de parámetros por nombre
# print(resta(b=-1))            #    TypeError: resta() missing 1 required positional argument: 'a'

# Paso de argumentos opcionales


def suma(a, b=5, c=0):    # a es un parámetro de entrada fijo   b y c son parámetro de entrada opcionales
    return a+b+c


# print(suma())       # TypeError: suma() missing 1 required positional argument: 'a'
print(suma(6))        # 11
print(suma(6, 1))     # 7
print(suma(6, 1, 2))  # 9
print(suma(6, c=20))  # 31   Combinación de paso por posición, opcional y por nombre

"""
Hasta ahora hemos visto funciones con un nº máximo de parámetros. Y si necesitamos una función con un
nº de argumentos que ni el programador conozca a priori? -> FUNCIONES DE PARAMETROS VARIABLES
"""

# funciones con parámetros variables


def suma2(*numeros):    # el * hace que el valor/es que se pasa/n se empaquete/n en una tupla
    print(numeros, type(numeros))  # (1, 3, 5, 7) <class 'tuple'>
    total = 0
    for n in numeros:
        total += n
    return total


print(suma2(1, 3, 5, 7))  # 16

# también podemos pasar a una función un conjunto de elementos key=value


def suma3(**dic):   # el ** hace que el valor/es que se pasa/n se empaquete/n en un diccionario
    print(dic, type(dic))   # {'a': 5, 'b': 20, 'c': 23} <class 'dict'>
    s = 0
    for key, value in dic.items():
        # print(key, value)
        s += value
    return s


print(suma3(a=5, b=20, c=23))   # 48
di = {'a': 10, 'b': 20}         # Podemos pasarle tb un diccionario
print(suma3(**di))              # 30  OJO, pasamos a la función la referencia a di. No el diccionario

# Sumar numeros que introduce el usuario por teclado


def suma4(*numeros):    # el * hace que el valor/es que se pasa/n se empaquete/n en una tupla
    print(numeros, type(numeros))  # ('?', ',', '?', ...) <class 'tuple'>
    total = 0
    for n in numeros:
        if n != " " and n != ",":
            try:
                total += int(n)
            except Exception as e:
                return e
    return total


print("Introduce valores entre 0 y 9, separados por coma: ", end="")   # 1,2,3  1, 2,3
s1 = input()        # Lo que se introduce por teclado siempre es una cadena de caracteres   "4,5"
t = tuple(s1)       # ('4',',','5')
print(suma4(*t))   # a la función suma4 le pasamos una referencia a la tupla t

# función que devuelve varios valores


def suma_y_media(a, b, c):
    """ Documentacion de la funcion """
    z = a+b+c
    media = z/3
    return z, media


print()

var1, var2 = suma_y_media(9, 6, 3)
print(var1)  # 18
print(var2)  # 6.0

# Documentación de una función
help(suma_y_media)  # nos muestra el nombre, los parámetros y los comentarios entre """ ...  """
print(suma_y_media.__doc__)  # muestra los comentarios entre """ ... """

"""
PASO POR VALOR Y PASO POR REFERENCIA (RECORDATORIO)

Cuando vimos mutabilidad de los objetos (3.7), dijimos ...

Cuando pasamos parámetros en la llamada a una función, hay dos formas de pasarlos:
a) paso por valor -> se pasa sólo el valor del objeto. Por tanto, aunque lo cambiemos dentro
                     de la función, el objeto original no cambiará su valor
b) paso por referencia -> se pasa un puntero (la dirección de memoria del objeto original)
                          Por tanto ojo que los cambios dentro de la función le afectarán

Pues bien... en Python por defecto:

 - los objetos inmutables (enteros, reales, complejos, booleanos, cadenas, rango, 
   tuplas, frozesets) se pasan por valor
 - los objetos mutables (listas, sets, diccionarios, clases definidas por el usuario) se pasan por referencia
"""

print()

# paso por valor


def funcion(p1):
    print("p1=", p1, id(p1))  # p1= 10 2219634262544   ¿?¿? no era paso por valor ¿?¿? Pq p1 y x tienen el mismo id
    p1 = 0
    print("p1=", p1, id(p1))  # p1= 0 2219634262224    Observa como al cambiar el valor es cuando se crea otro obj


x = 10
print("x=", x, id(x))  # x= 10 2219634262544
funcion(x)
print("x=", x, id(x))  # x= 10 2219634262544

# paso por referencia (observar que el id no cambia, siempre es el mismo)

print()


def funcion2(entrada):
    print("entrada=", entrada, id(entrada))   # entrada= [10, 20, 30] 2706453939648
    entrada.append(40)  # añadimos otro elemento al final de la lista
    # entrada = []   # ¿???? no borra q ??? EXPLICACIÓN: Se ha creado otra lista llamada tb entrada
    # entrada.clear()  # Ahora si que borro q
    print("entrada=", entrada, id(entrada))   # entrada= [10, 20, 30, 40] 2706453939648


q = [10, 20, 30]          # q es una lista
print("q=", q, id(q))     # [10, 20, 30] 2706453939648
funcion2(q)
print("q=", q, id(q))     # x= [10, 20, 30, 40] 2706453939648
