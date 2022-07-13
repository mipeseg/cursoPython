"""
TIPOS DE DATO NUMÉRICO:  ENTERO O INT

 - type(variable) -> nos indica el tipo de datos de la variable
      ADELANTO: En realidad -> type(obj) -> nos indica la clase a la que pertenece un objeto

 - entero o int -> cjto de nº enteros (+ y -), es decir, sin parte decimal
     NOTA: En otros lenguajes existen distintos tipos según la memoria que ocupa y el rango representado,
           en Python solo hay un tipo de entero: int

 - la funcion int() -> devuelve la parte entera de un nº real, decimal o float
"""
# EJEMPLOS
# Vamos a representar un entero con un valor muy alto, según el ordenador que tengamos.
x = 250**250    # 250^250
print(x)
print(type(x))

# Almacenamos valores en distintos sistemas numéricos. Al representarlos con print() se convierten a decimal
binario = 0b100          # 0b100 = 1*2^2 + 0*2^1 + 0*2^0 = 4
hexadec = 0x17           # 0x17 = 1*16^1 + 7*16^0 = 16 + 7 = 23
octal = 0o720          # 0o720 = 7*8^2 + 2*8^1 + 0*8^0 = 448 + 16 + 0 = 464
print(binario, type(binario))  # 4 <class 'int'>
print(hexadec, type(hexadec))  # 23 <class 'int'>
print(octal, type(octal))  # 464 <class 'int'>

# Aunque Python puede representar numeros muy altos, este entero es demasiado largo
# para representarlo. Provoca el error OverflowError
# print(5e200**2)

# getsizeof(x) -> devuelve los bits que ocupa una variable en memoria
import sys
x = 5**10000
y = 10
print("x ocupa en memoria", sys.getsizeof(x), "bits", type(x))
print("y ocupa en memoria", sys.getsizeof(y), "bits", type(y))

# uso de la función int()
b = int(116.6)
print(b)

"""
TIPOS DE DATO NUMÉRICO:  FLOAT, REAL O DECIMAL

 - type(variable) -> nos indica el tipo de datos de la variable
      ADELANTO: En realidad -> type(obj) -> nos indica la clase a la que pertenece un objeto

 - float, real o decimal -> cjto de nº (+ y -) con parte entera y decimal
     NOTA: En otros lenguajes existen distintos tipos según la memoria que ocupa y el rango representado,
           en Python solo hay un tipo de real: float

 - la funcion float() -> convierte un entero a real. La parte decimal será .0
"""
# EJEMPLOS
# Vamos a representar un número real
r = 125.789
print(r, type(r))   # 125.789 <class 'float'>

# Ejemplo de notación científica
num1 = 2.14 * 10**-4
num2 = 2.14e-4
print(num1, num2)   # 0.00021400000000000002 0.000214
print("{:.6f}".format(num1), num2)  # podemos dar formato a num1 para tenga la misma precison que num2
print("num1 ocupa en memoria", sys.getsizeof(num1), "bits")
print("num2 ocupa en memoria", sys.getsizeof(num2), "bits")

# En python, un float al contrario que un int, si tiene un valor minimo y máximo de representación
print(sys.float_info.min)  # 2.2250738585072014e-308
print(sys.float_info.max)  # 1.7976931348623157e+308

# Que ocurre si sobrepasamos los limites minimo y máximo?
num3 = 1.7976931348623157e+309
num4 = 2.2250738585072014e-500
print(num3, num4)  # no da error. Se muestra infinito y 0.0

# Conversion de entero a real
b = float(116)
print(b)   # 116.0

"""
TIPOS DE DATO NUMÉRICO:  COMPLEX O NUMERO COMPLEJO

 - type(variable) -> nos indica el tipo de datos de la variable
      ADELANTO: En realidad -> type(obj) -> nos indica la clase a la que pertenece un objeto
 
 - Hagamos un poco de memoria de los conjuntos numéricos:
   a) enteros o naturales ->  los que no tienen parte decimal. Ej)  3, -1, 10.
   b) racionales ->  los que pueden expresarse como una fracción de enteros. Ej: 3/10, 7/9.
   c) irracionales -> los que NO pueden expresarse como una fracción de enteros. Ej) π es irracional
   d) reales -> conjunto de todos los anteriores.
   d) imaginarios -> cjto de reales acompañados de la constante i=√-1 Ej) 4i, 3.7i.
   e) complejos -> tiene dos partes: una real y otra imaginaria (i) Ej) c = 5 + 5i   d = 1.3 - 10.3i   e = 2.56i
      Usos: física, matemáticas, ingeniería ya que se pueden representar como un punto en un eje de coordenadas

  - la librería cmath (https://docs.python.org/3/library/cmath.html) permite realizar muchas 
    más operaciones con nº complejos
"""

# CREACIÓN DE UN NUMERO COMPLEJO
# 1ª forma
c = 3 + 5j
print(c, type(c))        # (3+5j)  <class 'complex'>

# 2ª forma
c = complex(3.2, 19)
print(c, type(c))        # (3+5j)  <class 'complex'>

# OPERACIONES CON Nª COMPLEJOS
a = 1 + 3j
b = 4 + 1j
print("Suma:", a+b, "Resta:", a-b, "Multiplicación:", a*b, "División:", a/b)
print(a.conjugate(), b.conjugate())  # el condujado de un complejo es la negación de su parte i   (1-3j)  (4-1j)
