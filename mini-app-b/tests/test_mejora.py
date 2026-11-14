from fastapi.testclient import TestClient

from app.main import app

cliente = TestClient(app)


def crear_tarea(titulo: str) -> dict:
    respuesta = cliente.post("/api/tareas", json={"titulo": titulo})
    assert respuesta.status_code == 201
    return respuesta.json()


def test_filtra_tareas_por_estado():
    tarea = crear_tarea("Verificar filtro por estado")

    respuesta = cliente.get("/api/tareas", params={"estado": "pendientes"})
    assert respuesta.status_code == 200
    pendientes = respuesta.json()
    assert tarea in pendientes
    assert all(not t["completada"] for t in pendientes)

    assert cliente.put(f"/api/tareas/{tarea['id']}/completar").status_code == 200

    respuesta = cliente.get("/api/tareas", params={"estado": "pendientes"})
    pendientes = respuesta.json()
    assert tarea["id"] not in [t["id"] for t in pendientes]

    respuesta = cliente.get("/api/tareas", params={"estado": "completadas"})
    assert respuesta.status_code == 200
    completadas = respuesta.json()
    assert any(
        t["id"] == tarea["id"] and t["completada"] is True for t in completadas
    )
    assert all(t["completada"] is True for t in completadas)


def test_estado_invalido_devuelve_422():
    respuesta = cliente.get("/api/tareas", params={"estado": "invalido"})
    assert respuesta.status_code == 422


def test_pagina_muestra_los_filtros():
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    assert "Todas" in respuesta.text
    assert "Pendientes" in respuesta.text
    assert "Completadas" in respuesta.text
