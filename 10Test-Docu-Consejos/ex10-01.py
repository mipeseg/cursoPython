"""
PYTHON PEP8 (https://www.python.org/dev/peps/pep-0008/)
Es una guía de convenciones estilísticas aceptadas por amplio consenso en la comunidad Python. Es decir,
son usos y buenas costumbres sintácticas del lenguaje. Como deberíamos escribir un código Python. De hecho, si os
habéis fijado, muchos de los warnings que aparecen en PyCharm son recomendaciones estilisticas, que aunque
no afectan la ejecución del programa, ayudan a que el código sea más legible

                "Un código es más veces leído que escrito" -- Guido Van Rossum

Algunas normas estilisticas se contemplan en el PEP8:

  - Líneas en blanco
     - 2 lineas en blanco por arriba y por abajo de funciones y clase
     - 1 línea en blanco entre los métodos de una clase
  - líneas demasiado largas (max 79 caracteres por línea)
  - espacios en blanco
      - espacio en blanco a izq y drecha de operadores de asignacion y relacionales  ej) x = 3  a == b
      - no dejar espacios en blanco dentro de paréntesis o corchetes  ej)  a = 2*(b+c)
      - espacio en blanco después de coma   ej) print("hola", "adios", [1, 2, 4])
  - nombres de objetos o clases
      - evitar el uso de palabras reservadas
      - evitar usar sólo el caracter l. Se puede confundir con el caracter 1  Ej) a = l+1
      - utilizar nombre explicativos  Ej) mejor usar ->  media_arimetica = [1, 2, 3]/3  que  ma = [1, 2, 3]/3
      - estilismo según el objeto o clase:
        a) variables / funciones / métodos / Módulos ->  minúsculas y _ -> media  media_aritmetica
                                                        saludar()  subir_volumen()  mi_modulo.py
        b) constantes -> mayúsculas y _ -> PI = 3.1415  MASA_TIERRA = 5.972*10**24
        c) clases -> notación Camelcase -> Persona  ClaseDePrueba
        d) paquetes -> todos minúsculas ->  import paquetegeometria
  - código indentado -> 4 espacios en blanco
  - Python 3 codifica los ficheros en UTF-8 (es uno de los formatos actuales de codificación de caracteres Unicode)

USO DE GUIONES
  a) _nombre --> convención estilistica para indicar que una variable no debería accederse desde el exterior,
                 pero se puede acceder a ella.
  b) nombre_ --> podriamos usar una palabra reservada como nombre. Ej)  def_ = 8  print_ = 9
  c) __nombre  --> hace a un atributo o método de una clase PRIVADO
  d) __nombre__ --> Se usa para definir métodos mágicos. Ej)   def __init__(self):   constructor de clase
  e) _ --> descarta una variable  Ej)   def sumayresta(a, b):
                                             return (a+b), (a-b)
                                        suma, _ = sumayresta(5, 5)

"""

"""
INTRODUCCIÓN AL DEBUGGER O DEPURADOR DE CÓDIGO

"""


def suma(num1, num2):
    return num1+num2


def factorial(n):    # 4! = 4 * 3 * 2 * 1 = 24   Recordatorio en --> 26. Funciones 4/4  10:18
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print("Esto es una prueba de uso del debugger")
a = 5
lista = [10, 20, 30, 40]
print(a, suma(5, 7))
for x in lista:
    print(x, ",", end="")

print()
print(factorial(4))
