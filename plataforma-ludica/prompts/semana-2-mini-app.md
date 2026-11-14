# Prompts

## Mini App A
Haz una app web de lista de tareas con FastAPI.

## Mini App B

```
## Rol
Actúa como desarrollador backend con experiencia en FastAPI, Jinja2 y pruebas con pytest.

## Objetivo
Construir la mini-aplicación web Lista de tareas con estos requisitos:
1. GET / muestra la lista de tareas, un formulario para agregar una tarea y, en cada tarea,
botones para completarla y para eliminarla.
2. POST /api/tareas recibe {"titulo": "Estudiar FastAPI"} y responde con el código 201 y la
tarea creada: {"id": 1, "titulo": "Estudiar FastAPI", "completada": false}. El título debe
tener entre 1 y 100 caracteres; si no, responde con el código 422.
3. GET /api/tareas devuelve la lista de tareas.
4. PUT /api/tareas/{id}/completar marca la tarea como completada y la devuelve.
5. DELETE /api/tareas/{id} elimina la tarea y responde con el código 204.
6. Si la tarea no existe, completar y eliminar responden con el código 404.

## Contexto
Lee AGENTS.md. El contrato de la API está en tests/test_aceptacion.py: las rutas, los nombres
de los campos y los códigos de estado deben coincidir con esas pruebas.

## Restricciones
Usa solo las dependencias de requirements.txt.
Define las rutas en app/main.py y la lógica en app/servicios.py, sin importar FastAPI en
servicios.
Guarda los datos en memoria, sin base de datos ni archivos.
No modifiques tests/test_aceptacion.py.
La página usa HTML, CSS y JavaScript sin librerías externas.

## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos que vas a crear
y espera mi aprobación. Al terminar, resume en una línea qué hace cada archivo.

## Ejemplo
POST /api/tareas con {"titulo": "Leer el encargo"} responde con el código 201 y devuelve:
{"id": 1, "titulo": "Leer el encargo", "completada": false}

PUT /api/tareas/1/completar devuelve:
{"id": 1, "titulo": "Leer el encargo", "completada": true}

## Criterio de éxito
python -m pytest -v pasa todas las pruebas y ruff check no reporta errores. Si después de 3 intentos
las pruebas no pasan, detente y explica el problema.

```

### Prompt de mejoras:

```
## Rol
Actúa como desarrollador backend y frontend con experiencia en FastAPI, Jinja2, HTML y CSS minimalista.

## Objetivo
Agregar la funcionalidad de filtrado por estado y rediseñar la interfaz visual para que sea moderna
y minimalista:
1. `GET /api/tareas` debe aceptar el parámetro opcional `estado` (con los valores `pendientes` o
`completadas`), devolviendo únicamente las tareas que correspondan a ese estado.
2. Si el parámetro `estado` tiene un valor distinto de `pendientes` o `completadas`, debe responder
con el código de estado `422`.
3. La página principal en `app/templates/index.html` debe incluir botones para filtrar las tareas por:
**Todas**, **Pendientes** y **Completadas**.
4. Rediseñar la página principal para que tenga una interfaz minimalista, limpia, con tipografía clara,
tonos neutros y buen espacio en blanco.
5. Crear una prueba nueva en `tests/test_mejora.py` para verificar que el filtrado por estado funcione
correctamente y devuelva el contenido esperado.

## Contexto
Lee AGENTS.md y tests/test_aceptacion.py. La lógica de filtrado debe ir en app/servicios.py y las rutas
en app/main.py.

## Restricciones
Usa solo las dependencias de requirements.txt.
No modifiques tests/test_aceptacion.py.
Define las rutas en app/main.py y la lógica en app/servicios.py, sin importar FastAPI en servicios.
No uses librerías ni frameworks externos de CSS/JS en el HTML; aplica CSS puro y minimalista dentro del
archivo.

## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos que vas a modificar o
crear (`app/main.py`, `app/servicios.py`, `app/templates/index.html`, `tests/test_mejora.py`) y espera mi
aprobación.

## Ejemplo
Petición: `GET /api/tareas?estado=pendientes`
Respuesta esperada (código 200):
[{"id": 1, "titulo": "Estudiar FastAPI", "completada": false}]

Petición: `GET /api/tareas?estado=invalido`
Respuesta esperada: Código de estado 422.

## Criterio de éxito
python -m pytest -v pasa todas las pruebas (tanto las de aceptación como las de mejora en `tests/test_mejora.py`)
y ruff check no reporta errores. Si después de 3 intentos las pruebas no pasan, detente y explica el problema.

```
