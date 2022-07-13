# PALABRAS RESERVADAS en Python (recordemos que podemos listarlas con las siguientes instrucciones)
import keyword
import time

print(keyword.kwlist)

# Vamos a explicarlas a continuación

# CONDICIONALES: IF, ELIF, ELSE    (permiten alterar el flujo lineal del código según una condición)
lenguaje = "Python"

if lenguaje == "Python":
    print("Python fue desarrollado por Guido Van Rossum")
elif lenguaje == "C":
    print("C fue desarrollado por Dennis Ritchie")
elif lenguaje == "Java":
    print("Java fue desarrollado por James Gosling")
else:
    print("No estamos hablando de Python, C o Java")

# BUCLES: WHILE, FOR (permiten repetir un cjto de instrucciones x veces)    break, continue (alteran el bucle)
x = 10
while x < 30:
    print(x)   # Salida: 10, 20
    x += 10  # x = x + 10

for i in range(3):
    print(i)   # Salida: 0, 1, 2

for i in range(3):
    if i == 1:
        continue  # termina la iteracción pero continua el bucle     salida: 0, 2
    print(i)

x = 5
while True:
    print(x, "", end="")   # Salida: 5, 6, 7    end="" evita el salto de línea
    if x == 7:
        break
    x += 1

print("\n", end="")    # \n salto de linea manual   end="" evita el salto de línea automático

# VALORES: FALSE, TRUE  (booleanos)   NONE (valor nulo)
x = (5 > 1)
print(x)    # Salida: True


def funcion1():
    pass  # Instruccion vacía. Salta a la siguiente. Ej) Evita el error en una función vacia


print(funcion1())   # Salida: None

# OPERADORES LÓGICOS: AND, OR, NOT   (actuan sobre valores booleanos)

print(True and True)   # 0*0=0  0*1=0  1*0=0  1*1=1
print(False or False)   # 0+0=0  0+1=1  1+0=1  1+1=1
f = False
print(not f)   # invierte el valor de f

# FUNCIONES: DEF, RETURN, LAMBDA, PASS, YIELD
# def -> permite definir una función


def suma1(p1, p2):
    print("La suma es", p1+p2)


suma1(-7, 6)  # Salida: La suma es -1

# return -> permite que la función devuelva un valor


def suma2(p1, p2):
    return p1+p2


print("La suma es", suma2(14, 9))  # Salida: La suma es 23

# lambda -> permite definir una función lambda, sin nombre o anónima
print("La suma es", (lambda num1, num2: num1 + num2)(9, 3))    # Salida: La suma es 12

# pass -> instrucción vacía. Se usa en funciones, en estructuras de control, en clases ....


def resta():
    pass


# yield -> palabra reservada asocidada a generadores y corrutinas. Ya lo veremos con calma
def generador():
    n = 2
    yield n
    n += 1
    yield n
    n += 1
    yield n


for i in generador():
    print(i, "", end="")   # Salida: 2, 3, 4

print("\n", end="")  # salto de linea manual y evitamos el salto de linea automático


# CLASES: CLASS
# Una clase es un tipo de estructura de datos que permite definir un objeto con sus funciones (metodos)
# y variables (propiedades o atributos)
class Persona:

    @staticmethod
    def saludar():
        print("Hola")

    @staticmethod
    def despedir():
        print("Adiós")

    @staticmethod
    def sumar(a, b):
        return a+b


pedro = Persona()           # Pedro es un objeto de tipo Persona
pedro.saludar()             # Salida: Hola
print(pedro.sumar(5, 7))    # Salida: 12

# EXCEPCIONES: ASSERT, TRY, EXCEPT, FINALLY, RAISE  (relacionadas con las excepciones o situaciones inesperadas)
x = "hola mundo"
valor = None

try:
    valor = int(x)
    print("El doble del valor es", valor * 2)  # Salida: El doble del valor es 200
except Exception as e:
    print("Se produjo el error:", e)

# VARIABLES: GLOBAL, NONLOCAL
r = 0   # variable global


def incremento():
    global r   # avisamos a python que r es una variable global
    r = r + 1


incremento()
print(r)   # Salida: 1

# NONLOCAL  (indica que una variable no es local, sino que está definida en un ámbito anterior


def funcion_a():
    kg = 10

    def funcion_b():
        # nonlocal kg
        kg = 20
        print("funcion_b", kg)

    funcion_b()
    print("funcion_a", kg)


funcion_a()

# MÓDULOS: FROM, IMPORT  (nos permiten importar modulos o librerias, tanto de python como desarrollas por 3º

# import keyword   #importamos el modulo Keyword
print(keyword.iskeyword("if"))  # visualizamos True si la cadena es una palabra reservada

# PERTENENCIA E IDENTIDIAD: IN, IS
# in -> permite saber si un elemento PERTENECE en una estructura iterable
lista = ["a", "b", "c"]   # creamos una estructura iterable. En este caso una lista de caracteres
if "a" in lista:
    print("a está en la lista")       # salida: a está en la lista
print("k" in lista)                   # salida: false

# is -> permite saber si un objeto apunta a otro
list1 = [11, 12]      # lista de enteros
list2 = [-1, -2, -3]  # lista de enteros
c = list2             # c apunta a list2

print("Primer elemento de List1:", list1[0])  # muestro el primer elemento de list1
print("Tercer elemento de List2:", list2[2])  # muestro el tercer elemento de list2
print("Segundo elemento de List2:", c[1])     # muestro el segundo elemento de list2
print(list2 is c)                             # True   c apunta a list2

# ELIMINAR VARIABLE: DEL    (es una forma de elimar una variable que contenga muchos datos y liberar memoria)
borrar = 10
print(borrar)
del borrar

# CONTEXT MANAGERS: WITH, AS  (se usan para manejar ficheros. Las vemos mas adelante)

# CONCURRENCIA: ASYNC, AWAIT
# La concurrencia permite ejecutar procesos paralelamente, en lugar de secuencial


# esta función es secuencial. Empieza y termina en 3 segundos
def proces_a(ident):
    print("Empieza proceso", ident)
    time.sleep(3)
    print("Termina proceso", ident)


for i in range(3):  # se lanza 3 procesos secuenciales que durarán 9 segundos en total
    proces_a(i)

# definimos una función de concurrencia paralela. Se lanza 3 procesos a la vez en paralelo. A los 3 seg terminan
import asyncio


async def proceso(id_proceso):
    print("Empieza proceso:", id_proceso)
    await asyncio.sleep(3)
    print("Termina proceso:", id_proceso)


async def main():
    await asyncio.gather(proceso(4), proceso(5), proceso(6))

asyncio.run(main())
