"""Punto de entrada de la aplicación FastAPI."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app import proyecto
from app.rutas import api, paginas

CARPETA_APP = Path(__file__).resolve().parent

app = FastAPI(
    title="Plataforma lúdica de cursos para niños",
    description=f"Proyecto de {proyecto.APRENDIZ}: {proyecto.CURSO} con {proyecto.MECANICA}.",
    version=proyecto.VERSION,
)

app.mount("/static", StaticFiles(directory=CARPETA_APP / "static"), name="static")
app.include_router(paginas.router)
app.include_router(api.router)
