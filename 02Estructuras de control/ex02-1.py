# ESTRUCTURA CONDICIONAL IF - ELIF - ELSE
a = 4
b = 0

if b != 0:   # controlamos que el divisor sea distinto de 0 para evitar el error SeroDivisionError
    print(a/b)
else:
    print("División por cero no permitida")

# otro ejemplo de uso. Verificar si un número es par o impar
x = 7
if x % 2 == 0:   # % es el operador modulo. Es un operador aritmético que obtiene el resto o residuo de una division
    print("Es par")
else:
    print("Es impar")

# recordar la importancia de identar con 4 espacios las instrucciones del cuerpo
c = 0
if c != 0:
    d = c/2
    print("El valor de d es", d)
print("Fuera del if")

# la expresion condicional puede ser lo compleja que sea necesario
edad = 18
if edad >= 12 and edad < 18:        # creamos un rango [12..17]   / se puede simplificar con 12 <= edad < 18
    print("Eres adolescente")

# a diferencia de otros lenguajes, en Python no puede haber una instruccion o función vacía. Salvo que usemos
# la instruccion vacía pass
if a > 5:
    pass

# aunque se recomienda identar, podemos escribir las instrucciones del cuerpo a la misma línea para ahorrar lineas
# if a > 3: print("Es > 3")
# if a > 3: print("Es > 3"); print("Dentro del if")

# Veamos un ejemplo completo / La siguiente estructura equivale al switch en otros lenguajes. En Python no existe
x = "jhkfjsdhk"

if x == 5:
    print("x vale 5")
elif x == 6:
    print("x vale 6")
elif x == 7:
    print("x vale 7")
else:
    print("x desconocido")

""" OJO QUE ESTO NO ES PYTHON, es C
switch(x) {
  case 5:
    printf("x vale 5\n"); break;
  case 6:
    printf("x vale 6\n"); break;
  case 7:
    printf("x vale 7\n"); break;
  default:
     printf("valor desconocido\n"); 
}
"""

# OPERADOR TERNARIO  [código si se cumple] if [condición] else [código si no se cumple]
a = 100
b = 2
c = a/b if b != 0 else -1    # -1 podría indicar que se ha producido la división por 0
print(c)
