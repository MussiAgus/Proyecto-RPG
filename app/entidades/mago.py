from app.entidades.base import Personaje
from app.engine.habilidad import BolaDeFuego
from app.engine.mensajes import MensajeroMago

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(
            nombre=nombre,
            clase="Mago",
            vida=150,
            defensa=5,
            ataque=5,
            agilidad=10,
            defensa_magica= 25,
            ataque_magico=40,
            magia=100,
            mensajero=MensajeroMago()
            )
        self.habilidades.append(BolaDeFuego())

    def ataque_basico(self):
        if(self.magia_restante>=20):
            self.magia_restante-=20
            return self.generador_ataque("Magico", self.ataque_magico) 
        else:
            return self.generador_ataque("Fisico", self.ataque)
    
    def aumentos_especificos(self) -> tuple:
        return (5,1,4,1,4,1,6)