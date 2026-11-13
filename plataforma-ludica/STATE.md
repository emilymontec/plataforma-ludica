# STATE.md

Estado del proyecto. Léalo al iniciar cada sesión de trabajo y actualícelo al cerrarla.

## Estado actual

Actualizado: 2026-11-10.

- Prototipo FastAPI funcional como base: la página `/` muestra los datos del curso y la versión; `/salud`, `/api/proyecto` y `GET /api/version` exponen endpoints; FastAPI ofrece `/docs`.
- La interfaz usa plantillas Jinja2 y archivos estáticos. Incluye manifiesto, instalación como PWA y service worker con caché para uso sin conexión.
- El proyecto está configurado para Render y tiene una URL pública definida en `app/proyecto.py`; no se verificó el estado del despliegue durante esta actualización.
- Hay siete pruebas automatizadas en `tests/test_inicio.py` para la página, endpoints, documentación y recursos PWA. La nueva prueba verifica que `GET /api/version` responda `200` y devuelva el valor de `proyecto.VERSION`. No ejecuté la suite al preparar esta actualización documental.
- La especificación, el plan técnico, las tareas y el flujo de usuario siguen siendo plantillas sin historias ni tareas concretas.
- La autenticación y los flujos de docente/niño, cursos, misiones e insignias aún no están implementados. Los paquetes de modelos y servicios están reservados para trabajo futuro; no hay persistencia funcional.

## Decisiones

| Fecha | Decisión | Motivo |
| --- | --- | --- |
| 2026-11-10 | `GET /api/version` devuelve `{"version": proyecto.VERSION}` con un modelo de respuesta Pydantic. | Mantiene la versión vinculada a la fuente definida en `app/proyecto.py`; la prueba comprueba el contrato. |
| 2026-11-10 | `/salud` devuelve `{"estado": "ok"}`. | La respuesta implementada coincide con el valor verificado por la prueba del endpoint. |
| — | No hay decisiones de arquitectura registradas en ADR. | `specs/adr/` contiene únicamente la plantilla. |

## Siguiente paso

El endpoint de versión ya está implementado. El siguiente paso sigue siendo completar `specs/spec.md` con las historias, criterios de aceptación y alcance del MVP; después desglosarlos en `specs/tasks.md` antes de implementar el primer flujo de usuario.
