"""
OPERADORES DE ASIGNACIÓN (ASSIGMENT OPERATORS)
Nos permiten almacenar un resultado en una variable (en un objeto). Hasta ahora hemos visto el operador =
Hay más variaciones:
"""

# A continuación un listado
print("OPERADORES DE ASIGNACIÓN")
print("a = b    Operador asignación")              # asignación
print("a += b   Operador suma asignación")         # asignación con operadores aritméticos
print("a -= b   Operador resta asignación")
print("a *= b   Operador producto asignación")
print("a /= b   Operador división asignación")
print("a %= b   Operador módulo asignación")
print("a //= b  Operador división entera asignación")
print("a **= b  Operador exponente asignación")
print("a &= b   Operador AND asignación")          # asignación con operadores lógicos
print("a |= b   Operador OR asignación")
print("a ^= b   Operador XOR asignación")
print("a >>= b  Operador movimiento derecha asignación")    # asignación con operadores a nivel de bit
print("a >>= b  Operador movimiento izquierda asignación")

# EJEMPLOS DEL OPERADOR ASIGNACIÓN =

# Una simple asignación que venimos practicando desde el comienzo del curso.
x = 5.4     # el valor literal de la derecha, se almacena en la variable definida en la parte izquierda

# La asignación, a veces, es más compleja de lo que aparenta
a = [1, 2, 3]    # declaramos e inicializamos la lista a
b = a            # declaramos e inicializamos la lista b ¿? Seguro q b es una lista
b += [4]         # b = b + [4]    Añadimos una lista literal al final de la lista b  ¿? Seguro
# b es una lista?. b es un puntero que apunta hacia a. Recordemos que las lista son mutables, y
# por tanto se pasan por referencia. Lo podemos comprobar con la funcion id()
print(b, type(b), id(b))         # [1, 2, 3, 4] <class 'list'> 2788341771136
print(a, type(a), id(a))         # [1, 2, 3, 4] <class 'list'> 2788341771136

# EJEMPLOS DEL OPERADOR SUMA ASIGNACIÓN +=
# Todos los operadores que veremos a continuación sirven para abreviar el código, pero además
# permiten hacer más cosas
x += 1     # x = x + 1     LOS QUE VENGÁIS DE OTROS LENGUAJES: EN PYTHON NO EXISTE x++ ++x
print(x)   # 6.4

lista2 = [1, 2, 3]
lista2 += [4, 5, "hola"]       # lista2 = lista2 + [4, 5]    se produce la unión o suma de listas
print(lista2)                  # [1, 2, 3, 4, 5, 'hola']

# EJEMPLOS DEL OPERADOR RESTA ASIGNACIÓN -=
n1 = 9
n2 = 10
n1 -= n2    # n1 = n1 - n2
print(n1)   # 90

# EJEMPLOS DEL OPERADOR PRODUCTO ASIGNACIÓN *=
n1 = 9
n2 = 10
n1 *= n2    # n1 = n1 * n2
print(n1)   # 90

# EJEMPLOS DEL OPERADOR DIVISON ASIGNACIÓN /=
n1 = 10
print(n1, type(n1))   # 10 <class 'int'>
n1 /= 3               # n1 = n1 / 3
print(n1, type(n1))   # 3.3333333333333335 <class 'float'>

# EJEMPLOS DEL OPERADOR MODULO ASIGNACIÓN %=
# Recordemos que el operador % -> obtiene el resto o residuo de la división -> 6 % 2 = 0
a = 9
b = 15
b %= a     # b = b % a
print(b)   # 6

# EJEMPLOS DEL OPERADOR DIVISION ENTERA ASIGNACIÓN //=
a = 9
b = 15
b //= a       # b = b // a
print(b)      # 1

# EJEMPLOS DEL OPERADOR EXPONENTE ASIGNACIÓN **=
a = 5
a **= 2   # a = a**2
print(a)  # 25

a = 6
a **= -2   # 6^-2 = 1/6^2 = 1/36
print(a)   # 0.027777777777777776

# EJEMPLOS DEL OPERADOR AND ASIGNACIÓN &=  (Realiza bit a bit el AND Lógico)
a = 0b101010    # a es un entero en sistema binario
a &= 0b111111   # a = a & 0b111111   La operancion lógica AND se realiza bit a bit
print(bin(a))   # OJO: print(a) -> 42   bin(a) -> 0b101010

# EJEMPLOS DEL OPERADOR OR ASIGNACIÓN |=    (Realiza bit a bit el OR lógico)
a = 0b101010    # a es un entero en sistema binario
a |= 0b111111   # a = a | 0b111111   La operancion lógica OR se realiza bit a bit
print(bin(a))   # OJO: print(a) -> 63   bin(a) -> 0b111111

# EJEMPLOS DEL OPERADOR XOR ASIGNACIÓN ^=    (Realiza bit a bit el XOR lógico -> valores igual resultado 0)
a = 0b101010    # a es un entero en sistema binario
a ^= 0b111111   # a = a ^ 0b111111   La operancion lógica XOR se realiza bit a bit
print(bin(a))   # OJO: print(a) -> 21   bin(a) -> 0b10101

# EJEMPLOS MOV. DERECHA ASIGNACIÓN >>=      (Da error con float)
# EJEMPLOS MOV. IZQUIERDA ASIGNACIÓN <<=    (Da error con float)
a = 10     # 10 -> 0b1010
a >>= 1    # a = a >> 1 -> 0b1010 >> 1 -> 0b0101 = 5
print(a)   # 5

a = 10     # 10 -> 0b1010
a <<= 1    # a = a << 1 -> 0b1010 >> 1 -> 0b10100 = 20
print(bin(a))   # 20
