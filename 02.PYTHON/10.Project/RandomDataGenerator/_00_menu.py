import pretty_errors

from _01_user import user_generator
from _02_store import store_generator
from _03_item import item_generator
from _04_order import order_generator
from _05_orderitem import orderitem_generator


def generator_menu(num):
    if num == 9:
        exit(1)

    if num == 0:
        print(
            "\n\n\n",
            ":: Random Data Generator ::::::::::::::::::::::::\n",
            "=================================================\n",
            "  번호를 선택 후 엔터(↵)를 입력해주세요.\n",
            "-------------------------------------------------\n",
            "  1. 사용자 생성기\n",
            "  2. 상점 정보 생성기\n",
            "  3. 카페 메뉴 생성기\n",
            "  4. 주문 내역 생성기\n",
            "  5. 상세 주문 내역 생성기\n",
            "\n",
            "-------------------------------------------------\n",
            "  9: 종료\n",
            "=================================================\n",
        )
        num = int(input("번호입력: "))
        generator_menu(num)

    if num == 1:
        print(
            "\n\n\n",
            ":: Random Data Generator ::::::::::::::::::::::::\n",
            "=================================================\n",
            "  → 사용자 생성기\n",
            "-------------------------------------------------\n",
        )
        user_generator()
        print("=================================================")
        print(
            "-------------------------------------------------\n",
            "  0: 메인메뉴 | 9: 종료\n",
            "=================================================\n",
        )
        num = int(input("번호입력: "))
        generator_menu(num)


# store_generator()
# item_generator()
# order_generator()
# orderitem_generator()

generator_menu(0)
