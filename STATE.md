# STATE.md

Estado del proyecto. Léalo al iniciar cada sesión de trabajo y actualícelo al cerrarla.

## Estado actual

Actualizado: 2026-11-10.

- Prototipo FastAPI funcional como base: la página `/` muestra los datos del curso y la versión; `/salud` y `/api/proyecto` exponen endpoints; FastAPI ofrece `/docs`.
- La interfaz usa plantillas Jinja2 y archivos estáticos. Incluye manifiesto, instalación como PWA y service worker con caché para uso sin conexión.
- El proyecto está configurado para Render y tiene una URL pública definida en `app/proyecto.py`; no se verificó el estado del despliegue durante esta actualización.
- Hay seis pruebas automatizadas en `tests/test_inicio.py` para la página, endpoints, documentación y recursos PWA. No se ejecutaron en esta actualización.
- La especificación, el plan técnico, las tareas y el flujo de usuario siguen siendo plantillas sin historias ni tareas concretas.
- La autenticación y los flujos de docente/niño, cursos, misiones e insignias aún no están implementados. Los paquetes de modelos y servicios están reservados para trabajo futuro; no hay persistencia funcional.

## Decisiones

| Fecha | Decisión | Motivo |
| --- | --- | --- |
| — | No hay decisiones de arquitectura registradas en ADR. | `specs/adr/` contiene únicamente la plantilla. |

## Siguiente paso

Completar `specs/spec.md` con las historias, criterios de aceptación y alcance del MVP; después desglosarlos en `specs/tasks.md` antes de implementar el primer flujo de usuario.
