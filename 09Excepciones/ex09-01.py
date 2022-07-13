"""
EXCEPCIONES
Una excepción es una situación excepcional e imprevista provocada por una operación no permitida y
que produce un error que puede detener la ejecución normal del programa. Por ello, en Python y
en cualquier otro lenguaje, es necesario controlar las excepciones que puedan ocurrir

Listado de excepciones en Python -> https://docs.python.org/3/library/exceptions.html

Una excepción se puede lanzar de varias formas:
a) automáticamente -> Python lanza una excepción cuando se produce una operación no permitida
b) manualmente -> El programador usando  raise nombreExcepcion("info detallada")
c) excepciones definidas por el usuario (LO VEMOS MAS ADELANTE)

"""
# Lanzar excepciones manualmente con raise()
# raise ZeroDivisionError  # lanza la excepción ZeroDivisionError y detiene la ejecución normal del programa
# raise NameError("No encuentra un nombre")  # lanza la excepción NameError y detiene la ejecución

# Dividir por 0 matemáticamente es una indefinición, pero en programación provoca
# la excepción ZeroDivisionError. Como programadores podemos controlar el código para
# que esto no ocurra, pero no sería un control de excepciones

a = 5
b = 1          # La division por 0 está controlada. Pero y si b = "dkjdjkd"? Se produce la excepción TypeError
if b != 0:
    print(a/b)
else:
    print("División por cero")

# Por tanto como es muy complicado escribir un código que prevenga los numerosos errores, lo mejor es capturalos
# y controlarlos cuando se produzcan en tiempo de ejecución. Un verdadero control de excepciones sería este:

c = 5.2
d = 0
try:                      # en el bloque try se coloca el código que puede provocar las excepciones
    print(c/d)
except Exception as e:    # en el bloque except entramos si se produce cualquier excepción. No se detiene la ejecuión
    print(e, type(e))     # Todas las excepciones heredan de la clase Exception

# Otra forma sería controlar cada excepción por separado. A veces se utiliza para tomar decisiones diferentes
# OBSERVA: Si se produce una excepción no controlada se detendrá la ejecución del programa

e = 5
f = 2
try:                               # en el bloque try se coloca el código que puede provocar las excepciones
    print(e/f)
except ZeroDivisionError:          # entramos si se produce una excepción de clase ZeroDivisionError
    print("No se puede dividir por cero")
except TypeError:                  # entramos si se produce una excepción de clase TypeError
    print("Conflicto de tipos")

# try - else - except -> en el bloque else se entra si no se produce ninguna excepción

g = 12
h = 4
try:                               # en el bloque try se coloca el código que puede provocar las excepciones
    print(g/h)
except Exception as e:             # entramos si se produce cualquier excepcion
    print(e, type(e))
else:                              # entramos si no se produce ninguna excepción
    print("Todo correcto!")

print()

# try - else - except - finally -> en el bloque finally entramos siempre

i = 20
j = 5
try:                               # en el bloque try se coloca el código que puede provocar las excepciones
    print(i/j)
except Exception as e:             # entramos si se produce cualquier excepcion
    print(e, type(e))
else:                              # entramos si no se produce ninguna excepción
    print("Todo correcto!")
finally:                           # entramos siempre
    print("Fin del control de errores")

print()

# control de excepciones al trabajar con ficheros

try:                               # en el bloque try se coloca el código que puede provocar las excepciones
    fichero = open('ejemplo.txt', "r")
except Exception as e:             # entramos si se produce cualquier excepcion
    print(e, type(e))
else:                              # entramos si no se produce ninguna excepción
    print("Fichero abierto para lectura")
finally:                           # entramos siempre
    print("Fin del control de errores")
