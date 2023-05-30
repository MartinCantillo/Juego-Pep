//funcion para cargar las tematicas registradas
function cargarTematica() {
  const selectElement = document.getElementById("selTematicas");
  const tematicaN = document.getElementById("selectT");
  let endpoint = "/consultatematica";
  axios.get(endpoint)
    .then(function (response) {
      // La datos contiene los datos devueltos por la API
      const datos = response.data;

      // Iterar sobre los datos y agregar opciones al select
      for (let key in datos) {
        const option = document.createElement("option");
        option.text = datos[key].nombre_tematica;
        selectElement.appendChild(option);
      }
      for (let key in datos) {
        const option = document.createElement("option");
        option.text = datos[key].nombre_tematica;

        tematicaN.appendChild(option);
      }
    })
    .catch(function (error) {
      console.error(error);
    });
}

const crearPreguntaBtn = document.querySelector("#crearpreguntas");
const contenedorPregunta = document.querySelector(".contenedor");
const btnCancelar = document.querySelector(".cancel-button");
const btnActualizar = document.querySelector(".refresh-button");
const btnGuardar = document.querySelector(".save-button");

//ocultar los contenedores de crear pregunta y el de la tabla
crearPreguntaBtn.onclick = function () {
  contenedorPregunta.classList.toggle("open");
  const isOpen = contenedorPregunta.classList.contains("open");
  crearPreguntaBtn.classList = isOpen ? "card-pregunta open" : "card-pregunta";
  document.getElementById("btnActualizar").style.display = "none";
  document.getElementById("btnGuardar").style.display = "block";
  if (isOpen) {
    MostrarCrearPregunta();
    btnCancelar.onclick = function () {
      contenedorPregunta.classList.remove("open");
      crearPreguntaBtn.classList.remove("open");
      const isOpen = false;
      crearPreguntaBtn.classList = "card-pregunta";
      document.getElementById("crearpreguntas").style.display = "flex";
      CancelarPregunta();
    };
    btnGuardar.onclick = function () {
      guardarRespuestas();
    };
  } else {
    CancelarPregunta();
  }
};

function MostrarCrearPregunta() {
  // Ocultar elementos que no se mostrarán
  document.getElementById("tituloJuego").style.display = "none";
  document.getElementById("crearpreguntas").style.display = "none";
  document.getElementById("preguntas-creadas").style.display = "none";

  // Mostrar elementos que se mostrarán
  document.getElementById("contenedor").style.display = "block";
  document.getElementById("header-pregunta").style.display = "block";
  document.getElementById("footer").style.display = "flex";
}

function CancelarPregunta() {
  // Mostrar elementos que se ocultaron al crear la pregunta
  document.getElementById("tituloJuego").style.display = "none";
  document.getElementById("crearpreguntas").style.display = "flex";
  document.getElementById("preguntas-creadas").style.display = "flex";

  // Ocultar el contenido de la pregunta creada
  document.getElementById("contenedor").style.display = "none";
  document.getElementById("header-pregunta").style.display = "none";
  document.getElementById("footer").style.display = "none";
}

