function Iniciar(){
  let endpoint ='/valiusuarios'
  const txtuser = document.getElementById('usuario')
  const txtpsw = document.getElementById('contraseña')

  axios.post(endpoint,{
    'emailusuario_pk' : txtuser.value,
    'clave_usuario' : txtpsw.value
  })
  .then(function (response) {
    alert(response);
  })
  .catch(function (error) {
    console.log(error);
  });
}

