function changeCellColor() {
    let cells = document.getElementsByTagName("td")

    for (cells of cells) {
        cells.style.backgroundColor = "red"
    }
}

function changeRowColor() {
    let cells = document.getElementsByTagName("td")

    for (let i = 1; i < cells.length; i += 2) {
        cells[i].style.backgroundColor = "orange"
    }
}
function changeRowColor2() {
    let cells = document.getElementsByTagName("td")

    for (let i = 0; i < cells.length; i += 2) {
        cells[i].style.backgroundColor = "orange"
    }
}

function resetCellColor() {
    let cells = document.getElementsByTagName("td")

    for (cells of cells) {
        cells.style.backgroundColor = "white"
    }
}