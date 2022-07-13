"""
OPERADORES ARITMÉTICOS (Arithmetic operators)
Ya los hemos visto en el punto anterior. Nos permiten realizar operaciones sencillas:
+, -, *, /, //, %, **

Reglas de prioridad

Cuando tenemos una expresión con muchas variables y operadores, Python tiene que saber como evaluarla,
x lo que se establecen prioridades. Veamos la clasificación de mayor a menor prioridad:
() -> Rompe con las prioridades implícitas. Siempre se evalua primero
**
- negación
* / // %
+ -
Documentación oficial: https://docs.python.org/3/reference/expressions.html
"""
# EJEMPLOS
# OPERADOR SUMA +
print(10 + 3.5)          # 13.5  suma de mumeros   (ESTA ES LA ÚNICA OPERACIÓN ARTIMÉTICA)
print("Hola" + "Mundo")  # HolaMundo  concatenación de cadenas
print([1, 2] + [3, 4])   # unión de listas

# OPERADOR RESTA -
print(10 - 3.5)          # 6.5 resta de mumeros

# OPERADOR PRODUCTO *
print(10 * 3.5)          # 35  producto de mumeros  (ESTA ES LA ÚNICA OPERACIÓN ARTIMÉTICA)
print(3 * "Hola")        # HolaHolaHola
print([1, 2] * 2)        # [1, 2, 1, 2]

# OPERADOR DIVISÓN REAL /
print(10/3)     # 3.3333333333333335
print(1/2)      # 0.5
print(12.3/2)   # 6.15

# OPERADOR DIVISION ENTERA // (cociente de la división entera)
# OPERADOR MODULO % (Resto de la división entera)
print(10 // 3, 10 % 3)   # 3 1
print(10 // 2, 10 % 2)   # 5 0

# OPERADOR POTENCIA **
print(10**3)    # 10^3 -> 1000
print(2**2)     # 2^2 -> 4

# EJEMPLOS DE PRIORIDAD

print(10*(5+3))       # 80 Se evalúa primero la expresion entre ()
print(10*5+3)         # 53 la * tiene prioridad sobre la +
print(3*3+2/5+5 % 4)  # 10.4 ->  3*3 = 9   2/5 = 0.4   5%4 = 1 -> 9+0.4+1 = 10.4
print(-2**4)          # -16 -> 2**4=16 -> -16  (primero se hace la potencia y luego la negación
print((-2)**4)        # 16 -> -2 -> -2**4 = 16 (primero se hace la negación y luego la potencia
