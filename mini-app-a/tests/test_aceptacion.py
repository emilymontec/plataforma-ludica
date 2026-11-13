from fastapi.testclient import TestClient

from app.main import app

cliente = TestClient(app)

def crear(titulo="Estudiar FastAPI"):
    return cliente.post("/api/tareas", json={"titulo": titulo})

def ids_actuales():
    return [tarea["id"] for tarea in cliente.get("/api/tareas").json()]

def test_pagina_principal():
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    assert "text/html" in respuesta.headers["content-type"]
    
def test_crear_tarea():
    respuesta = crear()
    assert respuesta.status_code == 201
    tarea = respuesta.json()
    assert isinstance(tarea["id"], int)
    assert tarea["titulo"] == "Estudiar FastAPI"
    assert tarea["completada"] is False

def test_listar_incluye_la_tarea_creada():
    tarea = crear("Leer el encargo").json()
    assert tarea["id"] in ids_actuales()

def test_completar_tarea():
    tarea = crear().json()
    respuesta = cliente.put(f"/api/tareas/{tarea['id']}/completar")
    assert respuesta.status_code == 200
    assert respuesta.json()["completada"] is True

def test_eliminar_tarea():
    tarea = crear().json()
    assert cliente.delete(f"/api/tareas/{tarea['id']}").status_code == 204
    assert tarea["id"] not in ids_actuales()

def test_titulo_vacio():
    assert crear("").status_code == 422

def test_tarea_inexistente():
    assert cliente.put("/api/tareas/9999/completar").status_code == 404
    assert cliente.delete("/api/tareas/9999").status_code == 404