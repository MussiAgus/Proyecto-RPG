import mysql.connector
from mysql.connector import Error
import time


class DBManager:
    def __init__(self):
        self.config = {
            'host': 'db',
            'user': 'usuario_rpg',
            'password': 'proyecto_rpg',
            'database': 'rpg_db'
        }

    def conectar(self):
        
        intentos = 10
        while intentos > 0:
            try:
                conexion = mysql.connector.connect(**self.config)
                if conexion.is_connected():
                    #print("conectado a la bd")
                    return conexion
            except Error as e:
                print(f"Base de datos no lista (quedan {intentos} intentos)...")
                time.sleep(5)
                intentos -= 1
        
        print("No se pudo conectar a la base de datos tras varios intentos.")
        return None

    def guardar_inventario_y_habilidades(self, cursor, personaje_id, objetos, habilidades):
    # 1. Guardar Habilidades
    # Limpiamos habilidades previas para evitar duplicados
        cursor.execute("DELETE FROM habilidades WHERE personaje_id = %s", (personaje_id,))
    
        query_hab = "INSERT INTO habilidades (personaje_id, nombre_clase) VALUES (%s, %s)"
    
    # CRUCIAL: Guardamos el nombre de la clase (__class__.__name__), no el objeto
        datos_hab = [(personaje_id, h.__class__.__name__) for h in habilidades]
    
        if datos_hab:
            cursor.executemany(query_hab, datos_hab)

    # 2. Guardar Inventario
        cursor.execute("DELETE FROM inventario WHERE personaje_id = %s", (personaje_id,))
    
        query_inv = "INSERT INTO inventario (personaje_id, nombre_clase, cantidad) VALUES (%s, %s, %s)"
    
    # Aquí lo mismo: guardamos el nombre de la clase del ítem
        datos_inv = [
            (personaje_id, slot["item"].__class__.__name__, slot["cantidad"]) 
            for slot in objetos
        ]
    
        if datos_inv:
            cursor.executemany(query_inv, datos_inv)

    def guardar_personaje(self, personaje):
        conexion = self.conectar()
        if conexion:
            cursor = conexion.cursor()
            
            query = """
            INSERT INTO personaje 
            (nombre, clase, nivel, experiencia, vida_max, defensa, ataque, agilidad, defensa_magica, ataque_magico, magia_max, stamina_max, dinero)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                personaje.nombre, 
                personaje.clase, 
                personaje.nivel,
                personaje.experiencia_actual,
                personaje._vida,
                personaje._defensa,
                personaje._ataque,
                personaje._agilidad,
                personaje._defensa_magica,
                personaje._ataque_magico,
                personaje._magia,
                personaje._stamina,
                personaje._dinero
            )
            cursor.execute(query, valores)
            
            personaje_id = cursor.lastrowid
            self.guardar_inventario_y_habilidades(cursor, personaje_id,personaje.objetos,personaje.habilidades)

            conexion.commit() #Sin esto no se guardan los cambios
            cursor.close()
            conexion.close()
            print(f"¡{personaje.nombre} guardado en la DB!")

    def mostrar_personajes_creados(self):
        conexion = self.conectar()
        if not conexion:
            print("Error al acceder a la base de datos.")
            return
        cursor = None
        try:
            cursor = conexion.cursor()
            query = "SELECT nombre, clase, nivel FROM personaje"
            cursor.execute(query)
            personajes = cursor.fetchall()
            if personajes:
                for personaje in personajes:
                    nombre, clase, nivel = personaje
                    print(f"Nombre {nombre} -- Clase {clase} -- nivel {nivel}\n")
            else:
                print("No hay personajes en la BD.")
        except Error as e:
            print(f"Error al leer personajes:{e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conexion.is_connected():
                conexion.close()

    def buscar_nombre (self, nombre) -> bool:
        conexion = self.conectar()
        if not conexion:
            print("Error al acceder a la base de datos.")
            return False
        cursor = None
        try:
            cursor = conexion.cursor()
            query = "SELECT nombre FROM personaje WHERE nombre = %s"
            cursor.execute(query,(nombre, ))
            personaje = cursor.fetchone()
        except Error as e:
            print(f"Error al cargar personaje. -> {e}")
            personaje = None
        finally:
            if cursor is not None:
                cursor.close()
            if conexion.is_connected():
                conexion.close()
        
        if personaje == None : return False
        else : return True

    def cargar_personaje(self, nombre :str):
        conexion=self.conectar()
        
        if not conexion:
            print("No se pudo acceder a la base de datos")
            return None, [], []
        
        cursor = None

        lista_objetos_db = []
        lista_habilidades_db = []
        try:
            cursor = conexion.cursor()
            
            #Datos personaje

            query = "SELECT id, nombre, clase, nivel, experiencia, vida_max, defensa, ataque, agilidad, defensa_magica, ataque_magico, magia_max, stamina_max, dinero FROM personaje WHERE nombre= %s"
            cursor.execute(query,(nombre,))
            datos_personaje = cursor.fetchone()
            
            if not datos_personaje:
                return None, [], []

            #Objetos

            personaje_id = int(datos_personaje[0]) #type:ignore
            query = "SELECT nombre_clase, cantidad FROM inventario WHERE personaje_id = %s"
            cursor.execute(query, (personaje_id,))
            lista_objetos_db = cursor.fetchall()

            #Habilidades

            query = "SELECT nombre_clase FROM habilidades WHERE personaje_id = %s"
            cursor.execute(query, (personaje_id,))
            lista_habilidades_db = cursor.fetchall()

        except Error as e:
            print(f"Error al cargar personaje. -> {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conexion.is_connected():
                conexion.close()
        
        return datos_personaje, lista_objetos_db, lista_habilidades_db
    
    def borrar_personaje(self, nombre: str):
        conexion = self.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "DELETE FROM personaje WHERE nombre = %s"
                cursor.execute(query, (nombre,))
                conexion.commit()
                if cursor.rowcount > 0:
                    print(f"¡Personaje '{nombre}' eliminado correctamente!")
                else:
                    print(f"No se encontró al personaje '{nombre}'.")
            except Error as e:
                print(f"Error al intentar borrar: {e}")
            finally:
                cursor.close()
                conexion.close()

    def actualizar_personaje(self, personaje):
        conexion=self.conectar()
        if not conexion:
            print("No se pudo acceder a la base de datos")
            return None
        
        cursor = None
        try:
            cursor = conexion.cursor(dictionary=True)

            query = """
                UPDATE personaje SET
                    clase = %s,
                    nivel = %s,
                    experiencia = %s,
                    vida_max = %s,
                    defensa = %s,
                    ataque = %s,
                    agilidad = %s,
                    defensa_magica = %s, 
                    ataque_magico = %s, 
                    magia_max = %s,
                    stamina_max = %s,
                    dinero = %s
                WHERE nombre = %s
            """
            valores = (
                personaje.clase,
                personaje.nivel,
                personaje.experiencia_actual,
                personaje._vida,
                personaje._defensa,
                personaje._ataque,
                personaje._agilidad,
                personaje._defensa_magica,
                personaje._ataque_magico,
                personaje._magia,
                personaje._stamina,
                personaje._dinero,
                personaje.nombre             
            )
            cursor.execute(query, valores)

            query = "SELECT id FROM personaje WHERE nombre = %s"
            cursor.execute(query, (personaje.nombre,))
            resultado = cursor.fetchone()
            if resultado:
                self.guardar_inventario_y_habilidades(cursor, resultado['id'],personaje.objetos,personaje.habilidades) #type:ignore

            conexion.commit()
            print("\nPersonaje Actualizado!\n")

        except Error as e:
            print(f"Error al actualizar: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conexion.is_connected():
                conexion.close()