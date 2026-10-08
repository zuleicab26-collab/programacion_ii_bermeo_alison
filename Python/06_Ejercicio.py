peso = (int(float(input("Por favor ingrese el peso de su paquete en kilogramos: "))))
destino =(int(input("Por favor ingrese la zona del destino del paquete (1. America, 2. Europa o 3. Resto del mundo): ")))

zona_1 = 5.0
zona_2 = 7.5
zona_3 = 10.0 

if destino == 1: 
    costo_envio = peso * zona_1
    print("El costo de envío a América es:", costo_envio)
elif destino == 2:
    costo_envio = peso * zona_2
    print("El costo de envío a Europa es:", costo_envio)
elif destino == 3:
    costo_envio = peso * zona_3
    print("El costo de envío al resto del mundo es:", costo_envio)
else:
    print("Por favor ingrese un destino válido.")

