from flask import Flask
import pyodbc

app = Flask(__name__)

def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=sqlserver;'
        'DATABASE=master;'
        'UID=sa;'
        'PWD=YourStrong!Passw0rd'
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT @@VERSION')
    row = cursor.fetchone()
    conn.close()
    return f'SQL Server version: {row[0]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
