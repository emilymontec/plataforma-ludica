const state = {
  tasks: [],
  filter: "all",
};

const els = {
  form: document.getElementById("task-form"),
  title: document.getElementById("task-title"),
  description: document.getElementById("task-description"),
  list: document.getElementById("task-list"),
  empty: document.getElementById("empty-state"),
  template: document.getElementById("task-template"),
  progressRing: document.getElementById("progress-ring"),
  progressText: document.getElementById("progress-text"),
  progressFill: document.getElementById("progress-fill"),
  clearCompleted: document.getElementById("clear-completed"),
  toast: document.getElementById("toast"),
  counts: {
    all: document.getElementById("count-all"),
    pending: document.getElementById("count-pending"),
    completed: document.getElementById("count-completed"),
  },
};

let toastTimer;

function showToast(message, type = "info") {
  clearTimeout(toastTimer);
  els.toast.textContent = message;
  els.toast.classList.toggle("is-error", type === "error");
  els.toast.classList.add("is-visible");
  toastTimer = setTimeout(() => els.toast.classList.remove("is-visible"), 2800);
}

async function api(path, options = {}) {
  const response = await fetch(path, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });

  if (response.status === 204) {
    return null;
  }

  const data = await response.json().catch(() => null);

  if (!response.ok) {
    let message = "Ocurrió un error inesperado";
    if (data && Array.isArray(data.detail)) {
      message = data.detail.map((item) => item.msg).join(". ");
    } else if (data && typeof data.detail === "string") {
      message = data.detail;
    }
    throw new Error(message);
  }

  return data;
}

function timeAgo(isoString) {
  const date = new Date(isoString);
  const seconds = Math.max(0, Math.floor((Date.now() - date.getTime()) / 1000));

  if (seconds < 60) return "Hace un momento";
  const minutes = Math.floor(seconds / 60);
  if (minutes < 60) return `Hace ${minutes} min`;

  const hours = Math.floor(minutes / 60);
  if (hours < 24) return `Hace ${hours} h`;

  const days = Math.floor(hours / 24);
  if (days < 7) return `Hace ${days} d`;

  return date.toLocaleDateString("es-ES", { day: "numeric", month: "short", year: "numeric" });
}

function updateStats() {
  const total = state.tasks.length;
  const completed = state.tasks.filter((task) => task.completada).length;
  const pending = total - completed;
  const percent = total === 0 ? 0 : Math.round((completed / total) * 100);

  els.counts.all.textContent = total;
  els.counts.pending.textContent = pending;
  els.counts.completed.textContent = completed;
  els.progressText.textContent = `${percent}%`;
  els.progressRing.style.setProperty("--progress", percent);
  els.progressFill.style.width = `${percent}%`;
  els.clearCompleted.disabled = completed === 0;
}

function visibleTasks() {
  if (state.filter === "pending") return state.tasks.filter((task) => !task.completada);
  if (state.filter === "completed") return state.tasks.filter((task) => task.completada);
  return state.tasks;
}

function render() {
  els.list.innerHTML = "";
  const tasks = visibleTasks();

  els.empty.hidden = tasks.length > 0;
  if (tasks.length === 0) {
    const messages = {
      all: "No hay tareas por aquí. Añade la primera arriba.",
      pending: "¡Bien! No tienes tareas pendientes.",
      completed: "Todavía no has completado ninguna tarea.",
    };
    els.empty.textContent = messages[state.filter];
  }

  for (const task of tasks) {
    els.list.appendChild(buildTaskElement(task));
  }

  updateStats();
}

function buildTaskElement(task) {
  const node = els.template.content.firstElementChild.cloneNode(true);
  const check = node.querySelector(".check");
  const view = node.querySelector(".task-view");
  const editForm = node.querySelector(".task-edit");
  const title = node.querySelector(".task-title");
  const description = node.querySelector(".task-description");
  const meta = node.querySelector(".task-meta");
  const editTitle = node.querySelector(".edit-title");
  const editDescription = node.querySelector(".edit-description");

  node.dataset.id = task.id;
  node.classList.toggle("is-completed", task.completada);
  title.textContent = task.title;
  description.textContent = task.description;
  meta.textContent = timeAgo(task.creada_en);
  check.setAttribute("aria-label", task.completada ? "Marcar como pendiente" : "Marcar como completada");

  check.addEventListener("click", async () => {
    try {
      const updated = await api(`/api/tareas/${task.id}`, {
        method: "PATCH",
        body: JSON.stringify({ completada: !task.completada }),
      });
      replaceTask(updated);
      render();
    } catch (error) {
      showToast(error.message, "error");
    }
  });

  node.querySelector(".delete-task").addEventListener("click", async () => {
    try {
      await api(`/api/tareas/${task.id}`, { method: "DELETE" });
      state.tasks = state.tasks.filter((item) => item.id !== task.id);
      render();
      showToast("Tarea eliminada");
    } catch (error) {
      showToast(error.message, "error");
    }
  });

  const startEdit = () => {
    editTitle.value = task.title;
    editDescription.value = task.description;
    view.hidden = true;
    editForm.hidden = false;
    editTitle.focus();
    editTitle.select();
  };

  const stopEdit = () => {
    view.hidden = false;
    editForm.hidden = true;
  };

  node.querySelector(".edit-task").addEventListener("click", startEdit);
  node.querySelector(".cancel-edit").addEventListener("click", stopEdit);

  editForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    try {
      const updated = await api(`/api/tareas/${task.id}`, {
        method: "PATCH",
        body: JSON.stringify({
          titulo: editTitle.value,
          descripcion: editDescription.value,
        }),
      });
      replaceTask(updated);
      render();
      showToast("Tarea actualizada");
    } catch (error) {
      showToast(error.message, "error");
    }
  });

  return node;
}

function replaceTask(updated) {
  state.tasks = state.tasks.map((task) => (task.id === updated.id ? updated : task));
}

async function loadTasks() {
  try {
    state.tasks = await api("/api/tareas");
    render();
  } catch (error) {
    showToast(error.message, "error");
  }
}

els.form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const title = els.title.value.trim();

  if (!title) {
    els.title.focus();
    return;
  }

  try {
    await api("/api/tareas", {
      method: "POST",
      body: JSON.stringify({
        titulo: title,
        descripcion: els.description.value.trim(),
      }),
    });
    els.form.reset();
    els.title.focus();
    await loadTasks();
    showToast("Tarea añadida");
  } catch (error) {
    showToast(error.message, "error");
  }
});

els.description.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    els.form.requestSubmit();
  }
});

document.querySelectorAll(".filter").forEach((button) => {
  button.addEventListener("click", () => {
    state.filter = button.dataset.filter;
    document.querySelectorAll(".filter").forEach((item) => {
      item.classList.toggle("is-active", item === button);
    });
    render();
  });
});

els.clearCompleted.addEventListener("click", async () => {
  try {
    await api("/api/tareas/completadas", { method: "DELETE" });
    await loadTasks();
    showToast("Tareas completadas eliminadas");
  } catch (error) {
    showToast(error.message, "error");
  }
});

loadTasks();
