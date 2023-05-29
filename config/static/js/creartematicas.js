function saveTematica() {
  const nomTematica = document.getElementById("nombreTematica").value;
  const puntos = document.getElementById("topeTematica").value;
  if (nomTematica == "" || puntos == "") {
    alert("Todos los campos son obligatorios");
  } else {
    //Consumir la API Con metodo Post
    let endpoint = "/savetematica";

    axios
      .post(endpoint, {
        nombre_tematica: nomTematica,
        tope_tem: puntos,
      })
      .then(function (response) {
        document.getElementById("nombreTematica").value = "";
        document.getElementById("topeTematica").value = "";
      })
      .catch(function (error) {
        console.log(error);
      });
    alert("Cambios guardados exitosamente.");
  }
}
