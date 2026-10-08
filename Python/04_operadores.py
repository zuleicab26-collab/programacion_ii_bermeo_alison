#Operadores
"""
Operadores aritméticos
+ Suma
- Resta
* Multiplicación
/ División      
% Módulo
** Potenciación
"""

valor1 = 10
valor2 = 3
suma = valor1 + valor2
resta = valor1 - valor2
multiplicacion = valor1 * valor2
division = valor1 / valor2
modulo = valor1 % valor2
potenciacion = valor1 ** valor2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Potenciación:", potenciacion)

print("tabla de multiplicar del 5:")
print("5 x 1 =", 5 * 1)
print("5 x 2 =", 5 * 2) 
print("5 x 3 =", 5 * 3)
print("5 x 4 =", 5 * 4)
print("5 x 5 =", 5 * 5)
print("5 x 6 =", 5 * 6)
print("5 x 7 =", 5 * 7)
print("5 x 8 =", 5 * 8)
print("5 x 9 =", 5 * 9)
print("5 x 10 =", 5 * 10)


print("tabla de multiplicar del 7:")
multiplicador = 7
print(multiplicador, "x 1 =", multiplicador * 1)
print(multiplicador, "x 2 =", multiplicador * 2)    
print(multiplicador, "x 3 =", multiplicador * 3)
print(multiplicador, "x 4 =", multiplicador * 4)
print(multiplicador, "x 5 =", multiplicador * 5)
print(multiplicador, "x 6 =", multiplicador * 6)
print(multiplicador, "x 7 =", multiplicador * 7)
print(multiplicador, "x 8 =", multiplicador * 8)
print(multiplicador, "x 9 =", multiplicador * 9)
print(multiplicador, "x 10 =", multiplicador * 10)

print("Area de un triangulo con base 5 y altura 10:", (5 * 10) / 2)

#Operadores de comparacion (mayormente usado en if )
"""
== Igual a
!= Diferente de
> Mayor que
< Menor que
>= Mayor o igual que
<= Menor o igual que
"""
velocidad_anakin = 950
velocidad_sebula = 900

print("Aniki es más rápido que Sebula:", velocidad_anakin > velocidad_sebula)
print("Aniki es más lento que Sebula:", velocidad_anakin < velocidad_sebula)
print("Aniki es igual de rápido que Sebula:", velocidad_anakin == velocidad_sebula)
print("Aniki es diferente de Sebula:", velocidad_anakin != velocidad_sebula)
print("Aniki es más rápido o igual que Sebula:", velocidad_anakin >= velocidad_sebula)
print("Aniki es más lento o igual que Sebula:", velocidad_anakin <= velocidad_sebula)

resultado = velocidad_anakin > velocidad_sebula
print("Resultado de la comparación:", resultado)
print("Tipo de resultado:", type(resultado))

#Operadores lógicos
"""
and: Devuelve True si ambos operandos son True
or: Devuelve True si al menos uno de los operandos es True
not: Devuelve True si el operando es False y viceversa
"""

motores_funcionando = True
escudos_funcionando = False
combustible = 80

print("Todos los sistemas funcionando:", motores_funcionando and escudos_funcionando)
print("Algunos sistemas funcionando:", motores_funcionando or escudos_funcionando)
print("Los motores no están funcionando:", not motores_funcionando)

cantidad_motores = 2
cantidad_alas = 4
combustible = 80
print("La nave tiene al menos 2 motores y 4 alas?")
print(cantidad_motores >= 2 and cantidad_alas >= 4)
print("La nave tiene al menos 2 motores o 4 alas?")
print(cantidad_motores >= 2 or cantidad_alas >= 4)
print("La nave no tiene al menos 2 motores?")
print(not cantidad_motores >= 2 and combustible >= 50)

#Operadores de asignación
"""
= Asignación
+= Suma y asignación
-= Resta y asignación
*= Multiplicación y asignación
/= División y asignación
%= Módulo y asignación
**= Potenciación y asignación
"""
velocidad = 100
print("Velocidad inicial:", velocidad)
velocidad += 50
print("Velocidad después de acelerar 50:", velocidad)
velocidad -= 30
print("Velocidad después de frenar 30:", velocidad)
velocidad *= 2
print("Velocidad después de multiplicar:", velocidad)
division = 4
velocidad /= division
print("Velocidad después de dividir entre 4:", velocidad)
modulo = 3
velocidad %= modulo
print("Velocidad después de aplicar módulo 3:", velocidad)
velocidad //= 2
print("Velocidad después de dividir entre 2:", velocidad)
velocidad **= 2
print("Velocidad después de aplicar potenciación 2:", velocidad)

#Presendencia de operadores
"""
1. ()
2. **
3. *, /, //, %
4. +, -
"""

resultado_1 = 10 + 5 * 2
print("Resultado de 10 + 5 * 2:", resultado_1)
resultado_2 = (10 + 5) * 2
print("Resultado de (10 + 5) * 2:", resultado_2)
resultado_3 = 10 + 5 * 2 ** 2
print("Resultado 3:", resultado_3)