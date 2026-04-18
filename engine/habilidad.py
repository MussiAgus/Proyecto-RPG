from engine.efectos import Quemado

class Habilidad:
    def __init__(self, nombre, tipo, potencia, costo_magia):
        self.nombre = nombre
        self.tipo = tipo
        self.potencia = potencia
        self.costo_magia = costo_magia

    def usar(self, atacante, defensor):
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


    def usar(self, atacante, defensor):
        ataque = atacante.generador_ataque("Magico", self.potencia)
        defensor.recibir_danio(ataque)
        defensor.efectos_activos.append(Quemado())