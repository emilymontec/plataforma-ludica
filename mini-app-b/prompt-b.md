## Rol
Actúa como desarrollador backend con experiencia en FastAPI, Jinja2 y pruebas con pytest.

## Objetivo
Construir la mini-aplicación web Lista de tareas con estos requisitos:
1. GET / muestra la lista de tareas, un formulario para agregar una tarea y, en cada tarea, botones para completarla y para eliminarla.
2. POST /api/tareas recibe {"titulo": "Estudiar FastAPI"} y responde con el código 201 y la tarea creada: {"id": 1, "titulo": "Estudiar FastAPI", "completada": false}. El título debe tener entre 1 y 100 caracteres; si no, responde con el código 422.
3. GET /api/tareas devuelve la lista de tareas.
4. PUT /api/tareas/{id}/completar marca la tarea como completada y la devuelve.
5. DELETE /api/tareas/{id} elimina la tarea y responde con el código 204.
6. Si la tarea no existe, completar y eliminar responden con el código 404.

## Contexto
Lee AGENTS.md. El contrato de la API está en tests/test_aceptacion.py: las rutas, los nombres de los campos y los códigos de estado deben coincidir con esas pruebas.

## Restricciones
Usa solo las dependencias de requirements.txt.
Define las rutas en app/main.py y la lógica en app/servicios.py, sin importar FastAPI en servicios.
Guarda los datos en memoria, sin base de datos ni archivos.
No modifiques tests/test_aceptacion.py.
La página usa HTML, CSS y JavaScript sin librerías externas.

## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos que vas a crear y espera mi aprobación. Al terminar, resume en una línea qué hace cada archivo.

## Ejemplo
POST /api/tareas con {"titulo": "Leer el encargo"} responde con el código 201 y devuelve:
{"id": 1, "titulo": "Leer el encargo", "completada": false}

PUT /api/tareas/1/completar devuelve:
{"id": 1, "titulo": "Leer el encargo", "completada": true}

## Criterio de éxito
python -m pytest -v pasa todas las pruebas y ruff check no reporta errores. Si después de 3 intentos las pruebas no pasan, detente y explica el problema.