function actualizarC(){
    let endpoint = "/actucontra"
    const txtemail = document.getElementById('email')
    const txtcontra = document.getElementById('contraseña') 
    const txtcontraf = document.getElementById('contraseñaf')

    if(txtcontraf.value == txtcontra.value){
        axios.post(endpoint,{
            'emailusuario_pk' : txtemail.value,
            'clave_usuario' : txtcontra.value
        })
        .then(function (response) {
            alert("Cambio exitoso");
        })
        .catch(function (error) {
          console.log(error);
        });
    }else{
        alert("No coinciden las contraseñas / Usuario no existe")
    }
}