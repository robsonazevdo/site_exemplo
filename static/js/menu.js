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
//var menu = document.querySelector(".menu");
var conteudo = document.querySelector(".content");

let body = document.querySelector("body");


iconMenu.addEventListener("click", function() {

    body.classList.toggle("__move");
    //menu.classList.toggle("menu__move");
    //conteudo.classList.toggle("content-move");

});
/*recolhimento*/


conteudo.addEventListener("click", function() {

    body.classList.remove("__move");
});


/*
MENU ATIVO
*/

let linkNavs = document.querySelectorAll(".link-nav");

linkNavs.forEach(function(valorcorrente, index, linkNavs) {

    valorcorrente.addEventListener("click", function() {

        linkNavs.forEach(function(element) {
            element.classList.remove("active");
        });

        valorcorrente.classList.add("active");

    });

});