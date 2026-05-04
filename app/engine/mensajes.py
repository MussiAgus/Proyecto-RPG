from abc import ABC, abstractmethod

class Mensajero(ABC):
    """Clase base abstracta para mensajes de personajes."""
    
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

class MensajeroVacio (Mensajero):
    def mensaje_defenderse(self) -> str:
        return "Defensa!"
    
    def mensaje_defensa_magica(self) -> str:
        return "Defensa magica!"
    
    def mensaje_defensa_fisica(self) -> str:
        return "Defensaje fisica!"
    
    def mensaje_muerte(self) -> str:
        return "Ya no puede pelear mas..."

class MensajeroGuerrero(Mensajero):
    
    def mensaje_defenderse(self) -> str:
        return "Flexion de musculos! AHHH!"
    
    def mensaje_defensa_magica(self) -> str:
        return "Ja! Ser mas fuerte que tus trucos de feria!"
    
    def mensaje_defensa_fisica(self) -> str:
        return "Mis musculos ser mas fuertes que eso..."
    
    def mensaje_muerte(self) -> str:
        return "Pero todavia poder...pelear..."


class MensajeroMago(Mensajero):
    
    def mensaje_defenderse(self) -> str:
        return "Glifo de proteccion!"
    
    def mensaje_defensa_magica(self) -> str:
        return "Me insulta que intentes usar eso contra mi..."
    
    def mensaje_defensa_fisica(self) -> str:
        return "Ja! Los abdominales ya estan haciendo efecto."
    
    def mensaje_muerte(self) -> str:
        return "Ah! Al menos mi nombre no sera olvidado..."


class MensajeroStrider(Mensajero):
    
    def mensaje_defenderse(self) -> str:
        return "Dale, a ver si lo siento."
    
    def mensaje_defensa_magica(self) -> str:
        return "Seguro que no te equivocaste al pronunciarlo...?"
    
    def mensaje_defensa_fisica(self) -> str:
        return "Demasiado lento!"
    
    def mensaje_muerte(self) -> str:
        return "Fue divertido..."