var enunciadoGlobal = "";
function GuardarPregunta() {
  const enunciado = document.getElementById("enunciado").querySelector("p").textContent;
  enunciadoGlobal = enunciado;
  const tituloP = document.getElementById("tituloP").value;
  const puntos = document.getElementById("puntos").value;
  const tematicaN = document.getElementById("selTematicas").value;

  if (tituloP === "" || enunciado === "" || tematicaN === "Seleccionar") {
    alert("Todos los campos son obligatorios");
  } else {
    let url = "/consultatematica";
    axios.get(url, {
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
        axios.post(endpoint2, {
          NomCorto: tituloP,
          Idtematica_FK: idTematica,
          enunciado: enunciado,
          puntos: puntos,
        })
          .then(function (response) {
            alert(response);
            //Funcion para consultar a la bd para obtener la pk de la pregunta
            obtenerIdPreguntas();
            // Limpiar el contenido de los elementos HTML
            document.getElementById("tituloP").value = "";
            document.getElementById("enunciado").querySelector("p").textContent = "";
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
}

function respuestaCorrecta() {
  var inputsRadio = document.querySelectorAll('input[type="radio"]');
  // Agrega un evento a cada input de radio
  inputsRadio.forEach(function (input) {
    input.addEventListener("change", obtenerParrafo);
  });
}

// Función para obtener el párrafo asociado al input de radio seleccionado
var respCorrecta = "";
function obtenerParrafo(event) {
  var contenedorP = event.target.closest(".contenedor-option");
  var parrafo = contenedorP.querySelector("p");
  var valorParrafo = parrafo.textContent;
  respCorrecta = valorParrafo;
}

var idPreguntaActu = "";
var idPreguntaGlobal = "";
function obtenerIdPreguntas() {
  const enunciados = document.getElementById("enunciado").querySelector("p").textContent;
  // Cargar el id de la pregunta
  let url2 = "/consultapregunta";
  // se consulta por enunciado
  axios.get(url2, {
    params: {
      enunciado: enunciados,
    },
  })
    .then((response) => {
      const preguntas = response.data;
      let idPregunta = null;

      Object.values(preguntas).forEach((Pregunta) => {
        if (Pregunta.enunciado === enunciados) {
          idPregunta = Pregunta.id;
          // console.log("ID de la pregunta desde el if:", idPregunta);
        }
      });
      //console.log("ID de la pregunta: fuera del if", idPregunta);
      idPreguntaActu = idPregunta;
      idPreguntaGlobal = idPregunta;
    });
}

function guardarRespuestas() {
  // console.log("idPreguntaActu metodo guardar respuestas" + idPreguntaActu);

  var puntosAct = 0;
  var puntosAct1 = 0;
  var puntosAct2 = 0;
  var puntosAct3 = 0;
  // const enunciados = document.getElementById("enunciado").querySelector("p").textContent;
  const resp0 = document.getElementById("resp0").querySelector("p").textContent;
  const resp1 = document.getElementById("resp1").querySelector("p").textContent;
  const resp2 = document.getElementById("resp2").querySelector("p").textContent;
  const resp3 = document.getElementById("resp3").querySelector("p").textContent;
  const puntos = document.getElementById("puntos").value;
  //se valida que por lo menos este seleccionado una respuesa
  const radioSeleccionado = document.querySelector(
    'input[name="opciones"]:checked'
  );
  if (
    !radioSeleccionado || resp0 == "" || resp1 == "" || resp2 == "" || resp3 == "" || idPreguntaActu == "") {
    alert("Por favor verificar");
  } else {
    if (resp0 === respCorrecta) {
      puntosAct = puntos;
    } else if (resp1 === respCorrecta) {
      puntosAct1 = puntos;
    } else if (resp2 === respCorrecta) {
      puntosAct2 = puntos;
    } else if (resp3 === respCorrecta) {
      puntosAct3 = puntos;
    }

    //Consumir la API Con metodo Post
    let endpoint = "/saverespuesta";
    //1
    axios.post(endpoint, {
      EnuncRespu: resp0,
      PuntosRespu: puntosAct,
      IDpregunta_FK: idPreguntaActu,
    })
      .then(function (response) {
        alert("Guardado con éxito");
      })
      .catch(function (error) {
        console.log(error);
      });

    //2
    axios.post(endpoint, {
      EnuncRespu: resp1,
      PuntosRespu: puntosAct1,
      IDpregunta_FK: idPreguntaActu,
    })
      .then(function (response) { })
      .catch(function (error) {
        console.log(error);
      });

    //3
    axios.post(endpoint, {
      EnuncRespu: resp2,
      PuntosRespu: puntosAct2,
      IDpregunta_FK: idPreguntaActu,
    })
      .then(function (response) { })
      .catch(function (error) {
        console.log(error);
      });

    //4
    axios.post(endpoint, {
      EnuncRespu: resp3,
      PuntosRespu: puntosAct3,
      IDpregunta_FK: idPreguntaActu,
    })
      .then(function (response) { })
      .catch(function (error) {
        console.log(error);
      });

    //volver a la pantalla de preguntas
    contenedorPregunta.classList.remove("open");
    crearPreguntaBtn.classList.remove("open");
    const isOpen = false;
    crearPreguntaBtn.classList = "card-pregunta";
    document.getElementById("crearpreguntas").style.display = "flex";
    CancelarPregunta();
  }
}

var temtica = "";
//funcion para llenar la tabla con las preguntas registradas
function LlenarTabla() {
  let idTematica = null;
  const temati = document.getElementById("selectT").value;
  temtica = temati;
  if (temati == "Seleccionar") {
    alert("Por favor verifica");
  } else {
    // Hago consulta para obtener el Pk de la tematica
    let urlT = "/consultatematica";
    axios
      .get(urlT, {
        params: {
          nombre_tematica: temati,
        },
      })
      .then((response) => {
        const tematicas = response.data;

        Object.values(tematicas).forEach((tematica) => {
          if (tematica.nombre_tematica === temati) {
            idTematica = tematica.id;
          }
        });
        const tablaPreguntas = document
          .getElementById("tabla-preguntas")
          .getElementsByTagName("tbody")[0];
        tablaPreguntas.innerHTML = "";
        axios.post("/consultaP", {
          Idtematica_FK: idTematica,
        })
          .then(function (response) {
            const preguntas = response.data;
            // Itera sobre las preguntas y las agrega a la tabla
            Object.values(preguntas).forEach(function (pregunta) {
              const row = tablaPreguntas.insertRow();
              row.insertCell(0).innerHTML = pregunta.id;
              row.insertCell(1).innerHTML = pregunta.enunciado;
            });
            agregarBotonesConIconos();
          })
          .catch(function (error) {
            console.error(error);
          });
      });
  }
}

var idPreE = "";
var idPre = "";
var tabla = document.getElementById("tabla-preguntas");
function agregarBotonesConIconos() {
  var tabla = document.getElementById("tabla-preguntas");
  var filas = tabla.getElementsByTagName("tr");

  for (var i = 1; i < filas.length; i++) {
    var celdaOpciones = filas[i].insertCell(-1);

    var botonEditar = document.createElement("button");
    botonEditar.classList.add("icono-boton");
    botonEditar.title = "Editar";

    var iconoEditar = document.createElement("i");
    iconoEditar.classList.add("fas", "fa-edit"); // Clases de Font Awesome para el icono de editar

    botonEditar.appendChild(iconoEditar);
    celdaOpciones.appendChild(botonEditar);

    botonEditar.onclick = function () {
      var fila = this.parentNode.parentNode; // Obtener la fila correspondiente al botón
      idPre = fila.cells[0].innerHTML; // Obtener el ID de la pregunta de la celda correspondiente
      document.getElementById("btnActualizar").style.display = "block";
      document.getElementById("btnGuardar").style.display = "none";
      // editar la pregunta
      contenedorPregunta.classList.toggle("open");
      const isOpen = contenedorPregunta.classList.contains("open");
      crearPreguntaBtn.classList = isOpen
        ? "card-pregunta open"
        : "card-pregunta";
      cargarPregyResp();

      if (isOpen) {
        MostrarCrearPregunta();
        btnCancelar.onclick = function () {
          contenedorPregunta.classList.remove("open");
          crearPreguntaBtn.classList.remove("open");
          const isOpen = false;
          crearPreguntaBtn.classList = "card-pregunta";
          document.getElementById("crearpreguntas").style.display = "flex";
          CancelarPregunta();
        };
        btnActualizar.onclick = function () {
          editar();
        };
      } else {
        CancelarPregunta();
      }
    };

    var botonEliminar = document.createElement("button");
    botonEliminar.classList.add("icono-boton");
    botonEliminar.title = "Eliminar";

    var iconoEliminar = document.createElement("i");
    iconoEliminar.classList.add("fas", "fa-trash-alt"); // Clases de Font Awesome para el icono de eliminar

    botonEliminar.appendChild(iconoEliminar);
    celdaOpciones.appendChild(botonEliminar);
    botonEliminar.onclick = function () {
      var fila = this.parentNode.parentNode; // Obtener la fila correspondiente al botón
      idPreE = fila.cells[0].innerHTML; // Obtener el ID de la pregunta de la celda correspondiente
      eliminarrPregYResp();
    };
  }
}

var idpregg = "";
function cargarPregyResp() {
  const select = document.getElementById("selTematicas");
  select.value = temtica;
  let cargarurl = "/cargardatosp";
  let datosDiv = document.getElementById("enunciado");
  let datosResp0 = document.getElementById("resp0").querySelector("p");
  let datosResp1 = document.getElementById("resp1").querySelector("p");
  let datosResp2 = document.getElementById("resp2").querySelector("p");
  let datosResp3 = document.getElementById("resp3").querySelector("p");

  //Obtener radios
  const input0 = document.getElementById("input0");
  const input01 = document.getElementById("input01");
  const input02 = document.getElementById("input02");
  const input03 = document.getElementById("input03");
  idpregg = idPre;
  axios.post(cargarurl, {
    id: idPre,
  })
    .then(function (response) {
      var jsonData = response.data;
      for (var i = 1; i <= Object.keys(jsonData).length; i++) {
        var pregunta = jsonData[i].enunciado;
        var repts0 = jsonData[1].EnuncRespu;
        var repts1 = jsonData[2].EnuncRespu;
        var repts2 = jsonData[3].EnuncRespu;
        var repts3 = jsonData[4].EnuncRespu;
        var preguntaParrafo = datosDiv.querySelector("p");
        preguntaParrafo.innerText = pregunta;
        datosResp0.innerText = repts0;
        datosResp1.innerText = repts1;
        datosResp2.innerText = repts2;
        datosResp3.innerText = repts3;
        if (jsonData[i].PuntosRespu != 0) {
          //valido ahora lo que dice el enunciado para seleccionar el input
          if (jsonData[i].EnuncRespu == repts0) {
            input0.checked = true;
          }
          if (jsonData[i].EnuncRespu == repts1) {
            input01.checked = true;
          }
          if (jsonData[i].EnuncRespu == repts2) {
            input02.checked = true;
          }
          if (jsonData[i].EnuncRespu == repts3) {
            input03.checked = true;
          }
        }
      }
    })
    .catch(function (error) {
      console.log(error);
    })
    .finally(function () {
      // always executed
    });
}

function eliminarrPregYResp() {

  alert("Se elimino con exito id pregunta" + idPreE);

  let UrlP = "/delpregunta";
  let UrlR = "/delrespuestas";

  axios.post(UrlR, {
    IDpregunta_FK: idPreE,
  })
    .then(function (response) {
      axios.post(UrlP, {
        id: idPreE,
      })
        .then(function (response) {
        })
        .catch(function (error) {
          console.log(error);
        });
    })
    .catch(function (error) {
      console.log(error);
    });
}

function editar() {
  alert("Entro a editar pregunta codigo :" + idpregg);
  //volver a la pantalla de pregunta
  contenedorPregunta.classList.remove("open");
  crearPreguntaBtn.classList.remove("open");
  const isOpen = false;
  crearPreguntaBtn.classList = "card-pregunta";
  document.getElementById("crearpreguntas").style.display = "flex";
}
  //alert("Entro a editar codigo pregunta " + idpregg);
/*const enunciado2 = document
  .getElementById("enunciado")
  .querySelector("p").textContent;
let UpdateP = "/actualizarpreg";
axios
  .post(UpdateP, {
    id: idpregg,
    enunciado: enunciado2,
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });
  */

