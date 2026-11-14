const formulario = document.querySelector("#form-tarea");
const titulo = document.querySelector("#titulo");
const error = document.querySelector("#error");

function mostrarError(mensaje) {
  error.textContent = mensaje;
  error.hidden = false;
}

function ocultarError() {
  error.textContent = "";
  error.hidden = true;
}

async function pedir(url, opciones) {
  const respuesta = await fetch(url, opciones);
  if (!respuesta.ok) {
    throw new Error(`Error ${respuesta.status}`);
  }
  return respuesta;
}

formulario.addEventListener("submit", async (evento) => {
  evento.preventDefault();
  ocultarError();

  const valor = titulo.value.trim();
  if (valor.length < 1 || valor.length > 100) {
    mostrarError("El título debe tener entre 1 y 100 caracteres.");
    return;
  }

  try {
    await pedir("/api/tareas", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ titulo: valor }),
    });
    window.location.reload();
  } catch {
    mostrarError("No se pudo crear la tarea. Inténtalo de nuevo.");
  }
});

document.querySelectorAll(".completar").forEach((boton) => {
  boton.addEventListener("click", async () => {
    try {
      await pedir(`/api/tareas/${boton.dataset.id}/completar`, {
        method: "PUT",
      });
      window.location.reload();
    } catch {
      mostrarError("No se pudo completar la tarea.");
    }
  });
});

document.querySelectorAll(".eliminar").forEach((boton) => {
  boton.addEventListener("click", async () => {
    try {
      await pedir(`/api/tareas/${boton.dataset.id}`, { method: "DELETE" });
      window.location.reload();
    } catch {
      mostrarError("No se pudo eliminar la tarea.");
    }
  });
});
