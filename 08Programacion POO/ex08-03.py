"""
HERENCIA
  Una clase hija hereda los métodos y atributos de su clase padre. Además, la clase hija puede sobreesribit
  los heredados del padre y definir nuevos.

  - print(Clase.__base__) --> El atributo de clase   __base__   imprime el nombre de la clase padre
  - print(Clase.__subclasses__()) --> El método de clase   __subclasses__()   imprime una lista con
                                      los nombres de las clases hijas

  Utilidad de la herencia: Evitar el duplicar código innecesariamente
"""

# EJEMPLOS: Definimos una clase Animal y su hija Perro


class Animal:
    # implementamos el constructor de clase
    def __init__(self, espec, anyos):
        # atributos de instancia
        self.especie = espec
        self.edad = anyos

    # Método genérico pero con implementación particular
    def hablar(self):
        # Lo dejamos vacío para que se implemente en las clases hijas
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Lo dejamos vacío para que se implemente en las clases hijas
        pass

    # Método genérico común a todas las clases hijas
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)  # __name__ muestra solo el nombre de la clase


class Perro(Animal):
    # redefinimos el constructor que hereda del padre
    def __init__(self, espec, anyos, nom_duenyo):
        super().__init__(espec, anyos)  # llamamos al constructor del padre y le pasamos argumentos
        self.duenyo = nom_duenyo  # definimos un nuevo atributo de instancia

    def hablar(self):  # sobreescribe el método hablar del padre
        print("Guau!")

    def moverse(self):  # sobreescribe el método moverse del padre
        print("Se mueve caminando con 4 patas")


class Vaca(Animal):
    def hablar(self):   # sobreescribe el método hablar del padre
        print("Muuu!")

    def moverse(self):  # se sobreescribe el método moverse del padre
        print("Se mueve caminando con 4 patas")


class Abeja(Animal):
    def hablar(self):  # sobreescribe el método hablar del padre
        print("Bzzzz!")

    def moverse(self):   # se sobreescribe el método moverse del padre
        print("Se mueve volando")

    def picar(self):  # se crea un método nuevo exclusivo de las abejas
        print("Al ataque!")

"""
La clase Object es la base de la jerarquía de clases en Python. 
Todas las clases son subclases de la clase de Object, por lo tanto todos los objetos 
son instancias de Object.
"""
print(Animal.__base__)  # <class 'object'>   El padre de Animal es la clase object

# Las clases hijas de Animal son Perro, Vaca y Abeja
print(Animal.__subclasses__())  # [<class '__main__.Perro'>, <class '__main__.Vaca'>, <class '__main__.Abeja'>]
print(Perro.__base__)  # <class '__main__.Animal'>  La clase padre de Perro es Animal
print(Perro.__subclasses__())  # [] La clase Perro no tiene clases hijas
print(Vaca.__base__)  # <class '__main__.Animal'>  La clase padre de Vaca es Animal
print(Vaca.__subclasses__())  # [] La clase Vaca no tiene clases hijas
print(Abeja.__base__)  # <class '__main__.Animal'>  La clase padre de Abeja es Animal
print(Abeja.__subclasses__())  # [] La clase Abeja no tiene clases hijas

# observa que la clase Perro tiene un atributo especifico (duenyo) que no tienen los otros Animales
perro1 = Perro('mamífero', 10, "Pedro")
vaca1 = Vaca('mamífero', 23)
abeja1 = Abeja('insecto', 1)
print("perro1:", perro1.especie, perro1.edad, perro1.duenyo)  # perro1: mamífero 10 Pedro
print("vaca1:", vaca1.especie, vaca1.edad)                    # vaca1: mamífero 23
print("abeja1:", abeja1.especie, abeja1.edad)                 # abeja1: insecto 1

perro1.hablar()        # Guau!
perro1.moverse()       # Se mueve caminando con 4 patas
perro1.describeme()    # Soy un Animal del tipo Perro
vaca1.hablar()         # Muuu!
vaca1.moverse()        # Se mueve caminando con 4 patas
vaca1.describeme()     # Soy un Animal del tipo Vaca
abeja1.hablar()        # Bzzzz!
abeja1.moverse()       # Se mueve volando
abeja1.describeme()    # Soy un Animal del tipo Abeja
abeja1.picar()         # Al ataque!

"""
HERENCIA MÚLTIPLE
a) cuando una clase hereda de su padre, abuelo, bisabuelo ...
b) cuando una clase hereda de varios padres
"""

# Herencia múltiple caso A


class Abuelo:
    # implementamos el constructor de clase
    def __init__(self, nom, anyos):
        # atributos de instancia
        self.nombre = nom
        self.edad = anyos

    def explicacion(self):
        print("Soy el objeto abuelo")


class Padre(Abuelo):
    def explicacion(self):
        print("Soy el objeto padre")


class Hijo(Padre):
    def explicacion(self):
        print("Soy el objeto hijo")


obj1 = Hijo("Pablo", 25)
print(obj1.nombre, obj1.edad)  # Pablo 25
obj1.explicacion()             # Soy el objeto hijo

# Por qué si el método explicacion está definido en las tres clases, se usa el de la clase hijo.
# Porque sobreescribe los metodos heredados de las clases ancestras.
# Aun así,  podemos ver el orden en el que un objeto buscará un método entre las clases ancestras
# usando el atributo de clase __mro__

# (<class '__main__.Hijo'>, <class '__main__.Padre'>, <class '__main__.Abuelo'>, <class 'object'>)
print(Hijo.__mro__)
print(Padre.__mro__)   # (<class '__main__.Padre'>, <class '__main__.Abuelo'>, <class 'object'>)
print(Abuelo.__mro__)  # (<class '__main__.Abuelo'>, <class 'object'>)

# Herencia múltiple caso B


class Clase1:
    pass


class Clase2:
    pass


class Clase3:
    pass


class Clase4(Clase1, Clase3, Clase2):
    pass


"""
(<class '__main__.Clase4'>, <class '__main__.Clase1'>, <class '__main__.Clase3'>, 
<class '__main__.Clase2'>, <class 'object'>)
"""
print(Clase4.__mro__)
