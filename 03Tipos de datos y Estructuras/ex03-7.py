"""
CASTING

Cast o casting es convertir de un tipo de datos a otro. Existen 2 tipos de casting:
a) conversión implícita -> se realiza automáticamente al realizar operaciones con elementos de distinto tipo
b) conversión explícita -> la realidad el programador a voluntad. Ej) int(), str()

ES MUY IMPORTANTE SABER CON QUE TIPO DE DATO O ESTRUCTURA DE DATOS TRABAJAMOS EN CADA MOMENTO.
Ante la duda usar la funcion type() siempre
"""

# Ejemplo de conversión implícita
a = 1
b = 2.3
print(a, type(a), b, type(b))   # 1 <class 'int'> 2.3 <class 'float'>
a = a + b
print(a, type(a))    # 3.3 <class 'float'>

# No en todos los casos podrá realizarse la conversión implícita y dará un error
a = 1
b = "2.3"
# c = a + b   # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# FUNCIONES MAS USADAS EN LA CONVERSIÓN EXPLÍCITA
# int(real) / int(cadena) -> convierte un float a int. Se perderá la parte decimal / cadena con formato numerico
num1 = 13.5
cad1 = "1256"
ent1 = int(num1)
ent2 = int(cad1)
print(num1, type(num1), cad1, type(cad1), ent1, type(ent1), ent2, type(ent2))

# str(real) / str(int) -> convierte a cadena un real o un entero
num1 = 345.75
num2 = -56
cad1 = str(num1)
cad2 = str(num2)
print(num1, type(num1), num2, type(num2), cad1, type(cad1), cad2, type(cad2))

# float(cadena) / float(entero) -> convierte a real una cadena con formato numerico o un entero
cad1 = "-1267.67"
num1 = 89
real1 = float(cad1)
real2 = float(num1)
print(cad1, type(cad1), num1, type(num1), real1, type(real1), real2, type(real2))

# list(iterable) -> ya hemos visto que convierte a lista cualquier iterable
cadena = "Programación"
tupla = (1, 2, 3)
miset = {4, 5, 6}
midict = {1: "a", 2: "b", 3: "c"}
lista1 = list(cadena)
lista2 = list(tupla)
lista3 = list(miset)
lista4 = list(midict)
print(lista1, lista2, lista3, lista4)
"""
MUTABILIDAD
Python es un lenguaje orientado a objeto. Las variables, las estructuras de datos, las funciones... 
Los objetos son instancias (copias) de una determinada clase, de la cuál heredan 
sus propiedades (variables) y sus métodos (funciones)

Un objeto viene determinado por estas características:
 a) identidad -> es un identificador numérico unívoco, que nunca cambia DENTRO DE LA MISMA EJECUCIÓN. 
    Funcion id(obj)  ESTA CARACTERISTICA NOS AYUDA A VER LA MUTABILIDAD DE UN OBJETO
 b) Clase -> grupo al que pertenece el objeto. Podemos saberlo con la función type(obj)
 c) Valor -> se puede modificar (objeto mutable)    no se puede modificar (objeto inmutable)

Clasificación de los objetos según su mutabilidad
- Objetos mutables: listas, sets, diccionarios, clases definidas por el usuario ... 
  NOTA: Existen más como Bytearray, memoryview que no se tratarán en este curso
  
- Objetos inmutables: enteros, reales, complejos, booleanos, cadenas, rango, 
  tuplas, frozesets ...  
  
OJO: IMPORTANTE -> Es primordial manejar muy bien el concepto MUTABILIDAD,
ya que Python trata de forma distinta a un objeto mutable que a uno inmutable.
Por ejemplo: en el paso por valor / paso por referencia de las funciones

Cuando pasamos parámetros en la llamada a una función, hay dos formas de pasarlos:
a) paso por valor -> se pasa sólo el valor del objeto. Por tanto, aunque lo cambiemos dentro
                     de la función, el objeto original no cambiará su valor
b) paso por referencia -> se pasa un puntero (la dirección de memoria del objeto original)
                          Por tanto ojo que los cambios dentro de la función le afectarán
Pues bien... Python por defecto:
- los objetos inmutables se pasan por valor
- los objetos mutables se pasan por referencia

"""
# comprobar la identidad, clase y valor de un nº entero
x = 10
print("Identidad:", id(x))   # Identidad: 2531038265872   (cambiará en distintas ejecuciones)
print("Tipo:", type(x))      # Tipo: <class 'int'>
print("Value:", x)           # Value: 10

# Un objeto entero es inmutable. Y alguien dirá: "Pero si se puede cambiar el valor de una variable entera..."
# Efectivamente, pero el sistema nos engaña. En realidad crea otro objeto con el mismo nombre al que asigna
# el nuevo valor. Observad...
x = 6
print("Identidad:", id(x))   # Identidad: 1908837253520   (cambiará en distintas ejecuciones)
print("Tipo:", type(x))      # Tipo: <class 'int'>
print("Value:", x)           # Value: 6

# Sin embargo, una lista es un objeto mutable y lo vamos a demostrar a continuación
listaC = [1, 2, 3]
print("Identidad:", id(listaC))   # Identidad: 3144067085568  (cambiará en distintas ejecuciones)
print("Tipo:", type(listaC))      # Tipo: <class 'list'>
print("Value:", listaC)           # Value: [1, 2, 3]
listaC[0] = -15
print("Identidad:", id(listaC))   # Identidad: 3144067085568   (cambiará en distintas ejecuciones)
print("Tipo:", type(listaC))      # Tipo: <class 'list'>
print("Value:", listaC)           # Value: [-15, 2, 3]

# una tupla es inmutable también. Fijaros que ocurre...
tuplaB = (-100, -200, -300)
print("Identidad:", id(tuplaB))   # Identidad: 3144067085568  (cambiará en distintas ejecuciones)
print("Tipo:", type(tuplaB))      # Tipo: <class 'tuple'>
print("Value:", tuplaB)           # Value: (-100, -200, -300)
# tuplaB[1] = 14   # Este código ya da un error pq es inmutable

# Cómo podríamos modificar una tupla?. Fácil, convirtiéndola a lista, modificándola, y volviendola a convertir
# en tupla, pero OJO, la tupla original se habrá destruido.
tuplaB = (-100, -200, -300)
print("Identidad:", id(tuplaB))   # Identidad: 3144067085568  (cambiará en distintas ejecuciones)
print("Tipo:", type(tuplaB))      # Tipo: <class 'tuple'>
print("Value:", tuplaB)           # Value: (-100, -200, -300)
listaB = list(tuplaB)             # convertimos la tuplaB en lista
listaB[1] = 1000                  # modificamos un elemento de la lista
tuplaB = tuple(listaB)
print("Identidad:", id(tuplaB))   # Identidad: 3144067085568  (cambiará en distintas ejecuciones)
print("Tipo:", type(tuplaB))      # Tipo: <class 'tuple'>
print("Value:", tuplaB)           # Value: (-100, -200, -300)

# comprobación práctica del paso por valor y referencia y la IMPORTANCIA DE LA MUTABILIDAD


def funcion(p1, p2):
    p1 = 25       # no modificará el valor de x
    p2[0] = 10    # modificará el valor de y[0]
    p2.append("Adios")


x = 5    # x es un objeto de clase int. Por tanto inmutable
y = [5]  # y es un objeto de clase list. Por tanto mutable
print("x =", x, "y =", y)
funcion(x, y)
print("x =", x, "y =", y)
