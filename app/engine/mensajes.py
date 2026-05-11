from abc import ABC, abstractmethod

class MensajeroClases(ABC):
    
    def subida_niveles(self, nombre, cantidad):
        return f"{nombre} subio {cantidad} niveles!"
    
    def obtener_xp(self, nombre, cantidad):
        return f"\n{nombre} recibio {cantidad} puntos de XP!\n"
    
    def mostrar_vida_restante(self, nombre, vida):
        return f"\nVida restante de {nombre} : {vida}"
    
    def falta_mana(self, nombre, habilidad):
        return f"\n{nombre} no tiene suficiente magia para {habilidad}!\n"
    
    def habilidad_inexistente(self):
        return "\nLa opcion elegida no existe en el rango de habilidades\n"

    def formato_estadisticas(self, p) -> str:
        return (
            f"\n{'='*50}\n"
            f"CLASE: {p.clase} | NOMBRE: {p.nombre} | NIVEL: {p.nivel} | Dinero: {p.dinero}\n" 
            f"{'-'*50}\n"
            f"Vida Max: {p.vida} | Defensa: {p.defensa} | Def. Mágica: {p.defensa_magica} | Atk. Magico: {p.ataque_magico}\n"
            f"Ataque: {p.ataque} | Magia: {p.magia} | Agilidad: {p.agilidad}\n"
            f"{'='*50}\n"
    )
    @abstractmethod
    def mensaje_defenderse(self) -> str:
        pass
    
    @abstractmethod
    def mensaje_defensa_magica(self) -> str:
        pass
    
    @abstractmethod
    def mensaje_defensa_fisica(self) -> str:
        pass
    
    @abstractmethod
    def mensaje_muerte(self) -> str:
        pass

class MensajeroVacio (MensajeroClases):
    def mensaje_defenderse(self) -> str:
        return "Defensa!"
    
    def mensaje_defensa_magica(self) -> str:
        return "Defensa magica!"
    
    def mensaje_defensa_fisica(self) -> str:
        return "Defensaje fisica!"
    
    def mensaje_muerte(self) -> str:
        return "Ya no puede pelear mas..."

class MensajeroGuerrero(MensajeroClases):
    
    def mensaje_defenderse(self) -> str:
        return "Flexion de musculos! AHHH!"
    
    def mensaje_defensa_magica(self) -> str:
        return "Ja! Ser mas fuerte que tus trucos de feria!"
    
    def mensaje_defensa_fisica(self) -> str:
        return "Mis musculos ser mas fuertes que eso..."
    
    def mensaje_muerte(self) -> str:
        return "Pero todavia poder...pelear..."

class MensajeroMago(MensajeroClases):
    
    def mensaje_defenderse(self) -> str:
        return "Glifo de proteccion!"
    
    def mensaje_defensa_magica(self) -> str:
        return "Me insulta que intentes usar eso contra mi..."
    
    def mensaje_defensa_fisica(self) -> str:
        return "Ja! Los abdominales ya estan haciendo efecto."
    
    def mensaje_muerte(self) -> str:
        return "Ah! Al menos mi nombre no sera olvidado..."

class MensajeroStrider(MensajeroClases):
    
    def mensaje_defenderse(self) -> str:
        return "Dale, a ver si lo siento."
    
    def mensaje_defensa_magica(self) -> str:
        return "Seguro que no te equivocaste al pronunciarlo...?"
    
    def mensaje_defensa_fisica(self) -> str:
        return "Demasiado lento!"
    
    def mensaje_muerte(self) -> str:
        return "Fue divertido..."

class MensajeroBatalla():

    def agilidad(self, nombre):
        return f"\n{nombre} es mas agil! Empieza primero."
    
    def batalla_terminada(self, nombre):
        return f"\nBatalla terminada! El ganador es...{nombre}"
    
    def turno_ataque(self, nombre):
        return f"\n{nombre}! Ahora! Es tu turno de atacar... \n"
    
    def vida_restante(self, atacante, defensor):
        return f"Te quedan {atacante} PV, y al otro {defensor}\n"
    
    def acciones(self):
        return "\n\n1)Atacar\n2)Defender\n3)Habilidades\n4)Rendirse\n\nIngrese la accion: "

    def ingreso_invalido(self):
        return "\nEntrada inválida. Debe ser un número.\n"
    
    def opcion_incorrecta(self):
        return "\nOpcion incorrecta.\n"
    
    def limpieza_pantalla(self):
        return "\nPresioná Enter para continuar..."
    
    def elegir_habilidad(self):
        return "\nIngrese el numero de la habilidad: "
    
    def sin_habilidades(self):
        return "\nNo tienes habilidades disponibles.\n"