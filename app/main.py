from bd.bd_manager import DBManager
from engine.batalla import Batalla
from entidades.factoryClases import PersonajeFactory

bd = DBManager()
jugador = None
contrincante = PersonajeFactory.crear_personaje("The Boss", "Berserker")

while True:
    opcion = input("1) Crear un personaje.\n 2) Cargar personaje.\n>")
    if(opcion == "1"):
        nombre = input("Cual sera el nombre de tu heroe? \n >")
        clase = input("Y cual sera su especialidad? \n>")
    
        if not bd.buscar_nombre(nombre):
            jugador = PersonajeFactory.crear_personaje(nombre, clase)
            bd.guardar_personaje(jugador)
            print("\nPersonaje creado con exito!\n")
            break
        else:
            print("\nYa hay un personaje con ese nombre. Elegi otro, o eliminalo.\n")
            continue
    
    else:
        bd.mostrar_personajes_creados()

        nombre = input("\nCual es el nombre de tu heroe?\n")
        datos_personaje = bd.cargar_personaje(nombre)
        if datos_personaje:
            jugador = PersonajeFactory.cargar_personaje(datos_personaje)
            break
        else:
            print("No existe un jugador con ese nombre...")
            continue

if jugador is not None:
    jugador.subir_nivel(10)
    pelea = Batalla(jugador,contrincante)
    pelea.comienzo()
else:
    print("No se pudo conseguir un jugador")