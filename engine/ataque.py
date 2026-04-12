

class Ataque:
    def __init__(self, tipo, danio, efectos = None):
        self.tipo = tipo
        self.danio_base = danio
        self.efectos = []
    
    def devolver_danio(self):
        return self.tipo, self.danio_base