from app.entidades.berserker import Berserker
from app.entidades.mago import Mago
from app.entidades.strider import Strider


class PersonajeFactory:
    @staticmethod
    def crear_personaje(nombre, clase, id=None):
        if clase == 'Mago':
            personaje= Mago(nombre)
        elif clase == 'Berserker':
            personaje = Berserker(nombre)
        elif clase == 'Strider':
            personaje = Strider(nombre)
        
        return personaje

    @staticmethod
    def cargar_personaje(datos_db):
        # id, nom, clase, lvl, xp, vida, defensa, atk, agil, def_mag, atk_mag, mag, sta, din = datos_db
        if not datos_db:
            return None
        
        personaje = PersonajeFactory.crear_personaje(datos_db[1], datos_db[2])
        personaje.id = datos_db[0]
        personaje.nivel = datos_db[3]
        personaje.experiencia_actual = datos_db[4]
        personaje._vida = datos_db[5]
        personaje._defensa = datos_db[6]
        personaje._ataque = datos_db[7]
        personaje._agilidad = datos_db[8]
        personaje._defensa_magica = datos_db[9]
        personaje._ataque_magico = datos_db[10]
        personaje._magia = datos_db[11]
        personaje._stamina = datos_db[12]
        personaje._dinero = datos_db[13]

        return personaje