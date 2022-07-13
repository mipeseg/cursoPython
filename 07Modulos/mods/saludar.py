"""
MODULOS (MODULES)
Un módulo es un fichero con extensión *.py, que alberga código y puede usarse desde otros módulos *.py
Así podemos reutilizar el código y organizarlo en namespaces

Para importar un modulo usamos la instruccion:
      import nombreDelModulo
"""

# Este fichero saludar.py es un módulo desarrollado por mi, para este curso
# tiene codificadas dos funciones que usaremos desde cualquier otro módulo


def saludo(nombre):
    print("Hola", nombre)

# Fin del módulo
