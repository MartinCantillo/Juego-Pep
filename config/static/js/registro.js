function saveuser(){
    let endpoint = '/saveusuario'
    const txtnom = document.getElementById('nombre')
    const txtemail = document.getElementById('email')
    const txtcontra = document.getElementById('contraseña')
    const txtcontraf = document.getElementById('contraseñaf')


    if (txtcontraf.value == txtcontra.value){
        axios.post(endpoint,{
            'nom_usuario' : txtnom.value ,
            'IdCategoria_Fk' : 1,
            'estado': 'a',
            'clave_usuario': txtcontra.value,
            'avatar_rut': '/static/img/avatar/avatar1.jpg',
            'emailusuario_pk': txtemail.value
        })
        .then(function (response) {
          alert("Usuario creado");
        })
        .catch(function (error) {
          console.log(error);
        });
    }else{
      alert("No coinciden las contraseñas")
    }
}