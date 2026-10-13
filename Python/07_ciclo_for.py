#Ciclo for 

naves=[
    "Caza N-1",
    "Nabe real de Nabbo",
    "Transporte"
]
for nave in naves:
    print("Inspecionado ", nave)

print("Inspeccion realizada")

rondas = range(1,6)

print("Tipo de rondas: ", type(rondas))
for ronda in rondas:
    print(f"Ronda de vigilancia: {ronda}")
    print(f"Tipo de dato ronda: {type(ronda)}")


droides = range(1,17,3) #Desde el uno hasta el 17 saltando 2

print("Tipo de droides: ", type(droides))
for droide in droides:
    print(f"Reparar: droide B1-{droide}")
    print(f"Tipo de dato droide: {type(droide)}")

planetas = [
    "Naboo",
    "Tatooine",
    "Coruscant"
]

recorrido = enumerate(planetas, start=1)

for posicion, planeta in recorrido:
    print(f"Destino {posicion}: {planeta}")
    print(f"Tipo de dato {posicion}: {type(planeta)}")

paises = [
    "Ecuador",
    "Venezuela",
    "Chile",
    "Colombia",
    "Brasil",
    "Estados unidos"
]
for pais in paises:
    if pais == "Chile":
        continue
    if pais == "Brasil":
        break                     #breake rompepor completo
    print(f"Pais visitado: {pais}")


jedi = {}
print(jedi)
jedi_activo = {
    "nombre": "Obiwan",
    "fuerza": "120",
    "estilo_pelea": "Samurai",
    "misiones": ["guerra alderan", "secuestro palpatine", "escolta de leia"],
    "descripcion": {
        "estatura": 1.80,
        "especie": "humana"
    }
}
print(jedi_activo)
nave = dict (nombre= "AZ-1", capacidad=8, turbo_laser=2)
print(nave)

jedi["nombre"] = "Luck"
jedi["fuerza"] = 150
print(jedi)

for clave, valor in jedi_activo.items():
    print(f"{clave}: {valor}")

