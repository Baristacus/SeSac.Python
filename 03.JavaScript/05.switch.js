function selectInfo() {
    switch (document.querySelector("select").value) {
        case "-1":
            document.getElementById("text").innerHTML = "Select Fruit: "
            break
        case "apple":
            document.getElementById("text").innerHTML = "Apple<br>"
            break
        case "banana":
            document.getElementById("text").append("Banana ")
            break
        case "orange":
            document.getElementById("text").append("Orange ")
            break
    }
}