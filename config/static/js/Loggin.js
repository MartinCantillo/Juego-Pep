function Iniciar(){
  let endpoint ='/valiusuarios'
  const txtuser = document.getElementById('usuario')
  const txtpsw = document.getElementById('contraseña')

  axios.post(endpoint,{
    'emailusuario_pk' : txtuser.value,
    'clave_usuario' : txtpsw.value
  })
  .then(function (response) {
    let data = response.data;
    let sucess = data[0].payload;
    sucess ? window.location.href= '/avatar' : alert('Error');
  })
  .catch(function (error) {
    console.log(error);
  });
}

