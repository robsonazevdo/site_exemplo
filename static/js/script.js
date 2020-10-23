var btnentrar = document.querySelector("#entrar");
var btnsair = document.querySelector("#sair");
var body = document.querySelector("body");



btnentrar.addEventListener("click", function() {
    body.className = "entrar-js";
});


btnsair.addEventListener("click", function() {
    body.className = "sair-js";
});