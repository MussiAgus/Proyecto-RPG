from .base import Personaje
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
            magia=0
            )

    def ataque_basico(self):
        danio = self.ataque+(self.agilidad//10 * random.randint(0,3))
        return self.generador_ataque("Fisico", danio)

    def mostrar_especiales(self):
        pass

    def aumentos_especificos(self):
    # (vida, def, def_mag, ataque, ataque_mag, agi, mag)
        return (10, 2, 2, 4, 0, 6, 0)

    def mensaje_defenderse(self):
        print("Glifo de proteccion!")

    def mensaje_defensa_magica(self):
        print(f"Me insulta que intentes usar eso contra mi...")
    
    def mensaje_defensa_fisica(self):
        print(f"Ja! Los abdominales ya estan haciendo efecto.")
    
    def mensaje_muerte(self):
        print(f"Ah! Al menos el nombre de {self.nombre} no sera olcidado...")