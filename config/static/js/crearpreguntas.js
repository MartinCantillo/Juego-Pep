function cargarTematica() {
  // Obtén una referencia al elemento 'select' en tu HTML
  const selectElement = document.getElementById("selTematicas");

  let endpoint = "/consultatematica";
  axios
    .get(endpoint)
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

const crearPreguntaBtn = document.querySelector("#crearpreguntas");
const contenedorPregunta = document.querySelector(".contenedor");
const headerPregunta = document.querySelector("#header-pregunta");
const footerPregunta = document.querySelector(".footer");

crearPreguntaBtn.onclick = function () {
  contenedorPregunta.classList.toggle("open");
  const isOpen = contenedorPregunta.classList.contains("open");
  crearPreguntaBtn.classList = isOpen 
  ? "card-pregunta open"
  : "card-pregunta";
};

function GuardarPregunta() {
  const enunciado = document.getElementById("enunciado").value;
  const tituloP = document.getElementById("tituloP").value;
  const puntos = document.getElementById("puntos").value;
  const tematicaN = document.getElementById("selTematicas").value;

  let url = "/consultatematica";
  axios
    .get(url, {
      params: {
        nombre_tematica: tematicaN,
      },
    })
    .then((response) => {
      const tematicas = response.data;
      let idTematica = null;

      Object.values(tematicas).forEach((tematica) => {
        if (tematica.nombre_tematica === tematicaN) {
          idTematica = tematica.id;
        }
      });

      console.log("ID de la temática:", idTematica);

      // Realiza la petición para guardar la pregunta dentro del bloque .then()
      let endpoint2 = "/savepregunta";
      axios
        .post(endpoint2, {
          NomCorto: tituloP,
          Idtematica_FK: idTematica,
          enunciado: enunciado,
          puntos: puntos,
        })
        .then(function (response) {
          alert(response);
        })
        .catch(function (error) {
          console.log(error);
        });

      alert("Pregunta guardada con éxito.");
    })
    .catch((error) => {
      console.error("Error al obtener el ID de la temática:", error);
    });
}
