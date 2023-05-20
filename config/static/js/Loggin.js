function Iniciar() {
  var email = document.getElementById("email").value;

  var contraseña = document.getElementById("contraseña").value;

  if (email == "admin" && contraseña == "123") {
    alert("Iniciaste sesion ");
  } else {
    alert("Por favor verificar");
    
  }
}
