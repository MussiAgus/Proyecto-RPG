CREATE TABLE IF NOT EXISTS personaje (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) UNIQUE NOT NULL,
    clase VARCHAR(20) NOT NULL,
    nivel INT DEFAULT 1,
    experiencia INT DEFAULT 0,
    vida_max INT NOT NULL,
    defensa INT NOT NULL,
    ataque INT NOT NULL,
    agilidad INT NOT NULL,
    defensa_magica INT NOT NULL,
    ataque_magico INT NOT NULL,
    magia_max INT NOT NULL,
    stamina_max INT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);