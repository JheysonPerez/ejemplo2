import os
from flask import Flask
import pymysql
import time

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        connection = pymysql.connect(
            host=os.getenv('DB_HOST', 'mysql'),
            user=os.getenv('DB_USER', 'user'),
            password=os.getenv('DB_PASSWORD', 'userpassword'),
            database=os.getenv('DB_NAME', 'testdb')
        )
        cursor = connection.cursor()
        cursor.execute("SELECT 'Estoy agarrando señal desde MySQL :P!'")
        result = cursor.fetchone()
        return result[0]
    except Exception as e:
        return f"Error de conexión a MySQL: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
