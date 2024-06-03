inputBox = document.getElementById("inputBox");
function calculate() {
    inputBox.value = new Function("return " + inputBox.value)()
}

function enterKey(event) {
    if (event.keyCode == 13) {
        calculate();
    }
}