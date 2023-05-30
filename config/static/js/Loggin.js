function Iniciar(){
  let endpoint ='/valiusuarios'
  const txtuser = document.getElementById('usuario')
  const txtpsw = document.getElementById('contraseña')
  var txtopc1 = document.getElementById('opcion1')
  var txtopc2 = document.getElementById('opcion2')

  if(txtopc1.value == 1 & txtopc2.value == 1){
    alert("Elegir una sola opcion")
  }
  if(txtopc1.value == 1 & txtopc2.value == 0 ){
    axios.post(endpoint,{
      'emailusuario_pk' : txtuser.value,
      'clave_usuario' : txtpsw.value
    })
    .then(function (response) {
      let data = response.data;
      let sucess = data[0].payload;
      sucess ? window.location.href= '/menuprincipal' : alert('Usuario Invalido');
    })
    .catch(function (error) {
      console.log(error);
    });
  }
  if(txtopc1.value == 0 & txtopc2.value == 1 ){
    axios.post(endpoint,{
      'emailusuario_pk' : txtuser.value,
      'clave_usuario' : txtpsw.value
    })
    .then(function (response) {
      let data = response.data;
      let sucess = data[0].payload;
      sucess ? window.location.href= '/menuadmin' : alert('Usuario Invalido');
    })
    .catch(function (error) {
      console.log(error);
    });
  }
  
}