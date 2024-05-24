"""하이스코어
점수와 이름을 입력받고, 다양한 모드(score, high, history)에 따라서
각각, "스코어입력", "하이스코어출력", "전체히스토리보기" 기능 구현

----------------------------------------------------------

1. 실행 시 메뉴를 보여주고, 번호를 선택한다.
2. 
2. 저장을 한다.(txt? csv? 어디다가?)
    - 기존에 파일이 없다면 만든다.
    - 파일이 있다면?
3. 
"""

import csv

file_path = "02.highscore.csv"


def score_input():
    auto_num = 1
    input_name = input("이름을 입력하세요: ")
    input_score = input("스코어를 입력하세요: ")

    with open(file_path, "a", encoding="UTF-8", newline="") as file:
        headers = ["No", "Name", "Score"]
        score_save = csv.DictWriter(file, fieldnames=headers)
        score_save.writeheader()
        score_save.writerow([auto_num, input_name, input_score])
    return print("저장완료")


def high_output():
    return


def score_history():
    return


def menu(num):
    if num == 0:
        print(
            "\n\n\n\n\n"
            "*=================================================*\n"
            "  번호를 선택 후 엔터(↵)를 입력해주세요.\n"
            "*-------------------------------------------------*\n"
            "  1. 스코어 입력\n"
            "  2. 하이스코어 출력\n"
            "  3. 전체히스토리\n"
            "\n"
            "*-------------------------------------------------*\n"
            "  0: 메인메뉴 | 9: 종료\n"
            "*=================================================*"
        )
        num = int(input("번호입력: "))
        menu(num)
    if num == 1:
        print(
            "\n\n\n\n\n"
            "*=================================================*\n"
            "  번호를 선택 후 엔터(↵)를 입력해주세요.\n"
            "*-------------------------------------------------*\n"
            "  스코어 입력\n"
        )
        # 여기에... 스코어 입력 함수 호출
        score_input()
        print(
            "*-------------------------------------------------*\n"
            "  0: 메인메뉴 | 9: 종료\n"
            "*=================================================*"
        )
        num = int(input("번호입력: "))
        menu(num)
    if num == 9:
        exit(1)
    return num


menu(0)


# if menu_num == "1":
#     input_name = input("이름을 입력하세요: ")
#     input_score = input("스코어를 입력하세요: ")
