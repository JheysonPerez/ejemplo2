from flask import Flask
import mysql.connector
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

db_config = {
    "host": "mysql",
    "user": "user",
    "password": "userpassword",
    "database": "testdb"
}

try:
    logger.info("Intentando conectar a MySQL...")
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    conn.close()
    message = "Estoy agarrando señal desde MySQL :!"
    logger.info("Conexión a MySQL exitosa")
except mysql.connector.Error as e:
    message = f"Error al conectar a MySQL: {str(e)}"
    logger.error(message)

@app.route('/')
def home():
    return message

if __name__ == "__main__":
    logger.info("Iniciando Flask en 0.0.0.0:5000...")
    app.run(host="0.0.0.0", port=5000)