"""Aplicación web de la lista de tareas."""

from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from app import servicios

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Lista de tareas")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

EstadoFiltro = Literal["pendientes", "completadas"]


class TareaEntrada(BaseModel):
    """Datos para crear una tarea."""

    titulo: str = Field(min_length=1, max_length=100)


@app.get("/", response_class=HTMLResponse)
def pagina_principal(request: Request, estado: EstadoFiltro | None = None):
    """Muestra la lista de tareas y el formulario de alta."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "tareas": servicios.listar_tareas(estado),
            "estado": estado,
        },
    )


@app.post("/api/tareas", status_code=status.HTTP_201_CREATED)
def crear_tarea(datos: TareaEntrada) -> dict:
    """Crea una tarea y responde con ella."""
    return servicios.crear_tarea(datos.titulo)


@app.get("/api/tareas")
def listar_tareas(estado: EstadoFiltro | None = None) -> list[dict]:
    """Devuelve todas las tareas o las filtradas por estado."""
    return servicios.listar_tareas(estado)


@app.put("/api/tareas/{tarea_id}/completar")
def completar_tarea(tarea_id: int) -> dict:
    """Marca una tarea como completada."""
    tarea = servicios.completar_tarea(tarea_id)
    if tarea is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarea no encontrada",
        )
    return tarea


@app.delete("/api/tareas/{tarea_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_tarea(tarea_id: int) -> None:
    """Elimina una tarea."""
    if not servicios.eliminar_tarea(tarea_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarea no encontrada",
        )
