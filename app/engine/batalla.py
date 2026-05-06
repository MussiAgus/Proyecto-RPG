from  app.entidades.personaje import Personaje
from app.engine.mensajes import MensajeroBatalla
import os

class Batalla:
    def __init__(self, personaje_1: Personaje , personaje_2: Personaje):
        self.pj_1 = personaje_1
        self.pj_2 = personaje_2
        self.mensajero = MensajeroBatalla()
        self.turno = 0

    def elegir_orden(self, primero : Personaje, segundo: Personaje) -> tuple:
        if(self.turno % 2 == 0):
            return primero, segundo
        else:
            return segundo, primero

    def elegir_inicio(self) -> int:
        if(self.pj_1.agilidad >= self.pj_2.agilidad):
            print(self.mensajero.agilidad(self.pj_1.nombre))
            return 0
        else:
            print(self.mensajero.agilidad(self.pj_2.nombre))
            return 1 

    def comienzo(self):
        self.pj_1.es_jugador = True
        self.turno = self.elegir_inicio()

        while(self.pj_1.vida_restante >0 and self.pj_2.vida_restante>0):

            atacante, defensor = self.elegir_orden(self.pj_1,self.pj_2)

            atacante.procesar_efectos()
            if(atacante.vida_restante<=0): break

            if(atacante.es_jugador):
                print(self.mensajero.turno_ataque(atacante.nombre))
                print(self.mensajero.vida_restante(atacante.vida_restante, defensor.vida_restante))
                self.elegir_accion(atacante, defensor)
            
            else:
                self.accion_random(atacante, defensor)
                self.pausa_y_limpia()
            
            if(defensor.vida_restante<=0): break
            self.turno+=1
        
        if(self.pj_1.vida_restante > 0):
            ganador, perdedor = self.pj_1, self.pj_2
        else: 
            ganador, perdedor = self.pj_2, self.pj_1
            
        print(self.mensajero.batalla_terminada(ganador.nombre))
        self.repartir_xp(ganador,perdedor)

    def repartir_xp(self, ganador: Personaje, perdedor: Personaje) -> None:
        ganador.recibir_xp(perdedor.experiencia_otorgada)

    #Esto hay que desarrollarlo mas. Pero despues.
    def accion_random(self, atacante: Personaje, defensor: Personaje) -> None:
        print(f"{atacante.nombre} te esta atacando!")
        danio = atacante.ataque_basico()
        if danio:
            defensor.recibir_danio(danio)

    def accion_1(self, atacante, defensor):
        defensor.recibir_danio(atacante.ataque_basico())

    def accion_2(self, atacante):
        atacante.defenderse()
    
    def accion_3(self, atacante, defensor):
        if not atacante.habilidades:
            print(self.mensajero.sin_habilidades())
            self.pausa_y_limpia()
            return False
                
        atacante.mostrar_habilidades()
        try:
            indice_habilidad = int(input(self.mensajero.elegir_habilidad()))
            resultado = atacante.ejecutar_habilidad(indice_habilidad, defensor)
            if resultado:
                return True
            else: 
                self.pausa_y_limpia()
                
        except (ValueError, IndexError):
            print(self.mensajero.ingreso_invalido())
            self.pausa_y_limpia()
            return False

    def accion_4(self, atacante):
        atacante.muerte()
        
    def elegir_accion(self, atacante: Personaje, defensor: Personaje) -> None:
        while True:
            opcion = input(self.mensajero.acciones())
            if opcion == "1":
                self.accion_1(atacante,defensor)
                break
            elif opcion == "2":
                self.accion_2(atacante)
                break
            elif opcion == "3":
                if self.accion_3(atacante,defensor) :
                    break
            elif opcion == "4":
                self.accion_4(atacante)
                break
            else:
                print(self.mensajero.opcion_incorrecta())
                self.pausa_y_limpia()

    def pausa_y_limpia(self) -> None:
        input(self.mensajero.limpieza_pantalla())
        os.system('cls' if os.name == 'nt' else 'clear')
