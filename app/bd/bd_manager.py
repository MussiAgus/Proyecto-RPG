import mysql.connector
from mysql.connector import Error
import time

class DBManager:
    def __init__(self):
        self.config = {
            'host': 'db',          # Al estar en Docker pero mapear puertos, usas localhost
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
                    #print("¡Conexión exitosa a la base de datos!")
                    return conexion
            except Error as e:
                print(f"Base de datos no lista (quedan {intentos} intentos)...")
                time.sleep(5)
                intentos -= 1
        
        print("No se pudo conectar a la base de datos tras varios intentos.")
        return None

    def guardar_personaje(self, personaje):
        conexion = self.conectar()
        if conexion:
            cursor = conexion.cursor()
            
            query = """
            INSERT INTO personaje 
            (nombre, clase, nivel, experiencia, vida_max, defensa, ataque, agilidad, defensa_magica, ataque_magico, magia_max)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                personaje.nombre, 
                personaje.clase, 
                personaje.nivel,
                personaje.experiencia_actual,
                personaje.vida,
                personaje.defensa,
                personaje.ataque,
                personaje.agilidad,
                personaje.defensa_magica,
                personaje.ataque_magico,
                personaje.magia,
            )
            
            cursor.execute(query, valores)
            conexion.commit() #Sin esto no se guardan los cambios
            cursor.close()
            conexion.close()
            print(f"¡{personaje.nombre} guardado en la DB!")

    def mostrar_personajes_creados(self):
        conexion = self.conectar()
        if not conexion:
            print("Error al acceder a la base de datos.")
            return
        
        try:
            cursor = conexion.cursor()
            query = "SELECT nombre, clase, nivel FROM personaje"
            cursor.execute(query)
            personajes = cursor.fetchall()
            if personajes:
                for personaje in personajes:
                    print(f"Nombre {personaje[0]} -- Clase {personaje[1]} -- nivel {personaje[2]}\n")
            else:
                print("No hay personajes en la BD.")
        except Error as e:
            print(f"Error al leer personajes:{e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

    def cargar_personaje(self, nombre):
        conexion=self.conectar()
        cursor = conexion.cursor()

        query = "SELECT nombre, clase, nivel FROM personaje WHERE nombre= %s"
        cursor.execute(query, (nombre, ))
        resultado = cursor.fetchone()

        print(resultado) #Aca solo era para probar. Despues tendra otra codificacion.