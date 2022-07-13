"""
OPERADORES LÓGICOS (logical operators)
Permiten trabajar con valores lógicos o booleanos (True y False)

not  -> inversión del valor   not(True) es False y viceversa
and  -> pensar en el producto -> 0*0=0   0*1=0   1*0=0   1*1=1
or   -> pensar en la suma -> 0+0=0   0+1=1   1+0=1   1*1=1

Reglas de prioridad (de mayor a menor prioridad) -> not, and, or
mas info: https://docs.python.org/3/reference/expressions.html#operator-precedence

"""
# EJEMPLOS OPERADOR AND
hace_sol = True
fin_de_semana = True
ir_a_playa = hace_sol and fin_de_semana
print(ir_a_playa)
print(5 >= 3 and 10 < 8)   # True and False -> False

# EJEMPLOS OPERADOR OR
print(5 >= 3 or 10 < 8)   # True or False -> True

# OPERADOR NOT o negación lógica
print(not True)     # False
print(not False)    # True
print(not not not not True)   # True
print(not 0)   # True
print(not 1)   # False

# EJEMPLOS DE ORDEN DE PRIORIDAD
print(5 >= 3 or 10 < 8 and 5)   # True or False and True -> True  (and tiene prioridad sobre or)
print(False and False or True)  # True
print(True or False and False)  # True
# True  -> 0 and False or 1 and True or 1 and 0
#       -> False or True or False
#       -> True
print(0 and not 1 or 1 and not 0 or 1 and 0)   # 0 and 0 or 1 and 1 or 1 and 0    0 or 1 or 0   1 or 0  1