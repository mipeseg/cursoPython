"""
Sintaxis de un lenguaje de programación = Conjunto de reglas que indican como se escribe el código. Es
como la gramática en los idiomas
Ej: En lenguaje C  ->  a = 5; OK
    En Python -> a = 5; KO
"""

# Definimos tres variables a,b y c. Operamos con ellas y mostramos los resultados en pantalla

x = "El valor de (a+b)*c es"     # x es de tipo cadena
a, b, c = 4, 3, 2                # asignación múltiple
ancho = alto = profundo = 21     # asignación múltiple
d = (a + b) * c                  # Operación aritmática cuyo resultado almacenamos en d
imprimir = False                  # Definimos una variable de tipo booleano, y la inicializamos a verdadero

if imprimir:
    print(x, d)                  # Salida: El valor de (a+b)*c es 14
else:
    print("Es falso")            # Salida: Es falso

# Identación o tabulación de 4 espacios
# con 1 o más espacios WARNING
# con 0 espacios ERROR
if True:
    print("True")

# en Python no se termina las instrucciones con ; excepto si queremos escribir varias en una misma línea
# num1 = 34;
# num2 = 2.2;
# num1 = 34; num2 = 2.2

# Podemos separar una instrucción muy larga en Múltiples lineas usando \ o ()
# No es recomendable lineas de más de 79 caracteres
x = 100 + 200 + 300 + 400 + 500 + 600 + 700 + \
    800 + 900 + 2000 + 3000 + 40000 + 5000
y = 100 + 200 + 300 + 400 + 500 +\
    600 + 700 + 800 + 900 +\
    2000 + 3000 + 40000 + 5000
z = (100 + 200 + 300 + 400 + 500 +
     600 + 700 + 800 + 900 +
     2000 + 3000 + 40000 + 5000)

# Reglas de creación de nombres de variables o funciones
# 1. No pueden empezar por un numero
# 2. No se puede usar el guión medio -
# 3. no se permite el carácter espacio
# 4. no se puede usar palabra reservadas

# Ejemplos de nombres de variables no válidos
# 2area = 1535
# are-a = -4567
# are a = 105.6
# if = 3
# print = -67

# Podemos ver todas las palabras reservadas de Python
import keyword
print(keyword.kwlist)

# Ejemplos de nombres de variables válidos
_demo = 1000
de_mo = 2000
demo35 = 1.25
demo = -34
deMo = "Esto es una cadena"

# Uso de () en operaciones da prioridad
alpha = 10
beta = alpha*3-3**2-2+3   # 30-9-2+3  22
print(beta)               # salida 22

beta = alpha*(3-3)**2-2+3   # 10*0-2+3  1
print(beta)               # salida 1

beta = alpha*(3-3**2)-2+3   # 10*-6-2+3  -59
print(beta)               # salida -59

# ambito, alcance o Scope de una variable: Global vs Local
perimetro = 25  # ambito global


def alerta():
    global perimetro
    p = 5  # ambito local
    return perimetro + p


print("perimetro global", perimetro, "---", "perimetro local", alerta())
