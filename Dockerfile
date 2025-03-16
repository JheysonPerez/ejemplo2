# Imagen base de Python
FROM python:3.11-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos necesarios
COPY . .

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto que usa Flask
EXPOSE 5000

# Comando para iniciar la app con Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
