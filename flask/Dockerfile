FROM python:3.9-slim

# Definimos el directorio de trabajo
WORKDIR /app

# Instalamos dependencias de sistema para poder usar curl y pymysql correctamente
RUN apt-get update && \
    apt-get install -y curl gcc default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

# Copiamos los archivos necesarios
COPY requirements.txt /app/
COPY app.py /app/

# Instalamos las dependencias de Python desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto 5000
EXPOSE 5000

# Comando por defecto para ejecutar la app
CMD ["python", "app.py"]
