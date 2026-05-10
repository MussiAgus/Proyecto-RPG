from app.engine.objetos import catalogo_tienda

class Tienda:
    def __init__(self, personaje):
        self.personaje = personaje
        self.mensajero = None #Despues creo la clase de mensajero para esto
        self.objetos_permitidos_nivel = {}
        self.primer_ingreso = True

    def cargar_objetos_permitidos(self):
        
        for categoria, lista_objetos in catalogo_tienda.items():
            lista_auxiliar_permitidos =[]
            for objeto in lista_objetos:
                if self.personaje.nivel >= objeto.nivel_desbloqueo and objeto.puede_usar(self.personaje.clase):
                    lista_auxiliar_permitidos.append(objeto)
            
            self.objetos_permitidos_nivel[categoria] = lista_auxiliar_permitidos
        
    
    def entrar_tienda(self):
        self.cargar_objetos_permitidos()

        while True:
            if self.primer_ingreso:
                print("Ohh, nuevo comprador...espero que no seas del tipo tacanio, jeje.\n")
                self.primer_ingreso = False
            else:
                print(f"{self.personaje.nombre}! Como te va? Nos conseguiste tesoros...?\n")
            
            accion =input("1)Ver objetos disponibles\n2)Comprar objetos.\n3)Vender objetos.\n4)Volver a la posada\n>")
            
            if accion == "1":
                self.mostrar_objetos_compra()
                continue
            elif accion == "2":
                if self.personaje.dinero>10:
                    self.comprar()
                else:
                    print("Je! Puedo oler que no hay nada en tus bolsillos...volve despues.\n")
                    continue
            elif accion == "3":
                if len(self.personaje.objetos) == 0:
                    print("Claramente viniste sin equipaje. Que pensas venderme? Abrazos?\n")
                    continue
                else:
                    self.vender()
            elif accion == "4":
                print("Nos vemos! Espero ver tus monedas pronto por aca! :D\n")
                break
            else:
                print("Al parecer no entendiste bien lo que dije...")
                continue

    def mostrar_objetos_compra(self): 
        print("Bueno, esto es lo que tengo hoy...\n\n")

        for categoria, lista_objetos in self.objetos_permitidos_nivel.items():
            print(f"==={categoria}===\n")
            for indice, objeto in enumerate(lista_objetos, start=1):
                print(f"{indice}. {objeto.nombre} - {objeto.descripcion} - {objeto.costo} oro\n")

    def seleccionar_objeto_compra(self):
        #Con esto elijo la categoria
        categorias = list(self.objetos_permitidos_nivel.keys())
        for indice, categoria in enumerate(categorias, start=1):
            print(f"{indice}. {categoria}")
        
        opcion_categoria = int(input("Bueno, elegi una categoria...\n>"))
        if opcion_categoria <1 or opcion_categoria>len(categorias):
            print("No no, me mataste...no se que queres.\n")
            return None
        categoria_elegida = categorias[opcion_categoria-1]

        #Con esto elijo el objeto
        lista_objetos = self.objetos_permitidos_nivel[categoria_elegida]
        for indice, objeto in enumerate(lista_objetos, start=1):
            print(f"{indice}. {objeto.nombre} - {objeto.costo} oro\n")

        opcion_objeto = int(input("Que objeto querias?\n>"))
        if opcion_objeto < 1 or opcion_objeto > len(lista_objetos):
            print("Flaco, me estas prestando atencion, al menos?\n")
            return None
        
        objeto_elegido = lista_objetos[opcion_objeto-1]
        return objeto_elegido

    def comprar(self):
        
        objeto = self.seleccionar_objeto_compra()
        if objeto:
            cantidad = int (input("Bien...cuanto te pensas llevar de eso?\n>"))
            if (cantidad > 0):
                costo_total = objeto.costo * cantidad
                if(self.personaje.dinero > costo_total):
                    print("\nGenial! Una venta hecha.\n")
                    self.personaje.dinero -= costo_total
                    objeto_convertido = objeto()
                    self.personaje.sumar_objeto(objeto_convertido, cantidad)
                else:
                    print("\nNo no, aca no fiamos. Volve cuando tengas mas plata.\n")
            else:
                print("\nClaro, para que lo escribo en mi maquina de escribir invisible...\n")
        else:
            return None

    def vender(self):
        print("Interesante...espero que tengas muchas cosas raras! Mi curiosidad puede mas que mi apego al oro...\n")
        self.personaje.mostrar_objetos()

        indice = int(input("Que vas a ofrecerme?\nInsertar indice de objeto > "))
        if indice >=0 and indice < len(self.personaje.objetos):

            dic_venta = self.personaje.objetos[indice]
            objeto_venta = dic_venta["objeto"]

            cantidad = int(input("Cuanto de eso vas a darme?\n> "))
            
            if cantidad > 0 and cantidad <= dic_venta["cantidad"]:
                print("Trato hecho!\n")
                oro_ganado = objeto_venta.costo * cantidad
                self.personaje.dinero+=oro_ganado
                self.personaje.restar_objeto(objeto_venta, cantidad)
            else:
                print("No tenes tanto...\n")
                return
        else:
            print("Claro, si me das algo que no existe, entonces yo te doy oro invisible. Te gusta?\n")