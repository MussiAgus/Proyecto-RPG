from app.entidades.personaje import Personaje

class Efecto:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

    def aplicar(self, personaje):
        pass

class Quemado(Efecto):
    def __init__(self, duracion):
        super().__init__("Quemado", duracion)

    def aplicar(self, personaje: Personaje) ->None:
        danio = 10
        personaje.vida_restante -= danio
        print(f"{personaje.nombre} sufre {danio} de daño por quemadura!")
        self.duracion -= 1
        