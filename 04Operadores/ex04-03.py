"""
OPERADORES RELACIONALES (Comparison operators)
Se usan para saber la relación entre elementos. Ej) a > 5   a == b  c == (x/25+3)  a < b <= 3
y generan una expresión logica. Los operadores relacionales son:

== igual
!= distinto
> < >= <=  mayor  menor   mayor o igual  menor o igual

Reglas de prioridad
https://docs.python.org/3/reference/expressions.html#operator-precedence

"""
# EJEMPLOS
# OPERADOR IGUALDAD == (OJO: No confundir con la asignación)
print(4 == 4)            # True
print(4 == 5)            # False
print(4 == 4.0)          # True
print(0 == False)        # True
print("asd" == "asd")    # True
print("asd" == "asdf")   # False
print(2 == "2")          # False
print([1, 2, 3] == [1, 2, 3])   # True

print("")

# OPERADOR DISTINTO DE !=
print(4 != 4)           # False
print(4 != 5)           # True
print(4 != 4.0)         # False
print(1 != True)        # False
print("asd" != "asd")   # False
print("asd" != "asdf")  # True
print(2 != "2")         # True
print([1, 2, 3] != [1, 2, 3])  # False

print("")

# OPERADORES > < >= <=
print(5 > 3)              # True
print(5 > 5)              # False
print(True > 0.999)       # True
print([1, 2] > [10, 10])  # False
print("abc" < "abd")      # True
print("A" < "a")          # True  (Esto se debe a que lo que se comparan son los valores unicode)
print(ord('A'))           # 65
print(ord('a'))           # 97
print(3 >= 3)             # True
print([3, 4] >= [3, 5])   # False
print(3 <= 2.99999999999999999)  # True
