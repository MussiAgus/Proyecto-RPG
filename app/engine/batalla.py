from  app.entidades.base import Personaje
import os

class Batalla:
    def __init__(self, personaje_1: Personaje , personaje_2: Personaje):
        self.pj_1 = personaje_1
        self.pj_2 = personaje_2
        self.turno = 0

    def elegir_orden(self, primero : Personaje, segundo: Personaje) -> tuple:
        if(self.turno % 2 == 0):
            return primero, segundo
        else:
            return segundo, primero

    def elegir_inicio(self) -> int:
        if(self.pj_1.agilidad >= self.pj_2.agilidad):
            print(f"\n{self.pj_1.nombre} es mas agil! Empieza primero.\n")
            return 0
        else:
            print(f"\n{self.pj_2.nombre} es mas agil! Empieza primero.\n")
            return 1 

    def comienzo(self):
        self.pj_1.es_jugador = True
        self.turno = self.elegir_inicio()

        while(self.pj_1.vida_restante >0 and self.pj_2.vida_restante>0):

            atacante, defensor = self.elegir_orden(self.pj_1,self.pj_2)

            atacante.procesar_efectos()
            if(atacante.vida_restante<=0): break

            if(atacante.es_jugador):
                print(f"\n{atacante.nombre}! Ahora! Es tu turno de atacar... \n")
                print(f"Te quedan {atacante.vida_restante} PV, y al otro {defensor.vida_restante}\n")
                self.elegir_accion(atacante, defensor)
            else:
                self.accion_random(atacante, defensor)
                self.pausa_y_limpia()
            
            if(defensor.vida_restante<=0): break
            self.turno+=1
        
        print(f"\nBatalla terminada! El ganador es...{self.pj_1.nombre if self.pj_1.vida_restante>0 else self.pj_2.nombre}")
        if(self.pj_1.vida_restante<=0): self.repartir_xp(self.pj_2, self.pj_1)
        else: self.repartir_xp(self.pj_1, self.pj_2)

    def repartir_xp(self, ganador: Personaje, perdedor: Personaje) -> None:
        ganador.recibir_xp(perdedor.experiencia_otorgada)

    def accion_random(self, atacante: Personaje, defensor: Personaje) -> None:
        print(f"{atacante.nombre} te esta atacando!")
        danio = atacante.ataque_basico()
        if danio:
            defensor.recibir_danio(danio)

    def elegir_accion(self, atacante: Personaje, defensor: Personaje) -> None:
        while True:
            opcion = input("\n\n1)Atacar\n2)Defender\n3)Habilidades\n4)Acabar pelea\n\nIngrese la accion: ")
            if opcion == "1":
                defensor.recibir_danio(atacante.ataque_basico())
                break

            elif opcion == "2":
                atacante.defenderse()
                break

            elif opcion == "3":
                if not atacante.habilidades:
                    print("\nNo tienes habilidades disponibles.\n")
                    self.pausa_y_limpia()
                    continue
                
                atacante.mostrar_habilidades()
                try:
                    indice_habilidad = int(input("\nIngrese el numero de la habilidad: "))
                except ValueError:
                    print("\nEntrada inválida. Debe ser un número.\n")
                    self.pausa_y_limpia()
                    continue
                    
                if indice_habilidad >=0 and indice_habilidad < len(atacante.habilidades):
                    habilidad = atacante.habilidades[indice_habilidad]
                    habilidad.usar(atacante,defensor)
                    break
                else:
                    print("\nLa opcion elegida no existe en el rango de habilidades\n")
                    self.pausa_y_limpia()
                    continue
            elif opcion == "4":
                atacante.muerte();
                break
            else:
                print("\nOpcion incorrecta.\n")
                self.pausa_y_limpia()
                continue

    def pausa_y_limpia(self) -> None:
        input("\nPresioná Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
