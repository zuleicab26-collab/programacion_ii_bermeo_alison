from abc import ABC, abstractmethod

class NaveEspacial(ABC):
    modelo: str
    def __init__(self, modelo: str):
        self.modelo = modelo

    @abstractmethod
    def despegar(self):
        pass


class NaveCapsula(NaveEspacial):
    def __init__(self, modelo: str):
        super().__init__(modelo)

    def despegar(self):
        print(self.modelo, "despegar con motores de Capsula Corp")

class NaveSayayin(NaveEspacial):
    def __init__(self, modelo: str):
        super().__init__(modelo)

    def despegar(self):
        print(self.modelo, "despegar inmediatamente")

nave_bluma = NaveCapsula("Nave de Capsula")
nave_vegeta = NaveSayayin("Capsula Sayayin")

nave_bluma.despegar()
nave_vegeta.despegar()