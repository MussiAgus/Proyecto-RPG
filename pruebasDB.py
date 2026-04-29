from app.entidades.berserker import Berserker
from app.entidades.mago import Mago
from app.entidades.strider import Strider
from app.bd.bd_manager import  DBManager

def test_db():
    db = DBManager()

    # 1. Creamos los personajes (instancias de tus clases)
    conan = Berserker(nombre="Conan")
    gandalf = Mago(nombre="Gandalf")
    legolas = Strider(nombre="Legolas")

    # 2. Guardamos en la base de datos
    print("--- Guardando personajes ---")
    db.guardar_personaje(conan)
    db.guardar_personaje(gandalf)
    db.guardar_personaje(legolas)

    # 3. Probamos la carga
    print("\n--- Consultando la base de datos ---")
    db.cargar_personaje("Conan")
    db.cargar_personaje("Gandalf")
    db.cargar_personaje("Legolas")

if __name__ == "__main__":
    test_db()