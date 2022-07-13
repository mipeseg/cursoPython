"""
TIPO DE DATO: Lógico o Booleano
 - permite almacenar dos valores: True o False
"""
# EJEMPLOS
x = y = True      # Declaración e inicialización de dos variables booleanos
print(x, y, type(x))

print(5 > 3)    # También se obtiene un booleano del resultado de evaluar una expresión

# Podemos convertir un elemento a booleano usando la funcion bool()

print(bool(), bool(None), bool(False))           # False
print(bool(0), bool(0.0), bool(0j))              # False
print(bool(()), bool(""), bool([]), bool({}))    # False   Secuencias vacías
print(bool(10))      # True        El resto siempre True
print(bool(-10))     # True
print(bool("Hola"))  # True
print(bool(0.1))     # True

# En realidad un booleano es una subclase de Int. De hecho True=1 y False=0
print("Es el valor True una instancia de la clase int?", isinstance(True, int))
print("Es la clase bool una subclase de int?", issubclass(bool, int))

"""
TIPO DE DATO: Cadena o string
 - una string es un tipo de datos inmutable (LUEGO LO EXPLICAMOS que almacena una secuencia de caracteres
 - creación: usando "" o ''
 - Una cadena no tiene límite de tamaño: puede estar vacía o tener un nº casi infinito de caracteres 
   (dependiendo del computador)
"""
# EJEMPLOS
# Creación e inicialización de una cadena
s1 = "Esta es una cadena"
s2 = 'Esta es otra cadena'
print(s1, type(s1))       # Esta es una cadena  <class 'str'>
print(s2, type(s2))       # Esta es otra cadena  <class 'str'>

# si usamos el simbolo "" dentro de una cadena da error. Como lo solucionamos?
# s3 = "Vamos a entrar en la pestaña "Administrador""   # Esto daría error
s3 = 'Vamos a entrar en la pestaña "Administrador"'   # Esto daría error
print(s3)

# Podemos incluir caracteres especiales dentro de una cadena. Ej: \n salto de linea  \t tabulacion
print("Esto es un salto\nde línea")
print("Esto es una \t tabulación")
print("El caracter 110 equivale a \110")

# si usamos comillas triples la cadena puede ocupar varias lineas
print("""Esta cadena
  puede ocupar
    varias lineas """)

# la funcion str() convierte un valor a cadena de texto
x = 5
s = "El número es: " + str(x)
print(s)  # El número es: 5

# Formateo de cadenas -> a veces necesitamos dar un formato especifico a las cadenas de textos
x = 9.3
y = -5
print("El valor de (x,y) =", "(", x, ",", y, ")")  # un poco farragoso
print("El valor de (x,y) = (%.1f,%d)" % (x, y))  # usando el formateo clásico de cadenas
print("El valor de (x,y) = ({},{})".format(x, y))  # usando el formateo moderno de cadenas
print("El valor de (x,y) = ({num1},{num2})".format(num1=26.78, num2=-56))  # usando el formateo moderno de cadenas
# formateo de cadenas usando f-strings o cadenas literales, que permiten incrustar expresiones
# o llamar a funciones dentro en la cadena
print(f"x + y = {x+y}")
print(f"La parte decimal de x+y tiene {len(str(x+y))-2} dígitos")

# concatenación o unión de strings
cad1 = "Hola"
cad2 = "mundo"
print(cad1+" "+cad2)

# replicar x veces una cadena
print(3*cad1)
print(cad2*5)

# saber si una cadena es subcadena de otra
cad1 = "El mundo es inmenso"
cad2 = "mundo"
print("cad2 está contenida en cad1?", cad2 in cad1)  # True

# chr(entero) -> convierte un valor numerico en el caracter ASCII equivalente
# ord(caracter) -> convierte un caracter ASCII en su valor numerico
print(chr(38))   # &
print(ord("&"))  # 38

# las cadenas son iterables, es decir, se pueden indexar
t = "Edad del cliente: 70 años"
edad = int(t[18] + t[19])
print(edad, type(edad))

# obtener una subcadena
cadena = "Python es el lenguaje más buscado en 2021"
print(cadena[7:21])  # obtiene la subcadena desde inicio hasta fin-1
print(cadena[0:6:2])  # obtiene la subcadena desde inicio hasta fin-1 de 2 en 2
print(cadena[0::2])  # obtiene la subcadena desde inicio hasta fin-1 de 2 en 2
print(cadena[7:])  # obtiene la subcadena desde inicio hasta el final

# Algunos métodos de la clase string
s = "la guerra de las GALAXIAS"
print(s.capitalize())  # capitalize() -> convierte el primer caracter en mayúscula y el resto a minúsculas
print(s.lower())  # lower() -> convierte todos los caracteres a minúsculas
print(s.upper())  # upper() -> convierte todos los caracteres a mayusculas
print(s.swapcase())  # swapcase() -> invierte mayusculas y minusculas
print(s.count("la"))  # count() -> permite contar las veces que aparece una subcadena
print(s.isalnum())  # devuelve True si todos los caracteres son alfanumericos   Aquí False por los backspace
print(s.isalpha())  # devuelve True si todos los caracteres son alfanbeticos   Aquí False por los backspace
print("  galaxia  ".strip())   # elimina los backspace al principio y al final
print("123".zfill(5))   # rellena con 0 por la izquierda hasta que la cadena tenga 5 caracteres
print("welcome to the jungle".split())  # crea una lista con cada subcadena separada por backspace
print("welcome, to the jungle".split(","))  # crea una lista con cada subcadena separada por coma
print("manzana#pera#naranja#fresa".split("#"))  # crea una lista con cada subcadena separada por #
# crea una cadena de una lista de cadenas, intercalando otra cadena
print("###".join(["uno", "dos", "tres", "cuatro"]))
