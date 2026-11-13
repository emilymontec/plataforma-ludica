// Registro del service worker e instalación de la PWA.

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("/sw.js").catch((error) => {
      console.error("No se pudo registrar el service worker:", error);
    });
  });
}

const botonInstalar = document.getElementById("boton-instalar");
const ayudaIos = document.getElementById("ayuda-ios");
let solicitudInstalacion = null;

window.addEventListener("beforeinstallprompt", (evento) => {
  evento.preventDefault();
  solicitudInstalacion = evento;
  if (botonInstalar) botonInstalar.hidden = false;
});

if (botonInstalar) {
  botonInstalar.addEventListener("click", async () => {
    if (!solicitudInstalacion) return;
    solicitudInstalacion.prompt();
    await solicitudInstalacion.userChoice;
    solicitudInstalacion = null;
    botonInstalar.hidden = true;
  });
}

const esIos = /iphone|ipad|ipod/i.test(navigator.userAgent);
const yaInstalada = window.matchMedia("(display-mode: standalone)").matches || navigator.standalone;
if (ayudaIos && esIos && !yaInstalada) ayudaIos.hidden = false;
