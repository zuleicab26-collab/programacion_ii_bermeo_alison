##FUNCIONES 

def activar_sistema():
    print("==Sistema de naboo==")
    print("Sistema de control activado")

activar_sistema()

#Funciones con parametro

def saludar_jedi(nombre):
    print(f"Que la fuerza te acompañe:{nombre}")
saludar_jedi("Qui-Gon Jim")
saludar_jedi("Obi-Wan Kenobi")          

def mostrar_nave(nombre, combustible):
    print(f"nave:{nombre}")
    print(f"cantidad combustible:{combustible}")


mostrar_nave("Caza N-1", 80)

#Funciones que devuelven dato o informacion 
#return

def calcular_combustible2(inicial, consumo):
    restante = inicial - consumo
    return restante

resultado =calcular_combustible2(100,25)
print(f"Combustible: {resultado}")

resultado =calcular_combustible2(100,35)
print(f"Combustible: {resultado}")

print(f"Combustible: {calcular_combustible2(100,15)}")

def nave_preparada(combustible):
    return combustible>=50

if nave_preparada(80):
    print("Nave autorizada para despegar")
else: 
    print("Nave necesita recarga")

    