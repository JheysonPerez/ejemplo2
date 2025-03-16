# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de tu aplicación Flask al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto de la aplicación Flask
EXPOSE 5000

# Comando para iniciar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]
