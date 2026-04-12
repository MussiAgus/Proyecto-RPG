"""
En este, lo que hice fue jugar con los tipos de clases (padres, hijos), de manera que pueda optimizar un poco de codigo.
También intentaré investigar como es el tema del polimorfismo, y como puede ayudarme a mejorar las clases.
Actualizacion: El polimorifsmo es espectacular. No entendia como usar una funcion para todos en la clase padre, pero sin perder los mensajes. Pero con esto se soluciona todo.
"""

import random
from ..engine.ataque import Ataque

class Personaje:
    def __init__(self, nombre, clase, vida, defensa, defensa_magica, ataque, agilidad, magia, ataque_magico):
        self.nombre=nombre
        self.clase=clase
        self.nivel=1
        self.vida=vida
        self.vida_restante=self.vida
        self.defensa=defensa
        self.defensa_magica= defensa_magica
        self.ataque=ataque
        self.agilidad=agilidad
        self.magia=magia
        self.magia_restante=magia
        self.ataque_magico=ataque_magico
        self.experiencia_necesaria = 10
        self.experiencia_actual = 0
        self.experiencia_otorgada = 0
        self.esta_defendiendo = False
        self.es_jugador = False

    def subir_nivel(self, niveles):
        puntos_vida, puntos_defensa, puntos_defensa_magica, puntos_ataque, puntos_ataque_magico, puntos_agilidad, puntos_magia = self.aumentos_especificos()
        for indice in range(niveles):
            self.nivel+=1
            self.vida += (puntos_vida + random.randint(1, 3))
            self.defensa +=(puntos_defensa + random.randint(0, 2))
            self.defensa_magica+= (puntos_defensa_magica + random.randint(0, 2))
            self.ataque += (puntos_ataque + random.randint(0, 2))
            self.ataque_magico+=(puntos_ataque_magico + random.randint(0, 3))
            self.agilidad+= (puntos_agilidad + random.randint(1,2))
            self.magia+= (puntos_magia + random.randint(1,4))
        
        self.magia_restante=self.magia
        self.vida_restante=self.vida
        print(f"{self.nombre} subio {niveles} niveles!")

    def mostrar_estadisticas(self):
        print(f"\nClase: {self.clase}   Nombre: {self.nombre}   Nivel: {self.nivel}\n")
        print(f"Vida_Max: {self.vida}   Defensa: {self.defensa}   Defensa Magica: {self.defensa_magica}\n")
        print(f"Ataque: {self.ataque}   Agilidad: {self.agilidad}   Magia: {self.magia}   Ataque Magico:{self.ataque_magico}\n")
    
    def recibir_xp(self, experiencia):
        
        self.experiencia_actual+=experiencia
        niveles_agregados=0

        while self.experiencia_actual >= self.experiencia_necesaria:
            self.experiencia_actual -= self.experiencia_necesaria
            niveles_agregados+=1
            self.experiencia_necesaria+= (int(self.experiencia_necesaria*0.4))
        
        if niveles_agregados>0: self.subir_nivel(niveles_agregados)
    
    def recibir_danio(self, ataque):

        if(self.esta_defendiendo): 
            ataque["valor"]= ataque["valor"] // 2
            self.esta_defendiendo = False

        if ataque["tipo"]=="Magico":
            if ataque["valor"]>self.defensa_magica:
                self.vida_restante-=ataque["valor"]-self.defensa_magica
            else:
                self.mensaje_defensa_magica()
        else: 
            if ataque["valor"]>self.defensa:
                self.vida_restante-=ataque["valor"]-self.defensa
            else:
                self.mensaje_defensa_fisica()
        
        print(f"\nVida restante de {self.nombre} : {self.vida_restante if self.vida_restante>0 else 0}")
        if(self.vida_restante<=0): self.muerte()
    
    def generador_ataque(self, tipo, tipo_danio):
        
        self.esta_defendiendo = False
        return {
            "tipo": tipo,
            "valor": int(tipo_danio + tipo_danio * random.random())
        }

    def defenderse(self):
        self.mensaje_defenderse()
        self.esta_defendiendo = True

    def muerte(self):
        self.mensaje_muerte()
        self.experiencia_otorgada = self.nivel* random.randint(2,4)



