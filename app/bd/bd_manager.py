import mysql.connector
from mysql.connector import Error
import time

class DBManager:
    def __init__(self):
        self.config = {
            'host': 'db',          # Al estar en Docker pero mapear puertos, usas localhost
            'user': 'usuario_rpg',        # Lo definiste en tu docker-compose
            'password': 'proyecto_rpg',   # Lo definiste en tu docker-compose
            'database': 'rpg_db'          # Lo definiste en tu docker-compose
        }

    def conectar(self):
        # Intentaremos conectar 10 veces, esperando 5 segundos entre cada una
        intentos = 10
        while intentos > 0:
            try:
                conexion = mysql.connector.connect(**self.config)
                if conexion.is_connected():
                    print("¡Conexión exitosa a la base de datos!")
                    return conexion
            except Error as e:
                print(f"Base de datos no lista (quedan {intentos} intentos)...")
                time.sleep(5) # Espera 5 segundos antes de volver a intentar
                intentos -= 1
        
        print("No se pudo conectar a la base de datos tras varios intentos.")
        return None

    def guardar_personaje(self, personaje):
        conexion = self.conectar()
        if conexion:
            cursor = conexion.cursor()
            # Esta es la parte de "SQL puro" que querías ver
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
            conexion.commit() # ¡Importante! Sin esto no se guardan los cambios
            cursor.close()
            conexion.close()
            print(f"¡{personaje.nombre} guardado en la DB!")


    def cargar_personaje(self, nombre):
        conexion=self.conectar()
        cursor = conexion.cursor()

        query = "SELECT nombre, clase, nivel FROM personaje WHERE nombre= %s"
        cursor.execute(query, (nombre, ))

        resultado = cursor.fetchone()

        print(resultado)