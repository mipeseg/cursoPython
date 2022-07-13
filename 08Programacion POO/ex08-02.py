"""
TIPOS DE MÉTODOS EN UNA CLASE

a) métodos normales (def) -> los que definimos con la palabra reservada def
   - pueden consultar y modificar los atributos del objeto
   - pueden acceder a otros metodos
   - pueden modificar el estado de la clase (sef.class)
b) métodos de clase (@classmethod) -> los que definimos anteponiendo el decorador @classmethod a def
   - no puede acceder a los atributos de instancia
   - puede acceder a los atributos de clase
c) métodos estáticos (@staticmethod) -> los que definimos anteponiendo el decorador @staticmethod a def
   - no pueden modificar el estado ni de la clase ni de sus instancias
"""
# EJEMPLOS


class Persona:
    def metodo(self, arg1, arg2):     # el atributo self es obligatorio. Puede haber más parámetros
        self.pi += 1  # metodo puede consultar y modificar los atributos de clase
        self.dni = "123B"  # metodo puede consultar y modificar los atributos de instancia
        return "Método normal: ", \
               self.dni, self.pi, Persona.metododeclase(), \
               arg1+arg2, \
               self  # self es el propio objeto que llamó a metodo

    @classmethod
    def metododeclase(cls):           # el atributo cls es obligatorio. Puede haber más parámetros
        cls.pi += 1
        return "Método de clase: ", cls.pi, cls    # cls es la propia clase que llamó a metodo

    @staticmethod
    def metodoestatico():
        return "Método estático"

    # El método constructor __init__ es llamado automáticamente cuando se crea un objeto.
    def __init__(self, cod, nom):
        # print(f"Creando objeto {dni}")

        # Atributos de instancia (propios de cada objeto o instancia)
        self.dni = cod
        self.nombre = nom

    # Atributos de clase (comunes a la clase y a todos sus objetos)
    pi = 3.1415


individuo1 = Persona("12345678A", "Juan")
print(individuo1.dni, individuo1.nombre, individuo1.pi)
print(individuo1.metodo(5, 6))       # ('Método normal: ', 11, <__main__.Clase object at 0x000001F000D7EAA0>)
print(Persona.metododeclase())       # ('Método de clase', <class '__main__.Clase'>)
print(individuo1.metododeclase())    # ('Método de clase', <class '__main__.Clase'>)
print(Persona.metodoestatico())      # Método estático
print(individuo1.metodoestatico())   # Método estático
print(individuo1.pi, Persona.pi)     # ¿?¿?
