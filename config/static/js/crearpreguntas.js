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
        option.value = datos[key].nombre_tematica;
        selectElement.appendChild(option);
      }
    })
    .catch(function (error) {
      console.error(error);
    });
    console.log(selectElement);
}
