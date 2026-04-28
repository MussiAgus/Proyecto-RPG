class Ataque:
    def __init__(self, tipo, danio, efecto = None):
        self.tipo = tipo
        self.danio_base = danio
        self.efecto = efecto