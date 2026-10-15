class Guerrero:
    nombre: str #atributos son nombre y poder
    poder: int
    def __init__(self, nombre, poder): #los parametros son nombre y poder
        self.nombre = nombre
        self.poder = poder

    def saludar(self): #los metodos son saludar
        print(f"Hola, soy ",self.nombre)

    def entrenar(self):
        aumento = 200
        self.poder += aumento

    def atacar(self, cantidad):
        danio = self.poder * cantidad
        print("Guerrero ", self.nombre)
        print("Ataca :",danio)

goku = Guerrero("Goku", 9000) #goku es un objeto de la clase Guerrero
goku.saludar() 

print("Nombre del personaje:",goku.nombre)
print("Poder del personaje:",goku.poder)
goku.entrenar()
print("Poder del personaje:",goku.poder)
print("Poder del personaje:",goku.poder)
goku.atacar(10)
