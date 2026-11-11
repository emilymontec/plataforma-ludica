# Copilot instructions for `plataforma-ludica`

## Project context

This repository is a FastAPI-based educational web app for children. It serves a PWA-style landing page and exposes a simple REST API. The app is intentionally lightweight: the FastAPI app is created in `app/main.py`, and project metadata is centralized in `app/proyecto.py` so the homepage, API, and delivery script all stay aligned.

## Local build, test, and lint commands

Use the project environment before running the app or tests:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements-dev.txt
```

Run the app locally:

```bash
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000` and the API docs at `http://127.0.0.1:8000/docs`.

Validate the project:

```bash
pytest -v
ruff check .
```

Run a single test directly:

```bash
pytest tests/test_inicio.py::test_salud_responde_ok -q
```

Or a single file:

```bash
pytest tests/test_inicio.py -q
```

The CI workflow in `.github/workflows/ci.yml` does the same checks (`ruff check .`, `pytest -v`, and a startup probe against `/salud`).

## High-level architecture

- `app/main.py` creates the FastAPI app, mounts static assets at `/static`, and registers the routers.
- `app/rutas/paginas.py` serves HTML pages through Jinja2 templates in `app/templates/`.
- `app/rutas/api.py` exposes the REST endpoints and uses Pydantic models for request/response payloads.
- `app/proyecto.py` holds the app identity (`APRENDIZ`, `CURSO`, `MECANICA`, `VERSION`, `URL_PUBLICA`) so the homepage and API use a single source of truth.
- `app/static/` contains the PWA assets (`manifest.json`, `sw.js`, CSS, JS, and icons).
- `tests/` contains automated verification, including route and static asset checks.
- `specs/` stores the product/technical specification, plan, user flow, and ADR notes.
- `app/modelos/` and `app/servicios/` are reserved for future data-access and business-logic layers; keep route modules thin while those modules are under construction.

## Repository conventions

- Keep route handlers thin. Business logic should live in `app/servicios/` or dedicated modules rather than being embedded directly in the router functions.
- Keep the app metadata centralized in `app/proyecto.py`; avoid duplicating values across HTML, API responses, and scripts.
- Preserve the existing FastAPI + Jinja + PWA structure instead of introducing a separate frontend build system unless the project explicitly requires it.
- Prefer small, focused changes. The project is a learning/demo app and the existing tests are a lightweight regression suite.
- Use Spanish names and user-facing copy where they are part of the product or documentation, matching the repository's current terminology.
- Do not add secrets or real personal data to source files; use environment variables or `.env.example` patterns instead.
- When adding tests, follow the current style in `tests/test_inicio.py`: instantiate `TestClient(app)` and assert both the HTTP status and the expected payload or rendered content.

## Related project context

This repo also includes guidance in `AGENTS.md`, which states the project should use:

- Python 3.11+
- FastAPI + Jinja2
- SQLite for development and PostgreSQL for deployment
- pytest + TestClient + Ruff
- GitHub Actions + Render

Keep changes aligned with that structure.
