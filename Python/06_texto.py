#string cadenas de caracteres
jedi = "Qui-Gon Jinn"
aprendiz = "Obi-Wan Kenobi"
droide = "R2-D2"
planeta = "Naboo"
codigo = "327"

print("El jedi es:" + jedi)
print("El jedi", type(jedi))
print("El aprendiz es:" + aprendiz)
print("El aprendiz", type(aprendiz))
print("El droide es:" + droide)
print("El droide", type(droide))
print("El planeta es:" + planeta)
print("El planeta", type(planeta))
print("El codigo es:" + codigo)

longitud_jedi = len(jedi)
print("La longitud del nombre del jedi es:", longitud_jedi) 
longitud_aprendiz = len(aprendiz)
print("La longitud del nombre del aprendiz es:", longitud_aprendiz)
longitud_droide = len(droide)
print("La longitud del nombre del droide es:", longitud_droide)
longitud_planeta = len(planeta)
print("La longitud del nombre del planeta es:", longitud_planeta)
longitud_codigo = len(codigo)
print("La longitud del código es:", longitud_codigo)

mensaje= "La Federación de Comercio ha establecido un bloqueo en  Naboo."
print("El mensaje es:" + mensaje)
mensaje_mayusculas = mensaje.upper()
print("El mensaje en mayúsculas es:" + mensaje_mayusculas)
mensaje_minusculas = mensaje.lower()
print("El mensaje en minúsculas es:" + mensaje_minusculas)

comunicado = ("Los jedis son enviados a Naboo.")
print("El comunicado es:" + comunicado)
nuevo_comunicado = comunicado.replace("Naboo", "Tatooine")
print("El nuevo comunicado es:" + nuevo_comunicado)

planetas = "Naboo, Tatooine, Coruscant, Alderaan"
planetas_lista = planetas.split(", ")
print(planetas_lista)
print("La lista de planetas es:"+ str(planetas_lista))  
print("El primer planeta es:" + planetas_lista[0])


droide = "R2-D2"
print("El droide es:" + droide)
print("El primer caracter del droide es:" + droide[0]) #r
print("El segundo caracter del droide es:" + droide[1])#2
print("El tercer caracter del droide es:" + droide[2])#-
print("El cuarto caracter del droide es:" + droide[3])#d
print("El quinto caracter del droide es:" + droide[4])#2
print("El sexto caracter del droide es:" + droide[-1]) #Se va al ultimo caracter


planeta = "               Naboo                    "
print("El planeta es:" + planeta)
print("El planeta sin espacios es:" + planeta.strip())

