import pytest
import requests
import time
import json

# Pruebas de funcionalidad básica
def test_home_endpoint_success():
    """Verifica que el endpoint principal devuelva la señal de MySQL cuando la conexión es exitosa."""
    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            response = requests.get("http://localhost:5000", timeout=5)
            assert response.status_code == 200
            assert "Estoy agarrando señal desde MySQL :!" in response.text
            break
        except requests.RequestException as e:
            if attempt == max_attempts - 1:
                pytest.fail(f"Failed to connect after {max_attempts} attempts: {e}")
            time.sleep(5)

# Pruebas CRUD
def test_create_user():
    """Prueba la creación de un nuevo usuario."""
    payload = {"name": "Test User", "value": "123"}
    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            response = requests.post("http://localhost:5000/create", json=payload, timeout=5)
            data = response.json()
            assert response.status_code == 201
            assert "record created" in data.get("message", "")
            break
        except requests.RequestException as e:
            if attempt == max_attempts - 1:
                pytest.fail(f"Failed to create user: {e}")
            time.sleep(5)

def test_read_users():
    """Prueba la lectura de usuarios."""
    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            response = requests.get("http://localhost:5000/read", timeout=5)
            data = response.json()
            assert response.status_code == 200
            assert isinstance(data, list)  # Verifica que sea una lista
            break
        except requests.RequestException as e:
            if attempt == max_attempts - 1:
                pytest.fail(f"Failed to read users: {e}")
            time.sleep(5)

def test_update_user():
    """Prueba la actualización de un usuario."""
    # Primero crea un usuario para actualizar
    create_payload = {"name": "Update Test", "value": "initial"}
    create_response = requests.post("http://localhost:5000/create", json=create_payload, timeout=5)
    user_id = create_response.json().get("id")

    update_payload = {"name": "Updated User", "value": "updated"}
    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            response = requests.put(f"http://localhost:5000/update/{user_id}", json=update_payload, timeout=5)
            data = response.json()
            assert response.status_code == 200
            assert "updated" in data.get("message", "")
            break
        except requests.RequestException as e:
            if attempt == max_attempts - 1:
                pytest.fail(f"Failed to update user: {e}")
            time.sleep(5)

def test_delete_user():
    """Prueba la eliminación de un usuario."""
    # Primero crea un usuario para eliminar
    create_payload = {"name": "Delete Test", "value": "123"}
    create_response = requests.post("http://localhost:5000/create", json=create_payload, timeout=5)
    user_id = create_response.json().get("id")

    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            response = requests.delete(f"http://localhost:5000/delete/{user_id}", timeout=5)
            data = response.json()
            assert response.status_code == 200
            assert "deleted" in data.get("message", "")
            break
        except requests.RequestException as e:
            if attempt == max_attempts - 1:
                pytest.fail(f"Failed to delete user: {e}")
            time.sleep(5)

# Pruebas de resiliencia
def test_not_found():
    """Verifica que un endpoint inexistente devuelva 404."""
    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            response = requests.get("http://localhost:5000/nonexistent", timeout=5)
            assert response.status_code == 404
            break
        except requests.RequestException as e:
            if attempt == max_attempts - 1:
                pytest.fail(f"Failed to test 404: {e}")
            time.sleep(5)

def test_multiple_requests():
    """Simula múltiples solicitudes para verificar estabilidad."""
    for _ in range(10):
        response = requests.get("http://localhost:5000", timeout=5)
        assert response.status_code == 200