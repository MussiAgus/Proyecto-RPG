import random
import time
from app.engine.tienda import Tienda

class Posada:
    def __init__(self, personaje):
        self.personaje = personaje
        self.primer_ingreso = True #Este solamente se usa cuando el personaje entra pro primero vez
        self.ingreso_repetido = False #Este si pasa mucho tiempo, hasta que el personaje vuelve al menu.o 
        #Falta agregar mensajero

    #loop principal
    def recepcion(self):
        
        while True:
            if self.primer_ingreso and not self.ingreso_repetido:
                print("Decime, viajero, para que estas aca?\n")
                self.primer_ingreso = False
            else:
                if not self.ingreso_repetido:
                    print(f"Oh! {self.personaje.nombre}, volviste...me alegro!\n")
                    self.ingreso_repetido = True
            
            accion = input(("\n1)Descansar y comer\n2)Tienda\n3)Analizar tus estadisticas\n4)Salir de aventura!\n5)Dormir (terminar)\n\n>"))

            if accion == "1":
                self.descanso()
                continue
            elif accion == "2":
                self.entrar_tienda()
                continue
            elif accion == "3": 
                self.ver_estadisticas()
                continue
            elif accion == "4":
                self.salir_aventuras()
                continue
            elif accion == "5":
                print("\nEspero vuelvas pronto!\n")
                break
            else:
                print("No ingresaste una opcion valida...preste mas atencion, viajero!")
                continue
        print("Gracias por jugar!")

    def ver_estadisticas(self):
        
        print("\nVer estadisticas...? Claro, a ver, pone las manos aca...\n")
        self.personaje.mostrar_estadisticas()
        
        if self.personaje.nivel <= 5:
            print("\nHey, no te preocupes. Estas recien empezando! Se que vas a ser superfuerte.\n")
        elif self.personaje.nivel >5 and self.personaje.nivel <=15:
            print("\nSe nota tu esfuerzo. Ahora estas mucho mejor!\n")
        elif self.personaje.nivel >15:
            print("\nWow, recuerdo cuando llegaste por primera vez. Creo que hasta yo podria haberte ganado! Pero ahora estas entre los mejores...\n")

    def descanso(self):
        if self.personaje.dinero >= 5:
            self.personaje.dinero-=5;
            self.personaje.vida_restante=self.personaje.vida
            self.personaje.magia_restante=self.personaje.magia
            self.personaje.stamina_restante=self.personaje.stamina
            print(f"5 monedas gastadas.\nTe quedan {self.personaje.dinero}\n\n")
            print(f"Bueno, esta es la llave de la habitacion {random.randint(1,10)}. Espero descanses bien!")
            print("\nDescansando...\n")
            time.sleep(5)
            #Aca me gustaria poner el clima, pero que varie de forma random entre palabras de una lista.
            print("Es un nuevo dia! Hoy esta...\n")
            self.ingreso_repetido = False
        else:
            print("\nPerdon, pero...eh...politicas de la posada. No tenes suficiente dinero.\nPodrias irte de aventuras, no?\n\n")

    def salir_aventuras(self):
        pass

    def entrar_tienda(self):
        tienda = Tienda(self.personaje)
        tienda.entrar_tienda()