const hamburger = document.querySelector("#hamburger");
const addFilesBtn = document.querySelector("#addFiles");
addFilesBtn?.addEventListener("click", addFileInputElement);
const templateElement = document.getElementsByTagName("template")[0];
const inputElements = Array.from(document.querySelectorAll(".form-file-input"));
inputElements.forEach(inputElement => inputElement.addEventListener("change", showName));
const menu = document.querySelector("#menu");
hamburger?.addEventListener("click", function () {
    if (menu.classList.contains("hidden")) {
        menu.classList.remove("hidden")
    } else {
        menu.classList.add("hidden")
    }
});

function addFileInputElement(e) {
    e.preventDefault();
    const templateClone = templateElement.content.cloneNode(true);
    inputElement = templateClone.querySelector(".form-file-input");
    inputElement.addEventListener("change", showName);
    const fieldWrapper = document.querySelector("#field-wrapper");//get how many inputs we have currently in dom
    count = fieldWrapper.children.length + 1;
    inputElement.name = `documents-${count}-file`;
    inputElement.id = `customFile${count}`;
    templateClone.querySelector("label").htmlFor = inputElement.id;
    fieldWrapper.appendChild(templateClone);
}

function showName(e) {
    const label = this.nextElementSibling;
    label.querySelector("#label").textContent = this.files[0].name;
}