import random


class Objeto:
    # Atributo de clase: Centralizamos las reglas aquí
    REGLAS_CLASES = {
        "todos": ["Mago", "Berserker", "Strider"],
        "magicos": ["Mago"],
        "fisicos": ["Berserker", "Strider"],
        "Armadura_liviana": ["Mago", "Strider"],
        "Armadura_media": ["Strider", "Berserker"],
        "Armadura_pesada": ["Berserker"]
    }

    rango = "Normal"
    nombre = ""
    descripcion = ""
    costo = 0
    probabilidad = 0
    nivel_desbloqueo = 1
    clase_permitida = "todos" # Guardamos la "llave", no la lista

    @property
    def costo_venta(self):
        return int(self.costo * 0.6)
    
    @classmethod
    def puede_usar(cls, personaje_clase):
        permitidos = cls.REGLAS_CLASES.get(cls.clase_permitida, [])
        return personaje_clase in permitidos

    def usar(self, jugador, objetivo=None, batalla = None):
        pass

# POCIONES DE VIDA

class Pocion_menor(Objeto):
    nombre = "Pocion menor"
    descripcion = "Cura 100 pts. de vida."
    costo = 10
    probabilidad = 0.7
    nivel_desbloqueo= 1
    clase_permitida = "todos"
    
    def usar(self, jugador):
        if(jugador.vida_restante == jugador.vida):
            print("\nPero la vida esta completa!\n")
            return False
        carga = 100
        print(f"\nCargando {carga} puntos de vida!\n")
        jugador.vida_restante+=carga
        return True

class Pocion_media(Objeto):

    nombre = "Pocion media"
    descripcion = "Cura 150 pts. de vida."
    costo = 15
    probabilidad = 0.55
    nivel_desbloqueo= 3
    clase_permitida = "todos"
    
    def usar(self, jugador):
        if(jugador.vida_restante == jugador.vida):
            print("\nPero la vida esta completa!\n")
            return False
        carga = 150
        print(f"\nCargando {carga} puntos de vida!\n")
        jugador.vida_restante+=carga
        return True

class Pocion_mayor(Objeto):

    nombre = "Pocion mayor"
    descripcion = "Cura 300 pts. de vida."
    costo = 25
    probabilidad = 0.3
    nivel_desbloqueo= 5
    clase_permitida ="todos"
    
    def usar(self, jugador):
        if(jugador.vida_restante == jugador.vida):
            print("\nPero la vida esta completa!\n")
            return False
        carga = 300
        print(f"\nCargando {carga} puntos de vida!\n")
        jugador.vida_restante+=carga
        return True

class Pocion_MAX(Objeto):

    rango = "Medio"
    nombre = "Pocion MAX"
    descripcion = "Cura TODA la vida."
    costo = 40
    probabilidad = 0.2
    nivel_desbloqueo= 8
    clase_permitida = "todos"
    
    def usar(self, jugador):
        if(jugador.vida_restante == jugador.vida):
            print("\nPero la vida esta completa!\n")
            return False
        print(f"\nCargando TODOS tus puntos de vida!\n")
        jugador.vida_restante=jugador.vida
        return True

# POCIONES DE MANA
class Pocion_mana_menor(Objeto):

    nombre = "Pocion mana inf."
    descripcion = "Recupera 40 puntos de mana."
    costo = 12
    probabilidad = 0.7
    nivel_desbloqueo= 1
    clase_permitida = "magicos"
    
    def usar(self, jugador):
        if(jugador.magia_restante == jugador.magia):
            print("\nPero estas rebosante de mana...\n")
            return False
        carga = 40
        print(f"\nCargando {carga} puntos de mana!\n")
        jugador.magia_restante+=carga
        return True

class Pocion_mana_media(Objeto):
    
    nombre = "Pocion mana med."
    descripcion = "Recupera 80 puntos de mana."
    costo = 17
    probabilidad = 0.55
    nivel_desbloqueo= 3
    clase_permitida = "magicos"
    
    def usar(self, jugador):
        if(jugador.magia_restante == jugador.magia):
            print("\nPero estas rebosante de mana...\n")
            return False
        carga = 80
        print(f"\nCargando {carga} puntos de mana!\n")
        jugador.magia_restante+=carga
        return True

class Pocion_mana_mayor(Objeto):
    
    nombre = "Pocion mana GR."
    descripcion = "Recupera 120 puntos de mana."
    costo = 30
    probabilidad = 0.3
    nivel_desbloqueo= 5
    clase_permitida = "magicos"
    
    def usar(self, jugador):
        if(jugador.magia_restante == jugador.magia):
            print("\nPero estas rebosante de mana...\n")
            return False
        carga = 120
        print(f"\nCargando {carga} puntos de mana!\n")
        jugador.magia_restante+=carga
        return True

class Pocion_mana_MAX(Objeto):
    
    nombre = "Pocion mana MAX"
    descripcion = "Recupera TODO el mana."
    costo = 50
    probabilidad = 0.2
    nivel_desbloqueo= 8
    clase_permitida = "magicos"
    
    def usar(self, jugador):
        if(jugador.magia_restante == jugador.magia):
            print("\nPero estas rebosante de mana...\n")
            return False
        print(f"\nCargando TODOS tus puntos de mana!\n")
        jugador.magia_restante=jugador.magia
        return True

# AUMENTOS DE STATS





#Esto siempre tiene que ir al final

catalogo_tienda = {
    "Pociones de vida": [Pocion_menor,Pocion_media,Pocion_mayor,Pocion_MAX],
    "Pociones de mana": [Pocion_mana_menor,Pocion_mana_media,Pocion_mana_mayor,Pocion_mana_MAX]
}

mapeo_objetos = {
    "Pocion_menor": Pocion_menor, # pyright: ignore[reportUndefinedVariable]
    "Pocion_media": Pocion_media, # pyright: ignore[reportUndefinedVariable]
    "Pocion_mayor": Pocion_mayor, # pyright: ignore[reportUndefinedVariable]
    "Pocion_MAX" : Pocion_MAX, # pyright: ignore[reportUndefinedVariable]
    "Pocion_mana_menor" : Pocion_mana_menor, # pyright: ignore[reportUndefinedVariable]
    "Pocion_mana_media" : Pocion_mana_media, # pyright: ignore[reportUndefinedVariable]
    "Pocion_mana_mayor" : Pocion_mana_mayor, # pyright: ignore[reportUndefinedVariable]
    "Pocion_mana_MAX" : Pocion_mana_MAX # pyright: ignore[reportUndefinedVariable]
}