"""
FUNCIONES LAMBDA O ANÓNIMAS
Son pequeñas funciones sin nombre, que podemos usar acortar el código. Se suelen usar pocas veces
    (lambda p1, p2 ... : cuerpo)(valor1, valor2 ...)
"""

# EJEMPLOS


def suma(a, b):  # definición de una función
    return a+b


print(suma(7, 8))
print((lambda a, b: a + b)(4, 6))    # definición de una función lambda

# función lambda como entrada de una función normal  (EJEMPLO DIDACTICO SIN MUCHA UTILIDAD PRACTICA)


def funcion_normal(lambda_func):
    return lambda_func(2, 4)


print(funcion_normal((lambda a, b: a + b)))

# funcion normal como entrada de una función lambda  (EJEMPLO DIDACTICO SIN MUCHA UTILIDAD PRACTICA)


def funcion_normal2(a, b):
    return a + b


print((lambda a, b: funcion_normal2(a, b))(12, 4))   # 16

# función lambda con parámetros nominales
print((lambda a, b, c: a + b - c)(b=1, a=2, c=4))    # -1

# función lambda con parámetros opcionales
print((lambda a, b, c=4: a + b + c)(1, 2))    # 7

# función lambda con un nº variable de argumentos
print((lambda *args: sum(args))(10, 20, 30))      # 60

# función lambda que devuelve más de un valor
x = lambda a, b: (a + b, b - a)
print(x(3, 9), type(x))  # (12, 6)

"""
RECURSIVIDAD
Determinados problemas se pueden resolver haciendo que una función se llame a si misna N veces.
OJO: Em cierto momento debe haber una condición de salida pq de lo contraria LLAMADAS INFINITAS
y perdida del control del flujo de ejecución
"""

# Ejemplos
# Cálculo del factorial de un nº  Ej: !4 = 4*3*2*1 = 24


def factorial_normal(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1
    return r


print(factorial_normal(4))     # 24

# Cálculo del factorial de un nº de forma recursiva  Ej: !4 = 4*3*2*1 = 24
# Mejor explicarlo con la pizarra


def factorial_recursivo(n):
    if n == 1:
        return 1   # condición de salida
    else:
        return n * factorial_recursivo(n-1)


print(factorial_recursivo(4))   # 24

# Cálculo de la sucesión de Fibonacci de forma recursiva  Ej: 0, 1, 1, 2, 3, 5, 8, 13 ...
# Mejor explicarlo con la pizarra


def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)


print(fibonacci_recursivo(4))  # 3    5º elemento de la serie de Fibonacci
