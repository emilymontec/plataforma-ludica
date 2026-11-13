import sqlite3
from contextlib import closing
from datetime import UTC, datetime
from pathlib import Path

RUTA_BASE_DATOS = Path(__file__).with_name("tareas.db")


def abrir_conexion() -> sqlite3.Connection:
    conexion = sqlite3.connect(RUTA_BASE_DATOS)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def inicializar_base_datos() -> None:
    with closing(abrir_conexion()) as conexion:
        conexion.execute(
            """
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT NOT NULL DEFAULT '',
                completada INTEGER NOT NULL DEFAULT 0,
                creada_en TEXT NOT NULL
            )
            """
        )
        conexion.commit()


def serializar(fila: sqlite3.Row) -> dict:
    return {
        "id": fila["id"],
        "titulo": fila["titulo"],
        "descripcion": fila["descripcion"],
        "completada": bool(fila["completada"]),
        "creada_en": fila["creada_en"],
    }


def listar_tareas() -> list[dict]:
    with closing(abrir_conexion()) as conexion:
        filas = conexion.execute(
            "SELECT * FROM tareas ORDER BY completada ASC, creada_en DESC, id DESC"
        ).fetchall()

    return [serializar(fila) for fila in filas]


def obtener_tarea(tarea_id: int) -> dict | None:
    with closing(abrir_conexion()) as conexion:
        fila = conexion.execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,)).fetchone()

    return serializar(fila) if fila else None


def crear_tarea(titulo: str, descripcion: str) -> dict:
    creada_en = datetime.now(UTC).isoformat(timespec="seconds")

    with closing(abrir_conexion()) as conexion:
        cursor = conexion.execute(
            """
            INSERT INTO tareas (titulo, descripcion, completada, creada_en)
            VALUES (?, ?, 0, ?)
            """,
            (titulo, descripcion, creada_en),
        )
        conexion.commit()
        fila = conexion.execute(
            "SELECT * FROM tareas WHERE id = ?", (cursor.lastrowid,)
        ).fetchone()

    return serializar(fila)


def actualizar_tarea(tarea_id: int, cambios: dict) -> dict | None:
    columnas = {
        "titulo": "titulo",
        "descripcion": "descripcion",
        "completada": "completada",
    }
    asignaciones = []
    valores = []

    for clave, valor in cambios.items():
        if clave not in columnas:
            continue
        asignaciones.append(f"{columnas[clave]} = ?")
        valores.append(int(valor) if clave == "completada" else valor)

    if not asignaciones:
        return obtener_tarea(tarea_id)

    valores.append(tarea_id)

    with closing(abrir_conexion()) as conexion:
        cursor = conexion.execute(
            f"UPDATE tareas SET {', '.join(asignaciones)} WHERE id = ?",
            tuple(valores),
        )
        conexion.commit()

        if cursor.rowcount == 0:
            return None

        fila = conexion.execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,)).fetchone()

    return serializar(fila)


def completar_tarea(tarea_id: int) -> dict | None:
    return actualizar_tarea(tarea_id, {"completada": True})


def eliminar_tarea(tarea_id: int) -> bool:
    with closing(abrir_conexion()) as conexion:
        cursor = conexion.execute("DELETE FROM tareas WHERE id = ?", (tarea_id,))
        conexion.commit()

    return cursor.rowcount > 0


def eliminar_tareas_completadas() -> int:
    with closing(abrir_conexion()) as conexion:
        cursor = conexion.execute("DELETE FROM tareas WHERE completada = 1")
        conexion.commit()

    return cursor.rowcount
