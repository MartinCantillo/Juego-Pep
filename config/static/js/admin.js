// Seleccionamos los elementos del DOM necesarios
const createTematicsCard = document.querySelector("#creartematicas");
/*const createGameCard = document.querySelector("#crearpreguntas");
const createdByMeCard = document.querySelector("#creadospormi");
const changeRoleCard = document.querySelector("#cambiarrol");

// Agregamos el evento click a cada tarjeta

createGameCard.addEventListener("click", () => {
  window.location.href = "/crearpreguntas";
});

createdByMeCard.addEventListener("click", () => {
  window.location.href = "/creadospormi";
});

changeRoleCard.addEventListener("click", () => {
  window.location.href = "/cambiarrol";
});

createTematicsCard.addEventListener("click", () => {
  window.location.href = "/creartematicas";
});
*/

//Efectos Javascript Todos los derechos reservados.
var d = new Date(); var month = new Array(12); month[0] = 'Enero'; month[1] = 'Febrero'; month[2] = 'Marzo'; month[3] = 'Abril'; month[4] = 'Mayo'; month[5] = 'Junio'; month[6] = 'Julio'; month[7] = 'Agosto'; month[8] = 'Septiembre'; month[9] = 'Octubre'; month[10] = 'Noviembre'; month[11] = 'Diciembre'; var todaysDate = +d.getDate() + ' de ' + month[d.getUTCMonth()] + ' del ' + d.getUTCFullYear();
document.getElementById('fechahoy').innerHTML = 'Hoy es: ' + todaysDate;

function show() {
  var Digital = new Date()
  var hours = Digital.getHours()
  var minutes = Digital.getMinutes()
  var seconds = Digital.getSeconds()
  var dn = "AM"
  if (hours > 12) {
    dn = "PM"
    hours = hours - 12
  }
  if (hours == 0)
    hours = 12
  if (minutes <= 9)
    minutes = "0" + minutes
  if (seconds <= 9)
    seconds = "0" + seconds
  document.Tick.Clock.value = hours + ":" + minutes + ":" +
    seconds + " " + dn
  setTimeout("show()", 1000)
}
show();