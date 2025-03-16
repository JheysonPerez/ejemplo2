FROM python:3.9-slim

WORKDIR /app

# Copiamos el archivo app.py desde la carpeta flask (donde está el Dockerfile)
COPY app.py /app/

# Instalamos las dependencias necesarias, incluyendo cryptography
RUN pip install flask pymysql cryptography

EXPOSE 5000

CMD ["python", "app.py"]
