from .personaje import Personaje
from app.engine.mensajes import MensajeroGuerrero

class Berserker(Personaje):
    def __init__(self, nombre):
        super().__init__(
            nombre=nombre,
            clase="Berserker",
            vida=300,
            defensa=20,
            ataque=30,
            agilidad=15,
            defensa_magica= 5,
            ataque_magico=0,
            magia=0,
            mensajero=MensajeroGuerrero()
            )

    def ataque_basico(self):
        return self.generador_ataque("Fisico", self.ataque)

    def mostrar_especiales(self):
        pass
    
    def aumentos_especificos(self) -> tuple:
        return (15,4,1,5,0,1,0,4)