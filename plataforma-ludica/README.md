# Plataforma lúdica de cursos para niños

Prototipo de una plataforma web lúdica de cursos para niños, desarrollado con FastAPI.

- **Aprendiz:** Emily Monterrosa
- **Curso y mecánica:** Geografía de Colombia (mecánica: misiones e insignias)
- **Aplicación publicada:**

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
| `app/` | Aplicación FastAPI |
| `app/main.py` | Crea la aplicación, publica los archivos estáticos y registra las rutas |
| `app/proyecto.py` | Datos de identificación del proyecto |
| `app/rutas/` | Rutas HTML y API: página de inicio, estado del servicio y datos del proyecto |
| `app/servicios/` | Paquete reservado para la lógica de negocio; todavía no contiene servicios |
| `app/modelos/` | Paquete reservado para los modelos SQLModel; todavía no contiene modelos |
| `app/templates/` | Plantillas Jinja2 para la página de inicio y la estructura HTML común |
| `app/static/` | Estilos, JavaScript, manifiesto, service worker e iconos de la PWA |
| `tests/` | Pruebas automatizadas; `aceptacion/` está reservado para pruebas de aceptación |
| `specs/` | Especificación, plan técnico, tareas y flujo de usuario |
| `specs/adr/` | Plantilla para registrar decisiones de arquitectura |
| `prompts/` | Instrucciones para guardar prompts; actualmente solo contiene su README |
| `entregas/` | Plantilla para las respuestas semanales; `entregar.py` genera el PDF de una semana |
| `.github/workflows/ci.yml` | Ejecuta Ruff, las pruebas y una comprobación de inicio en GitHub Actions |
| `AGENTS.md` | Contexto y convenciones del proyecto para los agentes de IA |
| `STATE.md` | Estado actual, decisiones y siguiente paso |
| `POLITICA_IA.md` | Política para el uso de herramientas de IA |
| `pyproject.toml` | Configuración de pytest y Ruff |
| `requirements.txt` / `requirements-dev.txt` | Dependencias de ejecución y desarrollo |
| `render.yaml` | Configuración del despliegue en Render |
| `.env.example` | Ejemplo de variables de entorno; no contiene valores secretos |

## Licencia

MIT. Consulte el archivo [LICENSE](/LICENSE)
