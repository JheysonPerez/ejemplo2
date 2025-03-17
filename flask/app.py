from flask import Flask
import mysql.connector

app = Flask(__name__)

db_config = {
    "host": "mysql",
    "user": "user",
    "password": "userpassword",
    "database": "testdb"
}

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT 1")  # Consulta simple para verificar conexión
    conn.close()
    message = "Estoy agarrando señal desde MySQL :!"
except mysql.connector.Error as e:
    message = "Error al conectar a MySQL"

@app.route('/')
def home():
    return message