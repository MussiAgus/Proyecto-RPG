# 1. Usamos una imagen oficial de Python liviana
FROM python:3.11-slim

# 2. Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos el archivo de requisitos para instalar librerías
COPY requirements.txt .

# 4. Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos todo el código de nuestro proyecto al contenedor
COPY . .

# 6. Comando para ejecutar tu aplicación (ajusta el path si es necesario)
CMD ["python", "pruebasDB.py"]