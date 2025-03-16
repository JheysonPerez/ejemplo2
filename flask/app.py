import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

# Obtener la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv('DATABASE_URL', 'mysql://root:root@mysql:3306/mi_basedatos')

def get_db_connection():
    # Crear la conexión a la base de datos MySQL
    connection = mysql.connector.connect(
        host='mysql',  # El nombre del servicio en Docker Compose
        user='root',
        password='root',
        database='mi_basedatos'
    )
    return connection

@app.route('/')
def home():
    # Verificar si la conexión a la base de datos funciona
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT NOW()')  # Comando simple para probar la conexión
    result = cursor.fetchone()
    conn.close()
    
    # Mostrar el resultado (la hora del servidor MySQL)
    return f"Conexión exitosa, hora del servidor MySQL: {result[0]}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
