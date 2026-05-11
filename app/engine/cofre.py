import random
from app.engine.catalogo import catalogo_total

class Cofre:
    @staticmethod
    def generar_botin(personaje):
        posibles = []
        devolucion = ""
        for item in catalogo_total:
            if personaje.nivel >= item.nivel_desbloqueo:
                if hasattr(item, "puede_aprender"): #Esto para habilidad
                    if item.puede_aprender(personaje.clase):
                        posibles.append(item)
                elif hasattr(item, "puede_usar"): #Esto para objeto
                    if item.puede_usar(personaje.clase):
                        posibles.append(item)
                #En el futuro, podria ser un puede_equipar si termino creando armaduras
        if posibles:
            seleccionado = random.choice(posibles)
            
            if hasattr(seleccionado, "puede_aprender"):
                devolucion = "habilidad"
            else:
                devolucion = "objeto"
            return devolucion, seleccionado()
        
        return None