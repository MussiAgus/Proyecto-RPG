from __future__ import annotations
from typing import TYPE_CHECKING
from app.engine.efectos import Quemado

if TYPE_CHECKING:
    from app.entidades.personaje import Personaje


class Habilidad:
    def __init__(self, nombre, tipo, potencia, costo_magia):
        self.nombre = nombre
        self.tipo = tipo
        self.potencia = potencia
        self.costo_magia = costo_magia
        # Crear costo energia

    def usar(self, atacante: Personaje, defensor: Personaje) -> None:
        ataque = atacante.generador_ataque(self.tipo, self.potencia)
        defensor.recibir_danio(ataque)

class BolaDeFuego(Habilidad):
    def __init__(self):
        super().__init__(
            nombre="Bola de Fuego",
            tipo="Magico",
            potencia=40,
            costo_magia=50
        )

    def usar(self, atacante: Personaje, defensor: Personaje) -> None:
        if atacante.magia_restante < self.costo_magia:
            print(f"¡No tienes suficiente magia! Necesitas {self.costo_magia}, tienes {atacante.magia_restante}")
            return
        
        atacante.magia_restante -= self.costo_magia
        print(f"¡{atacante.nombre} usa {self.nombre}! (Magia restante: {atacante.magia_restante})")
        
        ataque = atacante.generador_ataque(self.tipo, self.potencia)
        defensor.recibir_danio(ataque)
        defensor.efectos_activos.append(Quemado(3))


#atributo para que la habilidad vaya a una clase especifica, y despues se active un selector al azar que le desbloquee una habiliad de esa lista.

#Corte letal (salto con hacha) para el guerrero. Subir defensa durante x cantidad de turnos (Muro de carne).

#Doble flecha (dos golpes) para el strider. Persuasion (Probabilidad de tener dos turnos).

#Siempre al final!

mapeo_habilidades ={
    "BolaDeFuego": BolaDeFuego # pyright: ignore[reportUndefinedVariable]
}