"""
OPERADORES A NIVEL DE BIT (bitwise operators)
Permiten trabajar con numeros enteros representados en forma binaria. Recordatorio de conversiones a sist. decimal

Ej) 165 -> 1*10**2 + 6*10**1 + 5*10**0 -> 100 + 60 + 5 ->  165
Ej) ob11011 -> 1*2**4 + 1*2**3 + 0 + 1*2**1 + 1*2**0 = 16 + 8 + 2 + 1 -> 27
ej) 0x18 -> 1*16**1 + 8*16**0 -> 16+8 = 24

Veamos los operadores a nivel de bit:
 & -> realiza la operación lógica and bit a bit
 | -> realiza la operación lógica or bit a bit
 ^ -> realiza la operación lógica xor bit a bit ( dos valores distintos son TRUE)
 ~ (ALT+126) -> realiza la operación not sobre cada bit
 >> mueve los bits hacia la derecha e inserta 0 por la izquierda
 << mueve los bits hacia la izquierda e inserta 0 por la derecha

Reglas de prioridad (de mayor a menor prioridad) ->
mas info: https://docs.python.org/3/reference/expressions.html#operator-precedence
"""
# EJEMPLOS DE CONVERSIONES
print(bin(27))  # 0b11011
print(bin(0x18))  # 0b11000 -> 24

# operador & | y ^
a = 0b1101
b = 0b1011
print(bin(a & b))   # 0b1001
print(bin(a | b))   # 0b1111
print(bin(a ^ b))   # 0b0110

# operador ~ (not)
a = 40
b = 5
print(bin(a))    # 0b101000 =  40
print(bin(~a))  # -0b101001 = -41
print(bin(b))    # 0b101 =  5
print(bin(~b))  # -0b110 = -6

# operadores >> <<
a = 0b1000
b = 0b0001
print(bin(a >> 2))     # 0b0010 -> 2        (si movemos 4 0 mas bits el valor se hace 0b0)
print(bin(b << 4))    # 0b10000 -> 16        (si movemos 4 0 mas bits el valor crecerá)
print(0b10000)