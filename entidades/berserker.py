from .base import Personaje

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
            magia=0
            )

    def ataque_basico(self) -> None:
        return self.generador_ataque("Fisico", self.ataque)

    def mostrar_especiales(self):
        pass
    
    def aumentos_especificos(self) -> tuple:
        return (15,4,1,5,0,1,0)

    def mensaje_defenderse(self) -> None:
        print("Flexion de musculos! AHHH!")

    def mensaje_defensa_magica(self) -> None:
        print(f"Ja! {self.nombre} ser mas fuerte que tus trucos de feria!")
    
    def mensaje_defensa_fisica(self) -> None:
        print(f"Mis musculos ser mas fuertes que eso...")
    
    def mensaje_muerte(self) -> None:
        print(f"Pero {self.nombre} todavia poder...pelear...")