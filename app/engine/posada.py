import random

class Posada:
    def __init__(self, personaje):
        self.personaje = personaje
        self.primer_ingreso = False
        #Falta agregar mensajero

    #loop principal
    def recepcion(self):
        
        while True:
            if self.primer_ingreso :
                accion = input(f"Oh! {self.personaje.nombre}, volviste...me alegro!\n1)Descansar y comer\n2)Tienda\n3)Analizar tus estadisticas\n4)Salir de aventura!\n5)Dormir (terminar)\n\n>")
            else:
                self.primer_ingreso = True
                accion = input("Decime, viajero, para que estas aca?\n1)Descansar y comer\n2)Tienda\n3)Analizar tus estadisticas\n4)Salir de aventura!\n5)Dormir (terminar)\n\n>")
            
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
        
        else:
            print("\nPerdon, pero...eh...politicas de la posada. No tenes suficiente dinero.\nPodrias irte de aventuras, no?\n\n")

    def salir_aventuras(self):
        pass

    def entrar_tienda(self):
        pass