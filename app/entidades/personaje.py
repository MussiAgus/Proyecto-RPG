
import random
from app.engine.ataque import Ataque
from app.engine.mensajes import MensajeroClases, MensajeroVacio
from abc import ABC, abstractmethod

class Personaje:
    def __init__(self,id, nombre, clase, vida, defensa, defensa_magica, ataque, agilidad, magia, ataque_magico, stamina, dinero, mensajero=None):
        self.id = id
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
        self._stamina = stamina
        self._stamina_restante = stamina
        self._dinero = dinero
        self.dinero_otorgado = 0
        self.efectos_activos=[]
        self.habilidades=[]
        self.objetos = []
        self.experiencia_necesaria = 10
        self.experiencia_actual = 0
        self.experiencia_otorgada = 0
        self.mensajero = mensajero or MensajeroVacio()
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
    
    @property
    def stamina(self) ->int:
        return self._stamina
    
    @property
    def stamina_restante(self):
        return self._stamina_restante
    
    @stamina_restante.setter
    def stamina_restante(self, valor: int) -> None:
        self._stamina_restante = max(0, min(valor, self._stamina))
    
    @property
    def dinero(self):
        return self._dinero
    
    @dinero.setter
    def dinero(self, valor: int) -> None:
        self._dinero = max(0, min(valor, 1000000))

    @abstractmethod
    def ataque_basico(self) -> Ataque:
        pass
    @abstractmethod
    def aumentos_especificos(self) -> tuple:
        pass

    def subir_nivel(self, niveles: int) -> None:
        puntos_vida, puntos_defensa, puntos_defensa_magica, puntos_ataque, puntos_ataque_magico, puntos_agilidad, puntos_magia, puntos_stamina = self.aumentos_especificos()
        for indice in range(niveles):
            self.nivel+=1
            self._vida += (puntos_vida + random.randint(1, 3))
            self._defensa +=(puntos_defensa + random.randint(0, 2))
            self._defensa_magica+= (puntos_defensa_magica + random.randint(0, 2))
            self._ataque += (puntos_ataque + random.randint(0, 2))
            self._ataque_magico+=(puntos_ataque_magico + random.randint(0, 3))
            self._agilidad+= (puntos_agilidad + random.randint(1,2))
            self._magia+= (puntos_magia + random.randint(1,4))
            self._stamina+= (puntos_stamina + random.randint(1,3))
        
        self.magia_restante=self._magia
        self.vida_restante=self._vida
        print(self.mensajero.subida_niveles(self.nombre, niveles))

    def mostrar_estadisticas(self) -> None:
        print(self.mensajero.formato_estadisticas(self))

    def recibir_dinero(self, cantidad):
        self.dinero+=cantidad

    def recibir_xp(self, experiencia: int) -> None:
        
        print(self.mensajero.obtener_xp(self.nombre, experiencia))
        self.experiencia_actual+=experiencia
        niveles_agregados=0

        while self.experiencia_actual >= self.experiencia_necesaria:
            self.experiencia_actual -= self.experiencia_necesaria
            niveles_agregados+=1
            self.experiencia_necesaria+= (int(self.experiencia_necesaria*0.4))
        
        if niveles_agregados>0: self.subir_nivel(niveles_agregados)
    
    def recibir_danio(self, ataque: Ataque) -> None:

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

        print(self.mensajero.mostrar_vida_restante(self.nombre, {self.vida_restante if self.vida_restante>0 else 0}))
        if (self.vida_restante<= 0): self.muerte()
    
    def generador_ataque(self, tipo: str, valor_base: int) -> Ataque:
        self.esta_defendiendo = False
        danio = int(valor_base + valor_base * random.random())
        return Ataque(tipo, danio)

    def mostrar_objetos(self):
        print("\nNum objeto -- Nombre -- Cantidad\n")
        for indice, objeto in enumerate(self.objetos):
            print(f'{indice} -- {objeto["objeto"].nombre} -- {objeto["cantidad"]}\n')

    def usar_objetos(self,enemigo=None, batalla=None):
        indice = int(input("Ingrese el numero de objeto a usar...\n>"))
        if indice >=0 and indice <len(self.objetos):
            dic = self.objetos[indice]

            if dic["objeto"].usar(self,enemigo,batalla):
                dic["cantidad"]-=1
                if dic["cantidad"]==0:
                    self.objetos.pop(indice)
            else:
                print("No usaste el objeto.")
    
    def sumar_objeto(self, objeto, cantidad):
        encontrado = False

        for elemento in self.objetos:            
            if isinstance(elemento, dict) and elemento["objeto"].nombre == objeto.nombre:
                elemento["cantidad"] += cantidad
                encontrado = True
                break
    
        # 2. Si no se encontró, lo agregamos como un nuevo diccionario (slot)
        if not encontrado:
            nuevo_slot = {"objeto": objeto, "cantidad": cantidad}
            self.objetos.append(nuevo_slot)

    def restar_objeto(self, objeto, cantidad):
        # Recorremos con índice para poder eliminar de forma segura
        for i, elemento in enumerate(self.objetos):
            if elemento["objeto"] == objeto: # Asegúrate si la llave es "item" o "objeto"
                elemento["cantidad"] -= cantidad
            
                if elemento["cantidad"] <= 0:
                    self.objetos.pop(i) # pop(i) sí elimina el elemento de la lista
                return True # Objeto encontrado y restado
        return False

    def mostrar_habilidades(self) -> None:
        for i, habilidad in enumerate(self.habilidades):
            print(f"{i} : {habilidad.nombre}")

    def ejecutar_habilidad(self, indice: int, objetivo: 'Personaje') -> bool:
        if 0 <= indice < len(self.habilidades):
            habilidad = self.habilidades[indice]
        
            if self.magia_restante >= habilidad.costo_magia:
                habilidad.usar(self, objetivo)
                return True
            else:
                print(self.mensajero.falta_mana(self.nombre, habilidad.nombre))
                return False
        else :
            print(self.mensajero.habilidad_inexistente())
        return False

    def sumar_habilidad(self, habilidad):
        if habilidad not in self.habilidades:
            self.habilidades.append(habilidad)
        else:
            print(f"Ya conoces la habilidad {habilidad.nombre}")

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
        self.dinero_otorgado = int(self._dinero * (0.5))
        self.dinero-=self.dinero_otorgado