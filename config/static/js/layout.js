const toggleBtn = document.querySelector('.toggle_btn')
const toggleBtnIcon = document.querySelector('.toggle_btn i')
const menuInferior = document.querySelector('.menu-inferior')

toggleBtn.onclick = function() {
    menuInferior.classList.toggle('open')

    const isOpen = menuInferior.classList.contains('open')

    toggleBtnIcon.classList = isOpen
    ? 'fa-solid fa-xmark'
    : 'fa-solid fa-bars'
}


  