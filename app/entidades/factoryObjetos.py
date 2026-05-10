from app.engine.objetos import mapeo_objetos

    
class ObjetosFactory:
    @staticmethod
    def cargar_inventario(personaje, lista_de_bd):
        for item in lista_de_bd:
            if isinstance(item, dict):
                nombre_clase = item['nombre_clase']
                cantidad = item['cantidad']
            else:
                nombre_clase = item[0]
                cantidad = item[1]

            clase_referencia = mapeo_objetos.get(nombre_clase)
            if clase_referencia:
                item_instanciado = clase_referencia()
                personaje.sumar_objeto(item_instanciado, cantidad)
    