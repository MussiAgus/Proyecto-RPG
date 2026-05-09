from .personaje import Personaje
from app.engine.mensajes import MensajeroStrider
import random

class Strider(Personaje):
    def __init__(self, nombre):
        super().__init__(
            nombre=nombre,
            clase="Strider",
            vida=200,
            defensa=10,
            ataque=20,
            agilidad=35,
            defensa_magica= 10,
            ataque_magico=0,
            magia=0,
            stamina = 30,
            dinero = 75, #Ladronzuelo...
            mensajero=MensajeroStrider()
            )

    def ataque_basico(self) :
        danio = self.ataque+(self.agilidad//10 * random.randint(0,3))
        return self.generador_ataque("Fisico", danio)

    def mostrar_especiales(self):
        pass

    def aumentos_especificos(self) -> tuple:
    # (vida, def, def_mag, ataque, ataque_mag, agi, mag)
        return (10, 2, 2, 4, 0, 6, 0, 2)