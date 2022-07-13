"""
MODULOS (MODULES)
Un módulo es un fichero con extensión *.py, que alberga código y puede usarse desde otros módulos *.py
Así podemos reutilizar el código y organizarlo en namespaces

Para importar un modulo usamos la instruccion:
      import nombreDelModulo  ( lo ideal es importar los modulos al principio del codigo y solo una vez)
"""

# Vamos a importar el modulo miModulo.py y usar su funciones
import miModulo                   # importamos el mundo entero
# from miModulo import suma, e    # deprecado???. No funciona bien

print(miModulo.suma(4, 3))      # 7
print(miModulo.resta(10, 2))    # 8
print(miModulo.pi)              # 3.14159
print(miModulo.e)               # 2.718
print(miModulo.radio_tierra)    # 6370
miModulo.frutas += ["lima"]
print(miModulo.frutas)          # ['pera', 'manzana', 'lima']

"""
En el ejemplo anterior ex07-01.py y miModulo.py están en la misma carpeta.
Pero, qué ocurre si queremos importar un módulo de otra carpeta ??

PAQUETES (PACKAGE)
Un paquete es un directorio que alberga modulos *.py 
Dentro de nuestro proyecto, hemos de crear un Python package y dentro crear los modulos
"""

from mods import saludar
saludar.saludo("Pedro")

"""
Pero, y si queremos tener todos nuestros modulos almacenados fuera de los proyectos??

a) Escojemos una ruta Ej: "D:\\liberfin2020\\canal youtube\\DODO island\\CURSOS\\Curso de Pyhton\\""
b) Dentro creamos una carpeta "Packages"
c) En la carpeta "Packages" creamos el fichero "__init__.py" que dejamos vacío (ahora ya es un paquete)
d) En el paquete "Packages" es donde copiaremos todos nuestros modulos *.py
"""

import sys            # importamos el modulo sys
# añadimos la ruta
sys.path.append(r'D:\liberfin2020\canal youtube\DODO island\CURSOS\Curso de Pyhton')
# cargamos el paquete y el modulo vamos a utilizar e importamos entero su codigo con *
from Packages.despedir import *
from Packages.funciones import *

# usamos las funciones deseadas
despedida("Ana")       # Hasta luego Ana
bye("Luis")            # Adiós Luis
despedida("Santiago")  # Hasta luego Santiago

# Podemos ver info de nuestro modulo
print(dir())     # permite ver los nombres de variables, funciones, clases ... cargados en nuestro namespace
print(__file__)  # .... \Ejercicios\07Modulos\ex07-01.py   ruta y nombre del modulo
print(__name__)  # __main__ indica que es el modulo principal
print(__package__)  # None  Este modulo no pertenece a ningún paquete

# Si intentamos importar un modulo que no existe da error.
# import moduloquenoexiste   # ModuleNotFoundError: No module named 'moduloquenoexiste'

# Si importamos un modulo que no existe podemos controlar el error
try:
    import moduloquenoexiste
except Exception as e:
    print("Error importando el modulo:", e)

# Y si tenemos un modulo del que queremos usar solo sus funciones pero no el resto del código ???
from mods import cocinar
cocinar.ver_recetas("1")   # Arroz con pollo: bla bla bla ...   Seguro que mostrará esto??

# recargar un modulo
# por mucho que usemos la instrucción import, sólo se importa la primera vez
import mods.recargar   # se importa el modulo recargar
import mods.recargar   # instrucción ignorada
import mods.recargar   # instrucción ignorada

# si por algún motivo queremos volver a importar un modulo
import importlib    # importamos un modulo nativo de Python
importlib.reload(mods.recargar)  # usamos su metodo reload()
importlib.reload(mods.recargar)  # usamos su metodo reload()
