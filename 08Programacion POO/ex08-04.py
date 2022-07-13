"""
COHESIÓN -> Es la relación que tienen entre sí los elementos de una función. Cuántas más cosas
haga la función menor cohesión y viceversa
a) cohesión debil -> relacion entre elementos es baja
b) cohesión fuerte -> relación entre elementos es alta (OBJETIVO A CONSEGUIR)
"""


# Ejemplo de cohesión baja (mal uso)
# Si queremos reutilizar esta función para que nos sume solo numeros no nos servirá


def suma1():
    num1 = float(input("Dame primer número"))
    num2 = float(input("Dame segundo número"))
    suma = num1 + num2
    print(suma)


# suma1()

print()

# Ejemplo de cohesión alta (se recomiendo su uso)
# suma2 sólo suma una lista


def suma2(numeros):
    total = 0
    for i in numeros:
        # total += i
        if str(i).isdigit():
            total = total + int(i)
    return total


# print("La suma es:", suma2([2, 3, 5, 6]))   # uso A
"""
   "1,3,4,6"
   ['1',',','3',',','4',',','6']
"""
# print(suma2(list(input("Introduce secuencia de numeros separada por comas"))))  # uso B
print()

"""
ACOPLAMIENTO (Coupling)
Mide la dependencia de un módulo con otros. Dos tipos:
a) acoplamiento débil -> nuestro módulo no tiene dependencia con otros módulos   (OBJETIVO A CONSEGUIR)
b) acoplamiento fuerte -> nuestro módulo tiene dependencias internas con otros módulos
"""
# Ejemplo de acoplamiento fuerte


class Clase1:
    x = True   # Si cambiamos a False -> AttributeError: 'Clase2' object has no attribute 'valor' en linea 59


class Clase2:
    def mi_metodo(self, valor):
        if Clase1.x:
            self.valor = valor


mi_clase = Clase2()
mi_clase.mi_metodo("Hola")
print(mi_clase.valor)

print()

"""
ABSTRACCIÓN
La abstracción de una clase consiste en ocultar la complejidad interior ofreciendo métodos de alto nivel,
sencillos de usar para que podamos interactuar con ella (una interfaz). Ej) No necesitamos conocer 
la circuitería de un TV para interactuar con él a través de un mando o interfaz ( que nos ofrece funciones de 
alto nivel como subirVolumen, bajarVolumen, cambiarCanal, etc...

Una clase interface es aquella que tiene métodos abstractos (vacíos de código). Y ya serán
las clases hija las que lo implementen. En Python hay dos tipos de clases interface:
  - Interfaces informales -> veremos un ejemplo
  - Interfaces formales -> Se definen con @absttractmethod  (NO SON OBJETIVO DE ESTE CURSO)
"""
# EJEMPLO DE INTERFACE INFORMAL


class Mando:                       # Mando es una clase interface. Define "que métodos" pero no "el cómo"
    def siguiente_canal(self):
        pass

    def canal_anterior(self):
        pass

    def subir_volumen(self):
        pass

    def bajar_volumen(self):
        pass


class MandoSamsung(Mando):
    def siguiente_canal(self):
        print("Samsung->Siguiente CH")

    def canal_anterior(self):
        print("Samsung->Anterior CH")

    def subir_volumen(self):
        print("Samsung->Subir VOL")

    def bajar_volumen(self):
        print("Samsung->Bajar VOL")


class MandoLG(Mando):
    def siguiente_canal(self):
        print("LG->Siguiente CH")

    def canal_anterior(self):
        print("LG->Anterior CH")

    def subir_volumen(self):
        print("LG->Subir VOL")

    def bajar_volumen(self):
        print("LG->Bajar VOL")


m1 = MandoSamsung()
m1.siguiente_canal()  # Samsung->Siguiente CH
m1.subir_volumen()    # Samsung->Subir VOL

m2 = MandoLG()
m2.siguiente_canal()  # LG->Siguiente CH
m2.subir_volumen()    # LG->Subir VOL

print()

"""
POLIMORFISMO
Un objeto puede tomar diferentes formas. 
Dicho de otra forma: un objeto puede cambiar de clase.

"""
# Recordáis que Python tiene tipado dinámico?. Eso nos permite que una variable
# cambie su tipo en función del dato que almacena. Y poder hacer cosas como esta:

