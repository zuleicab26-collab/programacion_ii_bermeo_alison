print("=====Control de energía======")
energia_textp = "ochenta"
try:
    energia = int(energia_textp)
    print(energia)
except ValueError:
    print("Error: deber ser numerico")

print("Fin del sistema")


"""
VakueError
TYpeError
KeyError
IndexError
ZeroDivisionError
"""


def calcular_energia(total,cantidad):
    try:
        resultado = total/cantidad
    except ZeroDivisionError:
        print("Error: division entre cero")
        return None
    except TypeError:
        print("Error: valor debe ser numerico")
        return None

print("Caso 1:", calcular_energia(100,4))
print("Caso 2:", calcular_energia(100,0))
print("Caso 3:", calcular_energia(100,"cuatro"))



print("========== DIAGNOSTICO R2-D2 ==========")
try:
    energia = int("cuatro")
    print("energia:",energia)
except ValueError:
    print("Error ded lectura")
else:
    print("Diagnostico completado")
finally:
    print("Cerrando diagnostico")



def validar_energia(energia):
    if type(energia) is not int:
        raise TypeError("La energia debe ser numero entero")
    if energia < 0 or energia > 100:
        raise ValueError("La energia debe estar entre 0 y 100")
    return energia


try:
    resultado = validar_energia(60)
    print("Eneria",resultado)
except (TypeError,ValueError) as error:
    print("Error:",error)


