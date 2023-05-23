const open1 = document.getElementById('btn_open1');
const modal_container1 = document.getElementById('popUp1');
const cerrar1 = document.getElementById('btn_cerrar1');

const open2 = document.getElementById('btn_open2');
const modal_container2 = document.getElementById('popUp2');
const cerrar2 = document.getElementById('btn_cerrar2');

const open3 = document.getElementById('btn_open3');
const modal_container3 = document.getElementById('popUp3');
const cerrar3 = document.getElementById('btn_cerrar3');

const open4 = document.getElementById('btn_open4');
const modal_container4 = document.getElementById('popUp4');
const cerrar4 = document.getElementById('btn_cerrar4');

const open5 = document.getElementById('btn_open5');
const modal_container5 = document.getElementById('popUp5');
const cerrar5 = document.getElementById('btn_cerrar5');

const open6 = document.getElementById('btn_open6');
const modal_container6 = document.getElementById('popUp6');
const cerrar6 = document.getElementById('btn_cerrar6');

const open7 = document.getElementById('btn_open7');
const modal_container7 = document.getElementById('popUp7');
const cerrar7 = document.getElementById('btn_cerrar7');

const open8 = document.getElementById('btn_open8');
const modal_container8 = document.getElementById('popUp8');
const cerrar8 = document.getElementById('btn_cerrar8');

const open9 = document.getElementById('btn_open9');
const modal_container9 = document.getElementById('popUp9');
const cerrar9 = document.getElementById('btn_cerrar9');

const open10 = document.getElementById('btn_open10');
const modal_container10 = document.getElementById('popUp10');
const cerrar10 = document.getElementById('btn_cerrar10');

const nuevoJuego = document.getElementById('btn_nuevo');

const imgChange1 = document.getElementById('imgChange1');
const imgChange2 = document.getElementById('imgChange2');
const imgChange3 = document.getElementById('imgChange3');
const imgChange4 = document.getElementById('imgChange4');
const imgChange5 = document.getElementById('imgChange5');
const imgChange6 = document.getElementById('imgChange6');
const imgChange7 = document.getElementById('imgChange7');
const imgChange8 = document.getElementById('imgChange8');
const imgChange9 = document.getElementById('imgChange9');
const imgChange10 = document.getElementById('imgChange10');


const jugar1 = document.getElementById('btn_jugar1');

//         Interaccion Nivel 1
open1.addEventListener('click', () => {
    modal_container1.classList.add('show');
});

cerrar1.addEventListener('click', () => {
    modal_container1.classList.remove('show');
});

jugar1.addEventListener('click', () => {
    imgChange1.src = '/config/static/img/JugandoImg/Win/nivel1Win.png';
});


//         Interaccion Nivel 2
open2.addEventListener('click', () => {
    modal_container2.classList.add('show');
});

cerrar2.addEventListener('click', () => {
    modal_container2.classList.remove('show');
});


//         Interaccion Nivel 3
open3.addEventListener('click', () => {
    modal_container3.classList.add('show');
});

cerrar3.addEventListener('click', () => {
    modal_container3.classList.remove('show');
});


//         Interaccion Nivel 4
open4.addEventListener('click', () => {
    modal_container4.classList.add('show');
});

cerrar4.addEventListener('click', () => {
    modal_container4.classList.remove('show');
});


//         Interaccion Nivel 5
open5.addEventListener('click', () => {
    modal_container5.classList.add('show');
    
});

cerrar5.addEventListener('click', () => {
    modal_container5.classList.remove('show');
});


//         Interaccion Nivel 6
open6.addEventListener('click', () => {
    modal_container6.classList.add('show');
});

cerrar6.addEventListener('click', () => {
    modal_container6.classList.remove('show');
});


//         Interaccion Nivel 7
open7.addEventListener('click', () => {
    modal_container7.classList.add('show');
});

cerrar7.addEventListener('click', () => {
    modal_container7.classList.remove('show');
});


//         Interaccion Nivel 8
open8.addEventListener('click', () => {
    modal_container8.classList.add('show');
});

cerrar8.addEventListener('click', () => {
    modal_container8.classList.remove('show');
});


//         Interaccion Nivel 9
open9.addEventListener('click', () => {
    modal_container9.classList.add('show');
});

cerrar9.addEventListener('click', () => {
    modal_container9.classList.remove('show');
});


//         Interaccion Nivel 10
open10.addEventListener('click', () => {
    modal_container10.classList.add('show');
});

cerrar10.addEventListener('click', () => {
    modal_container10.classList.remove('show');
});

//             Nuevo juego
nuevoJuego.addEventListener('click', () => {
    imgChange1.src = '/config/static/img/JugandoImg/Lost/nivel1Lost.png';
    imgChange2.src = '/config/static/img/JugandoImg/Lost/nivel2Lost.png';
    imgChange3.src = '/config/static/img/JugandoImg/Lost/nivel3Lost.png';
    imgChange4.src = '/config/static/img/JugandoImg/Lost/nivel4Lost.png';
    imgChange5.src = '/config/static/img/JugandoImg/Lost/nivel5Lost.png';
    imgChange6.src = '/config/static/img/JugandoImg/Lost/nivel6Lost.png';
    imgChange7.src = '/config/static/img/JugandoImg/Lost/nivel7Lost.png';
    imgChange8.src = '/config/static/img/JugandoImg/Lost/nivel8Lost.png';
    imgChange9.src = '/config/static/img/JugandoImg/Lost/nivel9Lost.png';
    imgChange10.src = '/config/static/img/JugandoImg/Lost/nivel10Lost.png';
});


//             Cambio imagen

