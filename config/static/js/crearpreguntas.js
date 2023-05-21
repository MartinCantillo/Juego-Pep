function cargarTematica() {
  // Obtiene una referencia al elemento 'select' en tu HTML
  const selectElement = document.getElementById("selTematicas");

  let endpoint = "/consultatematica";
  axios
    .get(endpoint)
    .then(function (response) {
      // La datos contiene los datos devueltos por la API
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

crearPreguntaBtn.onclick = function () {
  contenedorPregunta.classList.toggle("open");
  const isOpen = contenedorPregunta.classList.contains("open");
  crearPreguntaBtn.classList = isOpen ? "card-pregunta open" : "card-pregunta";
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
          //Funcion para consultar a la bd para obtener la pk de la pregunta
          obtenerIdPreguntas( );
        })
        .catch(function (error) {
          console.log(error);
        });
       
      alert("Pregunta guardada con éxito.");
      
    })
    .catch((error) => {
      alert("Error al obtener el ID de la temática:", error);
    });

    
}

function respuestaCorrecta() {
  // Obtén todos los inputs de radio
  var inputsRadio = document.querySelectorAll('input[type="radio"]');

  // Agrega un evento de escucha a cada input de radio
  inputsRadio.forEach(function (input) {
    input.addEventListener("change", obtenerParrafo);
  });
 
}
// Función para obtener el párrafo asociado al input de radio seleccionado

var respCorrecta = "";
function obtenerParrafo(event) {
  // Obtén el contenedor padre del input de radio
  var contenedorP = event.target.closest(".contenedor-option");

  // Obtén el párrafo dentro del contenedor
  var parrafo = contenedorP.querySelector("p");

  // Obtén el valor del párrafo
  var valorParrafo = parrafo.textContent;
  respCorrecta = valorParrafo;
 
}



var idPreguntaActu="" ;
function obtenerIdPreguntas( ) {

  const enunciados = document.getElementById("enunciado").value;
  // Cargar el id de la pregunta
  let url2 = "/consultapregunta";
  // se consulta por enunciado
  axios.get(url2, {
      params: {
        "enunciado": enunciados,
      },
    }).then((response) => {
      const preguntas = response.data;
      let idPregunta = null;
    
      Object.values(preguntas).forEach((Pregunta) => {
        if (Pregunta.enunciado === enunciados) {
          idPregunta = Pregunta.id;
          console.log("ID de la pregunta desde el if:", idPregunta);
        }
      });
      console.log("ID de la pregunta: fuera del if", idPregunta);
      idPreguntaActu=idPregunta
    });

}

function guardarRespuestas() {
  console.log("idPreguntaActu"+idPreguntaActu)
 
  var puntosAct = 0;
  var puntosAct1 = 0;
  var puntosAct2 = 0;
  var puntosAct3 = 0;
  const resp0 = document.getElementById("resp0").querySelector("p").textContent;
  const resp1 = document.getElementById("resp1").querySelector("p").textContent;
  const resp2 = document.getElementById("resp2").querySelector("p").textContent;
  const resp3 = document.getElementById("resp3").querySelector("p").textContent;
  const puntos = document.getElementById("puntos").value;

  if (resp0 === respCorrecta) {
    puntosAct = puntos;
    alert("es igual a resp0 puntos " + puntosAct);
  } else if (resp1 === respCorrecta) {
    puntosAct1 = puntos;
    alert("es igual a resp1 y puntos " + puntosAct1);
  } else if (resp2 === respCorrecta) {
    puntosAct2 = puntos;
    alert("es igual a resp2 puntos " + puntosAct2);
  } else if (resp3 === respCorrecta) {
    puntosAct3 = puntos;
    alert("es igual a resp3 puntos " + puntosAct3);
  }

  //Consumir la API Con metodo Post
  let endpoint = "/saverespuesta";
  //1
  axios
    .post(endpoint, {
      EnuncRespu: resp0,
      PuntosRespu: puntosAct,
      IDpregunta_FK: idPreguntaActu,
    })
    .then(function (response) {
      alert(response);
    })
    .catch(function (error) {
      console.log(error);
    });

  //2
  axios
    .post(endpoint, {
      EnuncRespu: resp1,
      PuntosRespu: puntosAct1,
      IDpregunta_FK: idPreguntaActu,
    })
    .then(function (response) {
      alert(response);
    })
    .catch(function (error) {
      console.log(error);
    });
  //3
  axios
    .post(endpoint, {
      EnuncRespu: resp2,
      PuntosRespu: puntosAct2,
      IDpregunta_FK: idPreguntaActu,
    })
    .then(function (response) {
      alert(response);
    })
    .catch(function (error) {
      console.log(error);
    });
  //4
  axios
    .post(endpoint, {
      EnuncRespu: resp3,
      PuntosRespu: puntosAct3,
      IDpregunta_FK: idPreguntaActu,
    })
    .then(function (response) {
      alert(response);
    })
    .catch(function (error) {
      console.log(error);
    });

  window.location.href = "/crearpreguntas";

 
}
