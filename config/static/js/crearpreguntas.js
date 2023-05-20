function cargarTematica() {
  // Obtén una referencia al elemento 'select' en tu HTML
  const selectElement = document.getElementById("selTematicas");

  let endpoint = "/consultatematica";
  axios.get(endpoint)
    .then(function (response) {
      // La respuesta contiene los datos devueltos por la API
      const datos = response.data;

      // Iterar sobre los datos y agregar opciones al select
      for (let key in datos) {
        const option = document.createElement("option");
        option.text = datos[key].nombre_tematica;
        selectElement.appendChild(option);
      }
    })
    .catch(function (error) {
      console.error(error);
    });
   
}

const crearPreguntaBtn = document.querySelector('#crearpreguntas')
const contenedorPregunta = document.querySelector('.contenedor')
const headerPregunta = document.querySelector('#header-pregunta')
const footerPregunta = document.querySelector('.footer')

crearPreguntaBtn.onclick = function() {
  contenedorPregunta.classList.toggle('open')
  const isOpen = contenedorPregunta.classList.contains('open')
  crearPreguntaBtn.classList = isOpen
  ? 'card-pregunta open'
  : 'card-pregunta'
}
