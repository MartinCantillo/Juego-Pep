function mostrarpregu(){
    let endpoint ='/traerpregu'
    const txt_pregunta = document.getElementById('txtpregunta')

        axios.get(endpoint,{
            'pregunta' : txt_pregunta.value ,
            
        })
        .then(function (response) {
        let data = response.data;
        
          alert("Usuario creado");
        })
        .catch(function (error) {
          console.log(error);
        });

}