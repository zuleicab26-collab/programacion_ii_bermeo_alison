from poo_guerrero import Guerrero

class Saiyajin(Guerrero):
    def __init__(self, nombre: str):
        super().__init__(nombre)

    def trasnsformarse(self):        
        print(self.nombre, "transformarse en Super Saiyajin")       


goku = Saiyajin("Goku")
goku.presentarse()
goku.trasnsformarse()

        