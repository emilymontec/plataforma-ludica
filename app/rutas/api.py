"""Endpoints de la API REST, documentados en /docs."""

from fastapi import APIRouter
from pydantic import BaseModel

from app import proyecto

router = APIRouter()


class Salud(BaseModel):
    estado: str


class DatosProyecto(BaseModel):
    aprendiz: str
    curso: str
    mecanica: str
    version: str


@router.get("/salud", response_model=Salud, tags=["Sistema"])
def salud():
    """Indica si la aplicación está en funcionamiento."""
    return Salud(estado="en funcionamiento")


@router.get("/api/proyecto", response_model=DatosProyecto, tags=["Proyecto"])
def datos_proyecto():
    """Devuelve los datos de identificación del proyecto."""
    return DatosProyecto(
        aprendiz=proyecto.APRENDIZ,
        curso=proyecto.CURSO,
        mecanica=proyecto.MECANICA,
        version=proyecto.VERSION,
    )
