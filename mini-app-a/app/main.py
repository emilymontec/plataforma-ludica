from pathlib import Path

from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field, field_validator

from app import database

CARPETA_PROYECTO = Path(__file__).resolve().parent.parent

plantillas = Jinja2Templates(directory=str(CARPETA_PROYECTO / "templates"))

app = FastAPI(
    title="Lista de Tareas",
    description="Aplicación web de lista de tareas construida con FastAPI.",
    version="1.0.0",
)

app.mount(
    "/static",
    StaticFiles(directory=str(CARPETA_PROYECTO / "static")),
    name="static",
)

database.inicializar_base_datos()


class TareaCrear(BaseModel):
    titulo: str = Field(max_length=200)
    descripcion: str = Field(default="", max_length=1000)

    @field_validator("titulo")
    @classmethod
    def validar_titulo(cls, valor: str) -> str:
        valor = valor.strip()
        if not valor:
            raise ValueError("El título no puede estar vacío")
        return valor

    @field_validator("descripcion")
    @classmethod
    def validar_descripcion(cls, valor: str) -> str:
        return valor.strip()


class TareaActualizar(BaseModel):
    titulo: str | None = Field(default=None, max_length=200)
    descripcion: str | None = Field(default=None, max_length=1000)
    completada: bool | None = None

    @field_validator("titulo")
    @classmethod
    def validar_titulo(cls, valor: str | None) -> str | None:
        if valor is None:
            return None
        valor = valor.strip()
        if not valor:
            raise ValueError("El título no puede estar vacío")
        return valor

    @field_validator("descripcion")
    @classmethod
    def validar_descripcion(cls, valor: str | None) -> str | None:
        return valor.strip() if valor is not None else None


@app.get("/", response_class=HTMLResponse)
async def pagina_principal(request: Request):
    return plantillas.TemplateResponse(request, "index.html")


@app.get("/api/tareas")
async def listar_tareas():
    return database.listar_tareas()


@app.post("/api/tareas", status_code=status.HTTP_201_CREATED)
async def crear_tarea(payload: TareaCrear):
    return database.crear_tarea(payload.titulo, payload.descripcion)


@app.put("/api/tareas/{tarea_id}/completar")
async def completar_tarea(tarea_id: int):
    tarea = database.completar_tarea(tarea_id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea


@app.patch("/api/tareas/{tarea_id}")
async def actualizar_tarea(tarea_id: int, payload: TareaActualizar):
    cambios = payload.model_dump(exclude_unset=True)
    if not cambios:
        raise HTTPException(status_code=400, detail="No se enviaron cambios")

    tarea = database.actualizar_tarea(tarea_id, cambios)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea


@app.delete("/api/tareas/completadas")
async def limpiar_tareas_completadas():
    return {"eliminadas": database.eliminar_tareas_completadas()}


@app.delete("/api/tareas/{tarea_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_tarea(tarea_id: int):
    if not database.eliminar_tarea(tarea_id):
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
