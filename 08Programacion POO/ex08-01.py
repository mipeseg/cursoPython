"""
PROGRAMACIÓN ORIENTADA A OBJETOS
La POO es un paradigma de programación que se derrollo en 1970 intentado imitar la realidad,
pero se popularizó mucho más tarde.

"Todos los elementos que usamos son objetos que pertenecen a una clase. Todos los objetos de una clase
tienen las mismas propiedades (variables) y métodos (funciones) pq las heredan de su clase. Dentro de una clase
puede haber subclases que tambien heredan

Ej )          clase Mamífero
                 - propiedades: vertebrado, homeoetermos (sangre caliente), respiración pulmonar ...
                 - métodos: correr(), comer(), respirar(), dormir() ...
                 clase Perro
                   - propiedades: hocico, cuadrupedo, pelo corporal ...
                   - métodos: ladrar(), vigilar(), cazar(), caminar() ...
                 clase Persona
                   - propiedades: bipedo, racional, emocional ...
                   - métodos: pensar(), conducir(), jugar-bolos()

              creamos dos objetos ->  bobby Perro  y  juan Persona
                 juan.pensar() -> iniciaria el proceso para que juan piense
                 juan.bipedo -> True
                 bobby.hocico -> True
                 bobby.cuadrupedo -> True
                 bobby.bipedo -> error pq esta propiedad no la tiene la clase Perro
                 bobby.vertebrado y juan.vertebrado -> True
                 juan.respirar() y bobby.respirar() -> se inicia el proceso de respirar en ambos

Después de este ejemplo, entenderemos mejor que una clase es una entidad genérica y que un objeto
es una entidad concreta.
"""
# DEFINIR UNA CLASE


class Nada:    # Nada es una clase vacía
    pass       # instrucción vacía


a = Nada  # a es un objeto de clase Nada

# DEFINIR ATRIBUTOS Y MÉTODOS EN UNA CLASE
"""
Existen dos tipos de atributos:

a) atributos de instancia -> son atributos que harán único a cada objeto (a cada instancia de una clase)
   ej) bobby es un objeto de la clase Perro = bobby es una instancia de la clase Perro
b) atributos de clase -> son atributos comunes a todos los objetos de la clase

En el ex08-02 veremos los distintos tipos de métodos en una clase
"""


class Perro:
    # El método constructor __init__ es llamado automáticamente cuando se cree un objeto.
    def __init__(self, nom, r):
        # print(f"Creando perro {nom}, {r}")

        # Atributos de instancia (propios de cada objeto o instancia)
        self.nombre = nom
        self.raza = r

    # Atributos de clase (comunes a la clase y a todos sus objetos)
    familia = "cánidos"

    # Métodos
    def ladrar(self):
        print(self.nombre, "dice: Guau!")

    def caminar(self, pasos=0):   # pasos es un argumento opcional con el valor default 0
        print(self.nombre, f"ha caminado {pasos} pasos")


can1 = Perro("Bobby", "Bulldog")  # Crea el objeto bobby de clase Perro
can2 = Perro("Toby", "Caniche")    # Crea el objeto toby de clase Perro
print(Perro)   # <class '__main__.Perro'>  Perro es un clase definida por el usuario
print(int)     # <class 'int'>  int es una clase nativa de Python
print(can1, can2)  # indica su Clase y su dirección de comienzo en memoria
print(type(can1))  # <class '__main__.Perro'>
print(type(5))     # <class 'int'>
print(f"El perro nº1 se llama {can1.nombre} y es de raza {can1.raza}")  # formateamos la cadena de salida
print("El perro nº2 se llama %s y es de raza %s" % (can2.nombre, can2.raza))  # formateamos la cadena de salida
print(Perro.familia, can1.familia, can2.familia)  # cánidos cánidos cánidos
can1.ladrar()     # Bobby dice: Guau!
can2.ladrar()     # Toby dice: Guau!
can1.caminar()    # Bobby ha caminado 0 pasos
can2.caminar(30)  # Toby ha caminado 30 pasos

"""
PRINCIPIOS BÁSICOS DE LA POO (Los veremos más tarde)

 a) Herencia
 b) Cohesión
 c) Acoplamiento
 d) Abstracción
 e) Polimorfismo
 f) Encapsulamiento
"""
