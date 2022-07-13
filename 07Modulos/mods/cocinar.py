"""
MODULOS (MODULES)
Un módulo es un fichero con extensión *.py, que alberga código y puede usarse desde otros módulos *.py
Así podemos reutilizar el código y organizarlo en namespaces

Para importar un modulo usamos la instruccion:
      import nombreDelModulo
"""

# Este fichero cocinar.py es un módulo desarrollado por mi, para este curso
# tiene codificadas dos funciones que usaremos desde cualquier otro módulo

def ver_recetas(cod):
    if cod == "1":
        print("Arroz con pollo: bla bla bla ... ")
    elif cod == "2":
        print("Tarta de queso: bla bla bla ... ")
    elif cod == "3":
        print("Macarrones al pesto: bla bla bla ... ")
    else:
        print("No existe receta con código: ", cod)

# if (__name__ == '__main__'):
print("Introduce código de receta: ", end="")
codigo = input()  # codigo es una cadena
ver_recetas(codigo)