from app.engine.habilidad import mapeo_habilidades


class HabilidadesFactory:
    @staticmethod
    def cargar_habilidades(personaje, lista_habilidades):
        for habilidad in lista_habilidades:
            nombre_clase = habilidad['nombre_clase'] if isinstance(habilidad, dict) else habilidad[0]
            
            clase_referencia = mapeo_habilidades.get(nombre_clase)
            if clase_referencia:
                item_instanciado = clase_referencia()
                personaje.sumar_habilidad(item_instanciado)