function mostrarpregu(){
    let endpoint ='/traerpregu'
    const txt_pregunta = document.getElementById('txtpregunta')

        axios.post(endpoint,{
            'pregunta' : txt_pregunta.value ,
            
        })
        .then(function (response) {
        let data = response.data;
        let pregunta_bd = data[0].enunciado;
        txt_pregunta.value= pregunta_bd;
          alert("pregunta mostrada");
          alert(data[0].id)
          alert(data[0].enunciado)
        })
        .catch(function (error) {
          console.log(error);
        });

}