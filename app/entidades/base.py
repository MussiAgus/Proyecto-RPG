
import random
from app.engine.ataque import Ataque
from app.engine.mensajes import Mensajero

class Personaje:
    def __init__(self, nombre, clase, vida, defensa, defensa_magica, ataque, agilidad, magia, ataque_magico, mensajero=None):
        self.nombre=nombre
        self.clase=clase
        self.nivel=1
        self._vida=vida
        self._vida_restante=self._vida
        self._defensa=defensa
        self._defensa_magica= defensa_magica
        self._ataque=ataque
        self._agilidad=agilidad
        self._magia=magia
        self._magia_restante=magia
        self._ataque_magico=ataque_magico
        self.efectos_activos=[]
        self.habilidades=[]
        self.experiencia_necesaria = 10
        self.experiencia_actual = 0
        self.experiencia_otorgada = 0
        self.mensajero = mensajero
        self.esta_defendiendo = False
        self.es_jugador = False
    
    @property
    def vida(self) -> int:
        return self._vida
    
    @property
    def vida_restante(self) -> int:
        return self._vida_restante
    
    @vida_restante.setter
    def vida_restante(self, valor: int) -> None:
        self._vida_restante = max(0, min(valor, self._vida))
    
    @property
    def defensa(self) -> int:
        return self._defensa
    
    @property
    def defensa_magica(self) -> int:
        return self._defensa_magica
    
    @property
    def ataque(self) -> int:
        return self._ataque
    
    @property
    def agilidad(self) -> int:
        return self._agilidad
    
    @property
    def magia(self) -> int:
        return self._magia
    
    @property
    def magia_restante(self) -> int:
        return self._magia_restante
    
    @magia_restante.setter
    def magia_restante(self, valor: int) -> None:
        self._magia_restante = max(0, min(valor, self._magia))
    
    @property
    def ataque_magico(self) -> int:
        return self._ataque_magico

    def subir_nivel(self, niveles: int) -> None:
        puntos_vida, puntos_defensa, puntos_defensa_magica, puntos_ataque, puntos_ataque_magico, puntos_agilidad, puntos_magia = self.aumentos_especificos()
        for indice in range(niveles):
            self.nivel+=1
            self._vida += (puntos_vida + random.randint(1, 3))
            self._defensa +=(puntos_defensa + random.randint(0, 2))
            self._defensa_magica+= (puntos_defensa_magica + random.randint(0, 2))
            self._ataque += (puntos_ataque + random.randint(0, 2))
            self._ataque_magico+=(puntos_ataque_magico + random.randint(0, 3))
            self._agilidad+= (puntos_agilidad + random.randint(1,2))
            self._magia+= (puntos_magia + random.randint(1,4))
        
        self.magia_restante=self._magia
        self.vida_restante=self._vida
        print(f"{self.nombre} subio {niveles} niveles!")

    def mostrar_estadisticas(self) -> None:
        print(f"\nClase: {self.clase}   Nombre: {self.nombre}   Nivel: {self.nivel}\n")
        print(f"Vida_Max: {self.vida}   Defensa: {self.defensa}   Defensa Magica: {self.defensa_magica}\n")
        print(f"Ataque: {self.ataque}   Agilidad: {self.agilidad}   Magia: {self.magia}   Ataque Magico:{self.ataque_magico}\n")
    
    def recibir_xp(self, experiencia: int) -> None:
        
        self.experiencia_actual+=experiencia
        niveles_agregados=0

        while self.experiencia_actual >= self.experiencia_necesaria:
            self.experiencia_actual -= self.experiencia_necesaria
            niveles_agregados+=1
            self.experiencia_necesaria+= (int(self.experiencia_necesaria*0.4))
        
        if niveles_agregados>0: self.subir_nivel(niveles_agregados)
    
    def recibir_danio(self, ataque: int) -> None:

        danio = ataque.danio_base

        if (self.esta_defendiendo): 
            danio = danio // 2
            self.esta_defendiendo = False

        if (ataque.tipo == "Magico"):
            if (danio > self.defensa_magica):
                self.vida_restante -= danio - self.defensa_magica
            else:
                print(f"{self.mensajero.mensaje_defensa_magica()}")
        else: 
            if (danio > self.defensa):
                self.vida_restante -= danio - self.defensa
            else:
                print(f"{self.mensajero.mensaje_defensa_fisica()}")

        print(f"\nVida restante de {self.nombre} : {self.vida_restante if self.vida_restante>0 else 0}")
        if (self.vida_restante<= 0): self.muerte()
    
    def generador_ataque(self, tipo: str, valor_base: int) -> Ataque:
        self.esta_defendiendo = False
        danio = int(valor_base + valor_base * random.random())
        return Ataque(tipo, danio)

    def mostrar_habilidades(self) -> None:
        for i, habilidad in enumerate(self.habilidades):
            print(f"{i} : {habilidad.nombre}")

    def defenderse(self) -> None:
        print(f"{self.mensajero.mensaje_defenderse()}")
        self.esta_defendiendo = True

    def procesar_efectos(self) -> None:
        for efecto in self.efectos_activos[:]:
            efecto.aplicar(self)
            if efecto.duracion <= 0:
                self.efectos_activos.remove(efecto)

    def muerte(self) -> None:
        self.vida_restante=0
        print(f"{self.mensajero.mensaje_muerte()}")
        self.experiencia_otorgada = self.nivel* random.randint(2,4)



