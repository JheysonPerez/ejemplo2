import pytest
import requests

def test_home_endpoint():
    response = requests.get("http://localhost:5000")
    assert response.status_code == 200
    assert "Estoy agarrando señal desde MySQL :!" in response.text  # Ajustado a lo que Flask devuelve