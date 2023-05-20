function saveTematica() {
  const nomTematica = document.getElementById("nombreTematica").value;
  const puntos = document.getElementById("topeTematica").value;
  //Consumir la API Con metodo Post
  let endpoint = "/savetematica";

  axios
    .post(endpoint, {
      "nombre_tematica": nomTematica,
      "tope_tem": puntos,
    })
    .then(function (response) {
      alert(response);
    })
    .catch(function (error) {
      console.log(error);
    });
    alert("Cambios guardados exitosamente.");
}
