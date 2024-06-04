inputBox = document.getElementById("inputBox");
operaterBtn = document.getElementsByClassName("operatorBtn");
numberBtn = document.getElementsByClassName("numberBtn");

function operator(symbol) {
    const operatorList = ["+", "-", "*", "/", "**"]
    lastInput = inputBox.value.slice(-1);

    checkInput = inputBox.value.includes(operatorList);

    if (!checkInput) {
        inputBox.value += symbol
    }
}

function calculate() {
    try {
        inputBox.value = new Function("return " + inputBox.value)()
    }
    catch {
        inputBox.value = "잘못된 값입니다."
    }
}

function enterKey(event) {
    if (event.keyCode == 13) {
        calculate();
    }
}