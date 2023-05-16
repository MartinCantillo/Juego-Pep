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

  const selectButton = document.getElementById('selectButton');


selectButton.addEventListener('click', () => {
  // Obtener el avatar seleccionado
  const selectedAvatar = document.querySelector('.thumbnail.selected');

  if (selectedAvatar) {
    // Realizar alguna acción con el avatar seleccionado
    console.log(`Avatar seleccionado: ${selectedAvatar.alt}`);
  } else {
    console.log('No se ha seleccionado ningún avatar');
  }
});

  