# manzana <class 'str'>      En la 1º iteración a es una cadena
# [1, 2, 3] <class 'list'>   En la 2º iteración a es una lista

for a in "manzana", [1, 2, 3]:
    print(a, type(a), " *** ", end="")

print("\n")

# Imaginaros que algo parecido ocurre con el polimorfismo
# NOTA: Con el tipado dinámico es más dificil ver el polimorfismo. Se ve mejor con lenguajes
#       de tipado estático como C y Java. Ej) int a = 5;
#       De hecho, el siguiente ejemplo aunque las clases Perro y Gato no fueran hijas de Animal
#       funncionaría igual por el tipado dinámico.


class Animal:
    def hablar(self):   # método vacío
        pass


class Perro(Animal):
    def hablar(self):   # sobreescribimos el método de la clase padre
        print("Guau!")


class Gato(Animal):     # sobreescribimos el método de la clase padre
    def hablar(self):
        print("Miau!")


# En la 1ª iteración el objeto animal es un Perro
# En la 2ª iteración el objeto animal es un Gato
for animal in Perro(), Gato():
    print(type(animal), "", end="")
    animal.hablar()

print()

"""
ENCAPSULAMIENTO O ENCAPSULACIÓN
Encapsular -> Hacer que los atributos y métodos internos de una clase se oculten al exterior.
              Sólo para uso interno en la clase.
NOTA: Python, por defecto, no encapsula
"""

# EJEMPLO SIN ENCAPSULAMIENTO (DEFAULT)


class Clase5:
    atrib1 = "Atributo de clase"            # atrib1 es un atributo de clase

    def __init__(self, atrib2):             # método constructor
        self.atrib_inst = atrib2            # atrib_inst es un atributo de instancia


obj2 = Clase5("Que tal?")
print(obj2.atrib1)          # Atributo de clase    Accedido por un objeto de esa clase  (DESDE EL EXTERIOR)
print(obj2.atrib_inst)      # Que tal?             Accedido por un objeto de esa clase  (DESDE EL EXTERIOR)
print(Clase5.atrib1)        # Atributo de clase    accedido desde el exterior
# print(Clase5.atrib_inst)  # AttributeError: type object 'Clase5' has no attribute 'atrib_inst'
print()

# EJEMLPLO: podemos usar los __x para hacer un atributo o método privado, y que no se pueda acceder desde
# el exterior


class Clase6:
    atrib1 = "Atributo de clase público"       # atrib1 es un atributo de clase PÚBLICO
    __atrib2 = "Atributo de clase privado"     # atrib2 es un atributo de clase PRIVADO

    def __init__(self, saludo):             # método constructor es PRIVADO por defecto
        self.atrib_inst = saludo          # atrib_inst es un atributo de instancia (sólo accesible a objetos)

    # Accesible desde el exterior
    def metodo_publico(self=0):
        print("Soy un método público")

    # Accesible desde el interior
    def __metodo_privado(self):
        print("Soy un método privado")


obj3 = Clase6("Que tal?")
print(obj3.atrib1)            # Atributo de clase público    Accedido por un objeto de esa clase desde el ext
print(Clase6.atrib1)          # Atributo de clase público    Accedido desde el exterior
# print(obj3.atrib2)          # AttributeError: 'Clase6' object has no attribute 'atrib2'
# print(Clase6.atrib2)        # AttributeError: type object 'Clase6' has no attribute 'atrib2'
print(obj3.atrib_inst)        # Atributo de instancia    Accedido por un objeto de esa clase
# print(Clase6.atrib_inst)    # AttributeError: type object 'Clase6' has no attribute 'atrib_inst'
obj3.metodo_publico()         # Soy un método público        Accedido por un objeto desde el exterior
Clase6.metodo_publico()       # Soy un método público        Accedido desde el exterior
# obj3.metodo_privado()       # AttributeError: 'Clase6' object has no attribute 'metodo_privado'
# Clase6.metodo_privado()     # AttributeError: type object 'Clase6' has no attribute 'metodo_privado'
