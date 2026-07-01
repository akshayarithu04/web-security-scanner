document.querySelector("form").addEventListener("submit", function () {

    const button = document.querySelector("button");

    button.disabled = true;

    button.innerHTML = "Scanning...";
});