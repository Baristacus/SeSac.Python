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

        // querySelector
        // https://developer.mozilla.org/ko/docs/Web/API/Document/querySelector
        let checkbox = newListItem.querySelector('input[type="checkbox"]');

        // 체크박스 체크
        // parentNode, childNode 찾아볼 것, 왜 childNode는 작동을 안할까?
        // https://ant-hill.tistory.com/33
        // 노드와 엘리먼트의 차이는?
        // https://velog.io/@yejineee/DOM%EC%9D%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-DOM-Node%EC%99%80-Element%EC%9D%98-%EC%B0%A8%EC%9D%B4
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