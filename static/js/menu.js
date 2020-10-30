/**
 *MENU SECUNDARIO */
var menuDoc = document.getElementsByClassName('link-nav-arrow')[0];
var listSecond = document.querySelector(".list-nav-second");

menuDoc.addEventListener("click", function() {
    listSecond.classList.toggle('hide');
    menuDoc.classList.toggle('arrow');

});


/**
 * MEnu HAMBURGUER
 * acionar o menu
 */

var iconMenu = document.querySelector(".icon-menu");
var menu = document.querySelector(".menu");
var conteudo = document.querySelector(".content");

iconMenu.addEventListener("click", function() {
    menu.classList.toggle("menu__move");
    conteudo.classList.toggle("content-move");

});