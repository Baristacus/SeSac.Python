let saveBtn = document.getElementById("saveBtn")
let todoList = document.getElementById("todoList")
let todoListUL = document.getElementById("todoUl")
let todoText = document.getElementById("todoText")

saveBtn.addEventListener("click", function () {

    if (todoText.value == "") {
        alert("비워둘수 없음")
    } else {
        let newListItem = document.createElement("li")
        newListItem.innerHTML = "<input type='checkbox' class='form-check-input me-2'>" + todoText.value + "<button class='deleteBtn btn btn-sm'>❌</button>"
        todoListUL.appendChild(newListItem);

        let checkbox = newListItem.querySelector('input[type="checkbox"]');

        // 체크박스 체크
        checkbox.addEventListener("change", function () {
            if (this.checked) {
                this.parentNode.style.textDecoration = "line-through";
            } else {
                this.parentNode.style.textDecoration = "none";
            }
        });

        // 리스트 삭제
        let deleteBtn = newListItem.querySelector('.deleteBtn');
        deleteBtn.addEventListener("click", function () {
            this.parentNode.remove();
        })
    }


    todoText.value = ""
    todoText.focus()

})