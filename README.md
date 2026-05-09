# Proyecto-RPG
Pequeño proyecto en el que creo un sistema básico de combate por turnos, en el lenguaje Python.
Actualmente el juego cuenta con un sistema de BD en mysql, pero aún falta implementar las funciones para poder usarlo durante el juego.
De todas formas, ya hay una versión base del juego, por lo que se puede hacer un pequeño combate.

## Instrucciones para probarlo (actualmente).
 - Clonar el repositorio.
 - Desde la carperta raiz, en la terminal escribir:
    - Docker compose up --build. Dejar que termine de preparar todo.
    - Precionar control+c para salir. 
    - Docker compose down. (los primeros tres pasos solamente la primera vez).
    - Docker compose up -d
    - docker exec -it rpg_game python main.py
    -
Listo. Con esto, el juego ya estaria corriendo en la consola.

--- 

## Actualmente cuenta con:
 - Diferentes clases de personajes (mago, berserker, strider).
 - Efectos persistentes (quemadura).
 - Habilidades para personajes (bola de fuego).
 - Sistema de subida de niveles, y aumentos de estadisticas.
 - Clase de mensajes aparte, y subclases para cada personaje.
 - Base de datos, para poder guardar y cargar personajes ya creados.
 - Uso de docker. Tanto para la bd, como para la app.

## Cosas en proceso:
 - Mejorar el proceso de las batallas, para poder terminar una, y comenzar otra.
 - Creación de más habilidades específicas por clase.
 - Creación de más efectos, acorde a las diferentes habilidades creadas. 

