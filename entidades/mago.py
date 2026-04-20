from entidades.base import Personaje
from engine.habilidad import BolaDeFuego

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
            )
        self.habilidades=[BolaDeFuego()]

    def ataque_basico(self) -> None:
        if(self.magia_restante>=20):
            self.magia_restante-=20
            return self.generador_ataque("Magico", self.ataque_magico) 
        else:
            return self.generador_ataque("Fisico", self.ataque)

    def mostrar_habilidades(self) -> None:
        for i, habilidad in enumerate(self.habilidades):
            print(f"{i} : {habilidad.nombre}")
    
    def aumentos_especificos(self) -> tuple:
        return (5,1,4,1,4,1,6)

    def mensaje_defenderse(self) -> None:
        print("Glifo de proteccion!")

    def mensaje_defensa_magica(self) -> None:
        print(f"Me insulta que intentes usar eso contra mi...")
    
    def mensaje_defensa_fisica(self) -> None:
        print(f"Ja! Los abdominales ya estan haciendo efecto.")
    
    def mensaje_muerte(self) -> None:
        print(f"Ah! Al menos el nombre de {self.nombre} no sera olcidado...")