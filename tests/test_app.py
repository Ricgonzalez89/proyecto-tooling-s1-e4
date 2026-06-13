import os
import sys

# Asegurar que el paquete raíz del proyecto esté en sys.path para importar `app`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import app as app_module
from app import app


import pytest


@pytest.fixture
def client():
    app.testing = True
    # resetear estado compartido antes de cada test
    app_module.tareas.clear()
    app_module.contador_id = 1
    with app.test_client() as client:
        yield client


def test_post_tarea(client):
    resp = client.post("/tareas", json={"titulo": "Prueba"})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["id"] == 1
    assert data["titulo"] == "Prueba"


def test_get_tareas(client):
    client.post("/tareas", json={"titulo": "Otra"})
    resp = client.get("/tareas")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert any(t["titulo"] == "Otra" for t in data)
