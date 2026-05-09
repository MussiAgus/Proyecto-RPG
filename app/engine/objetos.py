import random

clases_permitidas = {
    "todos": ["Todos"],
    "magicos": ["Mago"],
    "fisicos": ["Berserker", "Strider"],
    "Armadura_liviana": ["Mago", "Strider"],
    "Armadura_media": ["Strider","Berserker"],
    "Armadura_pesada": ["Berserker"]
}

catalogo_tienda = {
    "Pociones de vida": ["Pocion_menor","Pocion_media","Pocion_mayor","Pocion_MAX"],
    "Pociones de mana": ["Pocion_mana_menor","Pocion_mana_media","Pocion_mana_mayor","Pocion_mana_MAX"]
}

class Objeto:
    def __init__(self, nombre, costo, categoria, probabilidad, nivel_desbloqueo, clase_permitida):
        self.nombre = nombre
        self.costo = costo
        self.costo_venta = self.costo/2 + self.costo * 0.30
        self.categoria = categoria
        self.probabilidad = probabilidad
        self.nivel_desbloqueo = nivel_desbloqueo
        self.clase_permitida = clase_permitida
    
    def validar_uso(self, jugador):
        lista_permitida = clases_permitidas.get(self.clase_permitida, [])
        
        if jugador.clase in lista_permitida or self.clase_permitida == "todos":
            return True
        else:
            print(f"El objeto {self.nombre} no puede ser usado por un {jugador.nombre}.")
            return False

    def usar(self, jugador, objetivo=None):
        pass

class Obj_curacion(Objeto):
    def __init__(self, nombre, costo, probabilidad, nivel_desbloqueo, clase_permitida):
        super().__init__(nombre, costo, "curacion", probabilidad, nivel_desbloqueo, clase_permitida)

class Obj_powerUp(Objeto):
    def __init__(self, nombre, costo, probabilidad, nivel_desbloqueo, clase_permitida):
        super().__init__(nombre, costo, "powerup", probabilidad, nivel_desbloqueo, clase_permitida)

class Obj_ataque(Objeto):
    def __init__(self, nombre, costo, probabilidad, nivel_desbloqueo, clase_permitida):
        super().__init__(nombre, costo, "ataque", probabilidad, nivel_desbloqueo, clase_permitida)


# POCIONES DE VIDA

class Pocion_menor(Obj_curacion):
    def __init__(self):
        super().__init__(
            nombre = "Pocion menor",
            costo = 10,
            probabilidad = 0.7,
            nivel_desbloqueo= 1,
            clase_permitida = clases_permitidas["todos"]
        )
    
    def usar(self, jugador, objetivo = None):
        carga = 100
        print(f"\nCargando {carga} puntos de vida!\n")
        jugador.vida_restante(carga)

class Pocion_media(Obj_curacion):
    def __init__(self):
        super().__init__(
            nombre = "Pocion media",
            costo = 15,
            probabilidad = 0.55,
            nivel_desbloqueo= 3,
            clase_permitida = clases_permitidas["todos"]
        )
    
    def usar(self, jugador, objetivo = None):
        carga = 150
        print(f"\nCargando {carga} puntos de vida!\n")
        jugador.vida_restante(carga)

class Pocion_mayor(Obj_curacion):
    def __init__(self):
        super().__init__(
            nombre = "Pocion mayor",
            costo = 25,
            probabilidad = 0.3,
            nivel_desbloqueo= 5,
            clase_permitida = clases_permitidas["todos"]
        )
    
    def usar(self, jugador, objetivo = None):
        carga = 300
        print(f"\nCargando {carga} puntos de vida!\n")
        jugador.vida_restante(carga)

class Pocion_MAX(Obj_curacion):
    def __init__(self):
        super().__init__(
            nombre = "Pocion MAX",
            costo = 40,
            probabilidad = 0.2,
            nivel_desbloqueo= 8,
            clase_permitida = clases_permitidas["todos"]
        )
    
    def usar(self, jugador, objetivo = None):
        print(f"\nCargando TODOS tus puntos de vida!\n")
        jugador.vida_restante(jugador.vida)

# POCIONES DE MANA
class Pocion_mana_menor(Obj_curacion):
    def __init__(self):
        super().__init__(
            nombre = "Pocion mana inf.",
            costo = 12,
            probabilidad = 0.7,
            nivel_desbloqueo= 1,
            clase_permitida = clases_permitidas["magicos"]
        )
    
    def usar(self, jugador, objetivo = None):
        carga = 40
        print(f"\nCargando {carga} puntos de mana!\n")
        jugador.magia_restante(carga)

class Pocion_mana_media(Obj_curacion):
    def __init__(self):
        super().__init__(
            nombre = "Pocion mana med.",
            costo = 17,
            probabilidad = 0.55,
            nivel_desbloqueo= 3,
            clase_permitida = clases_permitidas["magicos"]
        )
    
    def usar(self, jugador, objetivo = None):
        carga = 80
        print(f"\nCargando {carga} puntos de mana!\n")
        jugador.magia_restante(carga)

class Pocion_mana_mayor(Obj_curacion):
    def __init__(self):
        super().__init__(
            nombre = "Pocion mana GR.",
            costo = 30,
            probabilidad = 0.3,
            nivel_desbloqueo= 5,
            clase_permitida = clases_permitidas["magicos"]
        )
    
    def usar(self, jugador, objetivo = None):
        carga = 120
        print(f"\nCargando {carga} puntos de mana!\n")
        jugador.magia_restante(carga)

class Pocion_mana_MAX(Obj_curacion):
    def __init__(self):
        super().__init__(
            nombre = "Pocion mana MAX",
            costo = 50,
            probabilidad = 0.2,
            nivel_desbloqueo= 8,
            clase_permitida = clases_permitidas["magicos"]
        )
    
    def usar(self, jugador, objetivo = None):
        print(f"\nCargando TODOS tus puntos de mana!\n")
        jugador.magia_restante(jugador.magia)

# AUMENTOS DE STATS