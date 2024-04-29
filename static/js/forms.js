let form = document.getElementById('#form')
let formChildren=form.children
for (var i = 0; i < formChildren.length; i++) {
    console.log(formChildren[i]);
    formChildren[i].classList.add("mb-4","justify-content-center","align-items-center")
}

let inputs=document.querySelectorAll('input')
for (var i = 0; i < inputs.length; i++) {
    console.log(inputs[i]);
    inputs[i].classList.add("form-control","border-1")
}

let labels=document.querySelectorAll('label')
for (var i = 0; i < labels.length; i++) {
    console.log(labels[i]);
    labels[i].classList.add("fw-bold","mb-2")
}