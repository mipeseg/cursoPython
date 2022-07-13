"""
EXCEPCIONES DEFINIDAS POR EL USUARIO
Si queremos crear nuestras propias excepciones definiremos clases que hereden de Exception
y lanzarlas manualmente con raise()
"""


# Creamos nuestra propia excepción heredando de la clase Exception
class MiExcepcion(Exception):
    # definimos el constructor de clase
    def __init__(self, p1, p2):
        self.parametro1 = p1
        self.parametro2 = p2


try:
    # Lanzamos manualmente con raise la excepción que hemos creado
    raise MiExcepcion("Division por cero", "El divisor es 0")
except MiExcepcion as e:
    print(e, type(e))    # ('Division por cero', 'El divisor es 0') <class '__main__.MiExcepcion'>
    print("parametro1 =", e.parametro1)
    print("parametro2 =", e.parametro2)

"""
GESTORES DE CONTEXTO (context managers)
Permite ahorrar código haciendo dos tareas. La 1ª al entrar a WITH y la 2ª al salir
"""

# Haciendo uso de los context managers, with -> abre el fichero, lo manipula y al salir lo cierra
with open('ejemplo.txt', 'w') as fichero:
    fichero.write('Hola!')

try:
    with open('ejemplo.txt', 'r') as fichero:
        print(fichero.read())
except Exception as e:
    print(e)
