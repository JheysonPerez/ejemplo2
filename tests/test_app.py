import requests

def test_home_endpoint():
    # Tu API debería devolver el mensaje que viene desde MySQL
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200
    assert "EStoy agarrando señal desde MySql :P!" in response.text
