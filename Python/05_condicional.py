#Condiccional if 
#Simple

combustible = 10
if combustible >= 10:
    print("Puede despegar")

#Condicional if-else 
creditos = 100
precio_repuestos = 150
if creditos >= precio_repuestos:
    print("Puede comprar repuestos")
else:
    print("No puede comprar repuestos")


creditos=int(input("Ingrese la cantidad de creditos: "))
precio_repuestos=int(input("Ingrese el precio de los repuestos: "))
if creditos >= precio_repuestos:
    print("Puede comprar repuestos")
else:
    print("No puede comprar repuestos")

#If anidado
if creditos >= precio_repuestos:
    print("Puede comprar repuestos")
    if creditos > precio_repuestos:
        print("Le sobran creditos") 
    else:
        print("Le alcanzan justo para comprar repuestos")
else:
    print("No tiene suficientes creditos para comprar el repuesto")


#Condicional if-elif-else
if creditos > precio_repuestos:
    print("Puede comprar repuestos y le sobran creditos")
elif creditos == precio_repuestos:
    print("Puede comprar repuestos y le alcanzan justo para comprarlo")
else:
    print("No tiene suficientes creditos para comprar el repuesto")


tipo_repuesto = input("Ingrese el tipo de repuesto motor, ala o escudo): ")
if tipo_repuesto == "motor" and creditos >= precio_repuestos and tipo_repuesto == "ala": 
    print("Puede comprar el repuesto y te sobran creditos")
elif tipo_repuesto == "ala" and creditos >= precio_repuestos:
    print("Puede comprar el repuesto y te sobran creditos")
elif tipo_repuesto == "escudo" and creditos >= precio_repuestos:
    print("Puede comprar el repuesto y te sobran creditos")
else:
    print("El repuesto no es válido")
    