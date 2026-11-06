"""Páginas HTML de la aplicación."""

from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from app import proyecto

CARPETA_APP = Path(__file__).resolve().parent.parent
plantillas = Jinja2Templates(directory=CARPETA_APP / "templates")

router = APIRouter(include_in_schema=False)


@router.get("/", response_class=HTMLResponse)
def inicio(request: Request):
    return plantillas.TemplateResponse(
        request,
        "inicio.html",
        {
            "aprendiz": proyecto.APRENDIZ,
            "curso": proyecto.CURSO,
            "mecanica": proyecto.MECANICA,
            "version": proyecto.VERSION,
        },
    )


@router.get("/sw.js")
def service_worker():
    """El service worker se sirve desde la raíz para controlar todo el sitio."""
    return FileResponse(
        CARPETA_APP / "static" / "sw.js",
        media_type="application/javascript",
        headers={"Cache-Control": "no-cache"},
    )
