# Registro: endpoint de versión de API

1. **Objetivo:** Agregar `GET /api/version` para devolver la versión definida en
`app/proyecto.py` y cubrirlo con una prueba.
2. **Herramienta y modelo:** Copilot SDK en VS Code; modelo no especificado.

3. **Prompt:** «Lee AGENTS.md. Agrega el endpoint GET /api/version, que devuelva
la versión definida en app/proyecto.py, con su prueba en tests/test_inicio.py.
Antes de escribir código, explícame qué archivos vas a modificar y espera mi aprobación.»

4. **Resultado:** Se agregó el endpoint y una prueba que verifica el estado HTTP y
que el valor coincide con `proyecto.VERSION`; la prueba pasa. No hubo que corregir
la implementación del endpoint. La suite también detectó una discrepancia previa en
la prueba de `/salud` (espera `"ok"`, pero la ruta responde `"en funcionamiento"`);ar
se dejó intacta por ser ajena al cambio.
