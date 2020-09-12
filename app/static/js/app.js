const hamburger = document.querySelector("#hamburger");
const menu = document.querySelector("#menu");
hamburger?.addEventListener("click", function () {
    if (menu.classList.contains("hidden")) {
        menu.classList.remove("hidden")
    } else {
        menu.classList.add("hidden")
    }
});