"""Lógica de la lista de tareas con almacenamiento en memoria."""

_tareas: list[dict] = []
_siguiente_id = 1


def listar_tareas() -> list[dict]:
    """Devuelve una copia de todas las tareas."""
    return [dict(tarea) for tarea in _tareas]


def crear_tarea(titulo: str) -> dict:
    """Crea una tarea nueva y la devuelve."""
    global _siguiente_id

    tarea = {"id": _siguiente_id, "titulo": titulo, "completada": False}
    _siguiente_id += 1
    _tareas.append(tarea)
    return dict(tarea)


def completar_tarea(tarea_id: int) -> dict | None:
    """Marca una tarea como completada; devuelve None si no existe."""
    for tarea in _tareas:
        if tarea["id"] == tarea_id:
            tarea["completada"] = True
            return dict(tarea)
    return None


def eliminar_tarea(tarea_id: int) -> bool:
    """Elimina una tarea; devuelve False si no existe."""
    for indice, tarea in enumerate(_tareas):
        if tarea["id"] == tarea_id:
            del _tareas[indice]
            return True
    return False
