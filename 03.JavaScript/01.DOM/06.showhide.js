function boxHidden() {
    document.getElementById("box").style.display = "none";
}

function boxShow() {
    document.getElementById("box").style.display = "block";
}

function boxToggle() {
    if (document.getElementById("box").style.display == "none") {
        document.getElementById("box").style.display = "block";
    } else {
        document.getElementById("box").style.display = "none";
    }
}