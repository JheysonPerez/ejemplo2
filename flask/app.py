from flask import Flask, request, jsonify
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

def get_db_connection():
    """Establece y devuelve una conexión a la base de datos."""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as e:
        logger.error(f"Error al conectar a MySQL: {str(e)}")
        raise

def init_db():
    """Inicializa la tabla users si no existe."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                value VARCHAR(255)
            )
        """)
        conn.commit()
        logger.info("Tabla users inicializada o ya existe")
    except mysql.connector.Error as e:
        logger.error(f"Error al inicializar la base de datos: {str(e)}")
    finally:
        conn.close()

# Inicializar la base de datos al arrancar
init_db()

@app.route('/')
def home():
    """Endpoint principal que verifica la conexión a MySQL."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        conn.close()
        return "Estoy agarrando señal desde MySQL :!"
    except mysql.connector.Error:
        return "Error al conectar a MySQL: Servicio no disponible", 500

# CRUD Endpoints
@app.route('/create', methods=['POST'])
def create_user():
    """Crea un nuevo usuario."""
    data = request.get_json()
    name = data.get('name')
    value = data.get('value')
    if not name:
        return jsonify({"error": "El campo 'name' es requerido"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, value) VALUES (%s, %s)", (name, value))
        conn.commit()
        logger.info(f"Usuario creado: {name}")
        return jsonify({"message": "record created", "id": cursor.lastrowid}), 201
    except mysql.connector.Error as e:
        logger.error(f"Error al crear usuario: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/read', methods=['GET'])
def read_users():
    """Lee todos los usuarios."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        users = [{"id": row[0], "name": row[1], "value": row[2]} for row in rows]
        logger.info(f"Usuarios leídos: {len(users)}")
        return jsonify(users), 200
    except mysql.connector.Error as e:
        logger.error(f"Error al leer usuarios: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    """Actualiza un usuario existente."""
    data = request.get_json()
    name = data.get('name')
    value = data.get('value')
    if not name:
        return jsonify({"error": "El campo 'name' es requerido"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name = %s, value = %s WHERE id = %s", (name, value, id))
        if cursor.rowcount == 0:
            return jsonify({"error": "Usuario no encontrado"}), 404
        conn.commit()
        logger.info(f"Usuario actualizado: ID {id}")
        return jsonify({"message": "updated"}), 200
    except mysql.connector.Error as e:
        logger.error(f"Error al actualizar usuario: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    """Elimina un usuario."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (id,))
        if cursor.rowcount == 0:
            return jsonify({"error": "Usuario no encontrado"}), 404
        conn.commit()
        logger.info(f"Usuario eliminado: ID {id}")
        return jsonify({"message": "deleted"}), 200
    except mysql.connector.Error as e:
        logger.error(f"Error al eliminar usuario: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

if __name__ == "__main__":
    logger.info("Iniciando Flask en 0.0.0.0:5000...")
    app.run(host="0.0.0.0", port=5000)