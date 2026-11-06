# Plataforma lúdica de cursos para niños

Prototipo de una plataforma web lúdica de cursos para niños, desarrollado con FastAPI.

- **Aprendiz:** Nombre Apellido
- **Curso y mecánica:** (complete)
- **Aplicación publicada:** (complete con la URL de Render)

## Ejecutar en su equipo

En Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

En Linux o macOS, cree el entorno con `python3 -m venv .venv` y actívelo con `source .venv/bin/activate`.

Abra http://127.0.0.1:8000 en el navegador. La documentación de la API está en http://127.0.0.1:8000/docs.

## Verificar

```bash
pytest -v
ruff check .
```

## Estructura

| Carpeta o archivo | Contenido |
| --- | --- |
| `app/` | Aplicación FastAPI: rutas, servicios, modelos, plantillas y archivos estáticos |
| `app/proyecto.py` | Datos de identificación del proyecto |
| `tests/` | Pruebas automatizadas |
| `specs/` | Especificación, flujo de usuario, plan técnico, tareas y decisiones |
| `prompts/` | Prompts versionados |
| `entregas/` | Respuestas semanales; `entregar.py` genera el PDF |
| `AGENTS.md` | Contexto del proyecto para los agentes de IA |
| `STATE.md` | Estado, decisiones y siguiente paso |
| `render.yaml` | Configuración del despliegue en Render |

## Licencia

MIT. Consulte el archivo LICENSE.
