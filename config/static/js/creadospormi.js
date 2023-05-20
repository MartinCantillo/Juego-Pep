/*// Seleccionamos los elementos del DOM necesarios
const menuBtn = document.querySelectorAll(".menu-button");
const menu = document.querySelectorAll(".menu");

// Agregamos un evento click a cada botón de menú
menuBtn.forEach((btn) => {
  btn.addEventListener("click", (event) => {
    // Obtenemos el menú correspondiente
    const menu = event.target.nextElementSibling;
    // Mostramos o escondemos el menú
    menu.classList.toggle("show");
  });
});

// Agregamos un evento click a cada opción del menú
const editBtns = document.querySelectorAll(".edit-button");
const deleteBtns = document.querySelectorAll(".delete-button");

editBtns.forEach((btn) => {
  btn.addEventListener("click", (event) => {
    console.log("Editar");
    // Aquí iría el código para editar el juego
  });
});

deleteBtns.forEach((btn) => {
  btn.addEventListener("click", (event) => {
    console.log("Eliminar");
    // Aquí iría el código para eliminar el juego
  });
});
*/
