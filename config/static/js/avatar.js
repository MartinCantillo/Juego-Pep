const main_img = document.querySelector('.main_img') 
const thumbnails = document.querySelectorAll('.thumbnail') 

thumbnails.forEach (thumb => {
    thumb.addEventListener('click', function(){ 
        const active = document.querySelector('.active')
        active.classList.remove('active') 
        thumb.classList.add("active")
        main_img.src = thumb.src
    })
})

document.getElementById("backButton").addEventListener("click", function() {
    history.back();
  });

/*const selectButton = document.getElementById('selectButton');


selectButton.addEventListener('click', () => {
  // Obtener el avatar seleccionado
  const selectedAvatar = document.querySelector('.thumbnail.selected');

  if (selectedAvatar) {
    // Realizar alguna acción con el avatar seleccionado
    console.log(`Avatar seleccionado: ${selectedAvatar.alt}`);
  } else {
    console.log('No se ha seleccionado ningún avatar');
  }
});*/

var selectButton = document.getElementById('selectButton');
        var mainAvatar = document.getElementById('mainAvatar');
        
        selectButton.addEventListener('click', function() {
            // Obtiene la ruta del avatar seleccionado
            var selectedAvatar = document.querySelector('.thumbnail.active').src;
            
            // Guarda la ruta del avatar seleccionado en el almacenamiento local
            localStorage.setItem('selectedAvatar', selectedAvatar);
            
            // Redirecciona a la misma página
            window.location.href = window.location.href;
        });
        
        // Verifica si hay un avatar seleccionado guardado en el almacenamiento local
        var savedAvatar = localStorage.getItem('selectedAvatar');
        
        if (savedAvatar) {
            // Si hay un avatar seleccionado guardado, muestra ese avatar en la página
            mainAvatar.src = savedAvatar;
        }else {
          // Si no hay un avatar seleccionado guardado, muestra el primer avatar
          var firstAvatar = document.querySelector('.thumbnail');
          mainAvatar.src = firstAvatar.src;
          firstAvatar.classList.add('active');
      }