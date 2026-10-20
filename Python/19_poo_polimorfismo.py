class Guerrero:
    nombre: str
    poder_inicial: int
    horas: int
    def __init__(self, nombre: str, poder_inicial: int, horas: int):
        self.poder_inicial = poder_inicial
        self.horas = horas
        self.nombre = nombre

    def atacar(self):
        print(f"{self.nombre} realizar una ataque")

    def calcular_poder(self):
        return self.poder_inicial

class Goku(Guerrero):
    def __init__(self, nombre: str, poder_inicial: int, horas: int):
        super().__init__(nombre, poder_inicial, horas)
  
    def atacar(self):
        print(self.nombre, "utilizar Kamehameha")

    def calcular_poder(self):
        return self.poder_inicial + self.horas*100

    
class Vegeta(Guerrero):
    def __init__(self, nombre: str, poder_inicial: int, horas: int):
        super().__init__(nombre, poder_inicial, horas)

    def atacar(self):
        print(self.nombre, "utilizar final flash")

    def calcular_poder(self):
        return self.poder_inicial + self.horas*150

goku = Goku("Gran goku", 150, 50)
vegeta = Vegeta("Vegeta", 200, 80)
goku.atacar()
vegeta.atacar()
goku.calcular_poder()
vegeta.calcular_poder()
print(goku.calcular_poder())
print(vegeta.calcular_poder())