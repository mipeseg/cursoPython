"""
DECORADOR @property
Este decorador hace que un método (función) se comporte como una propiedad. Esto combinado con
la ENCAPSULACIÓN tiene utilizades prácticas como:
  - A) hacer privado un atributo y además controlar su acceso mediante un método property
  - B) Consultar un parámetro que requiera de cálculos previos antes de ofrecerlos. De
       paso evitar redundancias
"""


# Ejemplo A
class Clase:
    # método constructor
    def __init__(self, p1):
        self.__atrib1 = p1   # atributo de instancia pero PRIVADO (solo es accesible desde dentro de la clase

    @property
    def mi_atributo(self):
        return self.__atrib1


obj1 = Clase("Programación en Python")
print(obj1.mi_atributo)       # Programación en Python   mi_atributo se comporta como una propiedad
# print(obj1.mi_atributo())   # TypeError: 'str' object is not callable   SI INTENTAMOS LLAMARLO COMO METODO
# print(obj1.__atrib1)        # AttributeError: 'Clase' object has no attribute '__atrib1'
# print(obj1.atrib1)          # AttributeError: 'Clase' object has no attribute 'atrib1'


# Ejemplo B
class Rectangulo:
    # método constructor
    def __init__(self, nom, b, a):
        self.nombre = nom    # atributo de instancia, accesible desde un objeto
        self.__base = b      # atributo de instancia pero PRIVADO (solo es accesible desde dentro de la clase)
        self.__altura = a    # atributo de instancia pero PRIVADO (solo es accesible desde dentro de la clase)
        # self.__perimetro = 2 * (self.__base + self.__altura)
        # self.__area = self.__base * self.__altura

    @property
    def perimetro(self):   # acceso controlado a los atributos de instancia
        return 2 * (self.__base + self.__altura)

    @property              # acceso controlado a los atributos de instancia
    def area(self):
        return self.__base * self.__altura


r1 = Rectangulo("RectanguloA", 6, 5)
r2 = Rectangulo("RectanguloB", 2.8, 3.7)
print(f"El perímetro de {r1.nombre} es {r1.perimetro}m")
print(f"El área de {r1.nombre} es {r1.area}m2")
print(f"El perímetro de {r2.nombre} es {r2.perimetro}m")
print(f"El área de {r2.nombre} es {r2.area}m2")
