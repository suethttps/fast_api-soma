from fastapi.testclient import TestClient
from app import app, sum_values


def test_sum_values():
    assert sum_values(1, 2) == 3
    assert sum_values(2, 2) == 4
    assert sum_values(3, 2) == 5


def test_root_endpoint():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API de soma funcionando"}


def test_sum_endpoint():
    client = TestClient(app)
    response = client.get("/sum/10/5")
    assert response.status_code == 200
    assert response.json() == {"result": 15}