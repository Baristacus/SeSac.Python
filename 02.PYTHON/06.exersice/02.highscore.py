"""하이스코어
점수와 이름을 입력받고, 다양한 모드(score, high, history)에 따라서
각각, "스코어입력", "하이스코어출력", "전체히스토리보기" 기능 구현
----------------------------------------------------------
1. csv파일은 현재 경로에 저장
    - 파일이 없는경우 실행 시 새로 만듦
2. 메인메뉴 보여주고, 번호 선택하기
3. 해당 메뉴에 따라 화면 구성하기
    - 스코어입력 : 이름과 스코어를 입력받아 저장(순번은 자동증가)
    - 하이스코어출력 : 기록된 목록에서 TOP3 출력
    - 전체히스토리 : 저장된 모든 기록 출력
"""

import csv
import os

current_file_path = os.path.abspath(__file__)
current_folder = os.path.dirname(current_file_path)

file_path = os.path.join(current_folder, "02.highscore.csv")
data_list = []


def create_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="UTF-8", newline="") as file:
            headers = ["No", "Name", "Score"]
            score_save = csv.DictWriter(file, fieldnames=headers)
            score_save.writeheader()


def score_input():
    with open(file_path, "r", encoding="utf-8") as f:
        all_list = csv.reader(f)
        for row in all_list:
            data_list.append(row)

    auto_num = (len(data_list) - 1) + 1

    while True:
        input_name = input("이름을 입력하세요: ")
        if input_name.strip() and not input_name.isdigit():
            break
        else:
            print("올바른 이름을 입력해주세요.")

    while True:
        input_score = input("스코어를 입력하세요: ")
        if input_score.isdigit():
            break
        else:
            print("스코어는 숫자로 입력해주세요.")

    input_data = {"No": auto_num, "Name": input_name, "Score": input_score}

    with open(file_path, "a", encoding="UTF-8", newline="") as file:
        headers = ["No", "Name", "Score"]
        score_save = csv.DictWriter(file, fieldnames=headers)
        if len(data_list) == 0:
            score_save.writeheader()
        score_save.writerow(input_data)

    data_list.clear()
    return print("  [저장완료]")


def high_score():
    with open(file_path, "r", encoding="utf-8") as file:
        all_list = csv.DictReader(file)
        for row in all_list:
            data_list.append(row)

    sorted_list = sorted(data_list, key=lambda x: int(x["Score"]), reverse=True)

    rank_num = 0

    for aaa in sorted_list[:3]:
        rank_num += 1
        print(f'  {rank_num}. {aaa["Name"]} - {aaa["Score"]}')

    data_list.clear()
    return print("  [불러오기 완료]")


def score_history():
    with open(file_path, "r", encoding="UTF-8") as file:
        score_list = csv.DictReader(file)
        if not score_list:
            print("  [데이터가 없습니다.]")
        else:
            for data in score_list:
                print(f'  {data["No"]}. {data["Name"]} - {data["Score"]}')

    return print("  [불러오기 완료]")


def menu(num):
    if num == 0:
        print(
            "\n\n\n\n\n"
            "=================================================\n"
            "  번호를 선택 후 엔터(↵)를 입력해주세요.\n"
            "-------------------------------------------------\n"
            "  1. 스코어 입력\n"
            "  2. 랭킹 TOP3\n"
            "  3. 전체목록\n"
            "-------------------------------------------------\n"
            "  9: 종료\n"
            "================================================="
        )
        num = int(input("번호입력: "))
        menu(num)
    if num == 1:
        print(
            "\n\n\n\n\n"
            "=================================================\n"
            "  스코어 입력\n"
            "-------------------------------------------------"
        )
        score_input()
        print(
            "-------------------------------------------------\n"
            "  0: 메인메뉴 | 9: 종료\n"
            "================================================="
        )
        num = int(input("번호입력: "))
        menu(num)
    if num == 2:
        print(
            "\n\n\n\n\n"
            "=================================================\n"
            "  랭킹 TOP3\n"
            "-------------------------------------------------"
        )
        high_score()
        print(
            "-------------------------------------------------\n"
            "  0: 메인메뉴 | 9: 종료\n"
            "================================================="
        )
        num = int(input("번호입력: "))
        menu(num)
    if num == 3:
        print(
            "\n\n\n\n\n"
            "=================================================\n"
            "  전체목록\n"
            "-------------------------------------------------"
        )
        score_history()
        print(
            "-------------------------------------------------\n"
            "  0: 메인메뉴 | 9: 종료\n"
            "================================================="
        )
        num = int(input("번호입력: "))
        menu(num)
    if num == 9:
        exit(1)

    if not num is 0 or 1 or 2 or 3 or 9:
        print("올바른번호를 입력해주세요.")
        menu(0)


create_file(file_path)
menu(0)
