function saveNivel() {
    const nomNivel = document.getElementById("nivel_input2").value;
    if (nomNivel == "") {
      alert("El campo es obligatorio");
    } else {
      //Consumir la API Con metodo Post
      let endpoint = "/savenivel";
  
      axios
        .post(endpoint, {
            nombre_nv: nomNivel,
        })
        .then(function (response) {
            document.getElementById("nivel_input2").value = "";
        })
        
        .catch(function (error) {
          console.log(error);
        });
      alert("Cambios guardados exitosamente.");
    }
  }
