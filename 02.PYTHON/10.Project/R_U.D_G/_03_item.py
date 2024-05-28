"""메뉴 생성기

- [v] item_uuid : UUID 랜덤 생성
- [v] item_name : 메뉴 카테고리 랜덤 생성 (Coffee, Non-Coffee, Bakery)
- [v] item_type : 메뉴 랜덤 생성
- [v] item_price : 메뉴 랜덤 생성에서 같이 가져옴

[v] 결과 : item.csv
Id,Name,Type,UnitPrice
"""

import os
import csv
import uuid
import random
from itertools import chain

current_file_path = os.path.abspath(__file__)
current_folder = os.path.dirname(current_file_path)

file_path = os.path.join(current_folder, "item.csv")


def create_save_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="UTF-8", newline="") as file:
            headers = ["Id", "Name", "Type", "UnitPrice"]
            file_save = csv.DictWriter(file, fieldnames=headers)
            file_save.writeheader()


def item_type_price():
    id = str(uuid.uuid4())
    category = random.choice(["Coffee", "Non-Coffee", "Bakery"])

    # Coffee
    if category == "Coffee":
        with open(
            "random_data/item_coffee_price_data.csv", "r", encoding="UTF-8"
        ) as file:
            file_read = csv.DictReader(file)
            coffee_list = [x for x in file_read]
            coffee = random.choice(coffee_list)
            return id, category, coffee["Menu"], coffee["Price"]

    # Non-Coffee
    if category == "Non-Coffee":
        with open(
            "random_data/item_noncoffee_price_data.csv", "r", encoding="UTF-8"
        ) as file:
            file_read = csv.DictReader(file)
            noncoffee_list = [x for x in file_read]
            noncoffee = random.choice(noncoffee_list)
            return id, category, noncoffee["Menu"], noncoffee["Price"]

    # Bakery
    if category == "Bakery":
        with open(
            "random_data/item_bakery_price_data.csv", "r", encoding="UTF-8"
        ) as file:
            file_read = csv.DictReader(file)
            bakery_list = [x for x in file_read]
            bakery = random.choice(bakery_list)
            return id, category, bakery["Menu"], bakery["Price"]


def item_generator():
    create_save_file(file_path)
    create_number = int(input("생성하려는 데이터의 갯수를 입력하세요: "))
    item_list = []
    for _ in range(create_number):
        item_list.append(item_type_price())

    with open(file_path, "a", encoding="UTF-8", newline="") as file:
        item_save = csv.writer(file)
        item_save.writerows(item_list)

    return print(f"{create_number}개의 데이터가 'item.csv'파일에 저장되었습니다.")


# TEST
# print(item_type_price())
item_generator()
