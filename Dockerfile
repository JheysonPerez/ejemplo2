# Imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia e instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de archivos al contenedor
COPY . .

# Exponer el puerto de la app
EXPOSE 5000

# Comando para ejecutar tu aplicación con Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
