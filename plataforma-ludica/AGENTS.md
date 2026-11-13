# AGENTS.md

Contexto del proyecto para los agentes de IA. Léalo antes de cualquier cambio.

## Proyecto

Plataforma web lúdica de cursos para niños.
Curso: Geografía de Colombia.
Mecánica: Misiones e Insignias.
Roles: docente y niño. El niño entra con código de clase y avatar, sin correo.

## Stack

- Python 3.11 o superior, FastAPI, plantillas Jinja2
- SQLModel con SQLite en desarrollo y PostgreSQL al publicar
- pytest con TestClient, Ruff
- GitHub Actions para el CI y Render para el despliegue

## Comandos

- Instalar: `pip install -r requirements-dev.txt`
- Ejecutar: `uvicorn app.main:app --reload`
- Pruebas: `pytest -v`
- Estilo: `ruff check .`

## Estructura

- `app/rutas/`: reciben la petición y llaman a los servicios; sin regla de negocio
- `app/servicios/`: regla de negocio, con pruebas propias
- `app/modelos/`: tablas de SQLModel
- `app/templates/` y `app/static/`: interfaz y PWA
- `tests/`: pruebas; `tests/aceptacion/`: criterios de la especificación

## Convenciones

- Nombres en español, claros y completos.
- Cambios pequeños, una tarea por rama y prueba antes del código.
- Al iniciar cada sesión, leer STATE.md.

## Qué no hacer

- No escribir claves ni contraseñas en el código: se leen de variables de entorno.
- No instalar dependencias sin verificar que existen en pypi.org.
- No modificar ni borrar pruebas para que pasen.
- No usar datos personales reales.
- No hacer commit ni push: los hace el desarrollador.

## Lecciones aprendidas

Cada vez que el agente se equivoque, escriba aquí la regla que evita repetir el error.