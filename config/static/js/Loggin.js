function Iniciar() {
  var email = document.getElementById("email").value;

  var contraseña = document.getElementById("contraseña").value;

  if (email == "admin" && contraseña == "123") {
    alert("Iniciaste sesion ");
    console.log(email);
    console.log(contraseña);
  } else {
    alert("Por favor verificar");
    
  }
}
