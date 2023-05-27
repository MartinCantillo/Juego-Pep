
  let endpoint ='/traerpregu'
  const txt_pregunta = document.getElementById('txtpregunta')

      axios.get(endpoint,{
          'pregunta' : txt_pregunta.value ,
          
      })
      .then(function (response) {
      let data = response.data;
      let pregunta_bd = data[1].enunciado;
        //alert("pregunta mostrada");
        //alert(data[1].id)
        //alert(data[1].enunciado)
        txt_pregunta.textContent = pregunta_bd;
      })
      .catch(function (error) {
        console.log(error);
      });


