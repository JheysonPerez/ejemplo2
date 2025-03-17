from flask import Flask
import pymysql

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        connection = pymysql.connect(
            host="mysql",
            user="user",
            password="userpassword",
            database="testdb"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT 'Probando coneccion desde MySql :P!'")
        result = cursor.fetchone()
        return result[0]
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
