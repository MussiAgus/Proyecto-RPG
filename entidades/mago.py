from .base import Personaje

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
            magia=100
            )

    def ataque_basico(self):
        
        if(self.magia_restante>=20):
            self.magia_restante-=20
            return self.generador_ataque("Magico", self.ataque_magico) 
        else:
            return self.generador_ataque("Fisico", self.ataque)

    def mostrar_especiales(self):
        pass
    
    def aumentos_especificos(self):
        return (5,1,4,1,4,1,6)

    def mensaje_defenderse(self):
        print("Glifo de proteccion!")

    def mensaje_defensa_magica(self):
        print(f"Me insulta que intentes usar eso contra mi...")
    
    def mensaje_defensa_fisica(self):
        print(f"Ja! Los abdominales ya estan haciendo efecto.")
    
    def mensaje_muerte(self):
        print(f"Ah! Al menos el nombre de {self.nombre} no sera olcidado...")