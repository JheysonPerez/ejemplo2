# Imagen base de Python slim
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalamos herramientas del sistema necesarias para PyMySQL y curl
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        gcc \
        default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

# Copiamos los archivos de dependencias y código
COPY requirements.txt .
COPY app.py .

# Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto donde correrá Flask
EXPOSE 5000

# Comando por defecto que ejecuta la app
CMD ["python", "app.py"]
