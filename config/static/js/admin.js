// Seleccionamos los elementos del DOM necesarios
const createGameCard = document.querySelector("#crearjuego");
const createdByMeCard = document.querySelector("#creadospormi");
const changeRoleCard = document.querySelector("#cambiarrol");

// Agregamos el evento click a cada tarjeta
createGameCard.addEventListener("click", () => {
  window.location.href = "/crearjuego";
});

createdByMeCard.addEventListener("click", () => {
  window.location.href = "/creadospormi";
});

changeRoleCard.addEventListener("click", () => {
  window.location.href = "/cambiarrol";
});
