from  entidades.base import Personaje
import os

class Batalla:
    def __init__(self, personaje_1: Personaje , personaje_2: Personaje):
        self.pj_1 = personaje_1
        self.pj_2 = personaje_2
        self.turno = 0

    def comienzo(self):
        self.pj_1.es_jugador = True
        primero, segundo = self.elegir_orden()
        atacante = primero
        defensor = segundo

        while(True):
            
            if(self.turno % 2 == 0):
                atacante = primero
                defensor = segundo
            else:
                atacante = segundo
                defensor = primero
            
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
        defensor.recibir_danio(atacante.ataque_basico())

    def elegir_accion(self, atacante: Personaje, defensor: Personaje) -> None:
        opcion = input("\n\n Presione 1 para atacar, 2 para defender y 3 para usar habilidades: ")
        if opcion not in ["1", "2","3"]:
            print("Opción inválida")
            return self.elegir_accion(atacante, defensor)
        if(opcion == "1"):
            defensor.recibir_danio(atacante.ataque_basico())
        elif(opcion=="2"):
            atacante.defenderse()
        else:
            atacante.mostrar_habilidades()
            indice_habilidad=int(input("\n Presione el numero correspondiente a la habilidad: "))
            habilidad=atacante.habilidades[indice_habilidad]
            habilidad.usar(atacante, defensor)

    def elegir_orden(self) -> tuple[Personaje,Personaje]:
        if(self.pj_1.agilidad >= self.pj_2.agilidad):
            print(f"\n{self.pj_1.nombre} es mas agil! Empieza primero.\n")
            return self.pj_1, self.pj_2
        else:
            print(f"\n{self.pj_2.nombre} es mas agil! Empieza primero.\n")
            return self.pj_2, self.pj_1 

    def pausa_y_limpia(self) -> None:
        input("\nPresioná Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
