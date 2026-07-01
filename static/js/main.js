document.querySelector("form").addEventListener("submit", function () {

    const button = document.querySelector("button");

    button.disabled = true;

    button.innerHTML = "Scanning...";
});
document.addEventListener("DOMContentLoaded", function(){

    const form = document.querySelector("form");

    if(form){

        form.addEventListener("submit", function(){

            const button = document.querySelector("button");

            button.disabled = true;

            button.innerHTML = "Scanning... 🔍";

        });

    }

});