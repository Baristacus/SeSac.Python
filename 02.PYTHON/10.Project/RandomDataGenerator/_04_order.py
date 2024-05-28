"""주문 생성기

- [v] order_uuid : UUID 랜덤 생성
- [v] order_date : YYYY-MM-DD HH:MM:SS 랜덤 생성 - 2023년 ~ 2024년
- [v] storeid : store.csv에서 랜덤 가져오기
- [v] userid : user.csv에서 랜덤 가져오기

[v] 결과 : order.csv
Id,OrderAt,StoreId,UserId
"""

import os
import csv
import uuid
import random

current_file_path = os.path.abspath(__file__)
current_folder = os.path.dirname(current_file_path)

file_path = os.path.join(current_folder, "order.csv")


def create_save_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="UTF-8", newline="") as file:
            headers = ["Id", "OrderAt", "StoreId", "UserId"]
            file_save = csv.DictWriter(file, fieldnames=headers)
            file_save.writeheader()


def order_date():
    year = random.randint(2023, 2024)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"


def store_data():
    store_data_list = []
    with open("store.csv", "r", encoding="UTF-8") as file:
        store_read = csv.DictReader(file)
        for store_data in store_read:
            store_data_list.append(store_data)
    return random.choice(store_data_list)["Id"]


def user_data():
    user_data_list = []
    with open("user.csv", "r", encoding="UTF-8") as file:
        user_read = csv.DictReader(file)
        for user_data in user_read:
            user_data_list.append(user_data)
    return random.choice(user_data_list)["Id"]


def order_generator():
    create_save_file(file_path)
    create_number = int(input("생성하려는 데이터의 갯수를 입력하세요: "))

    order_list = []
    for _ in range(create_number):
        order_list.append(
            {
                "Id": str(uuid.uuid4()),
                "OrderAt": order_date(),
                "StoreId": store_data(),
                "UserId": user_data(),
            }
        )

    with open(file_path, "a", encoding="UTF-8", newline="") as file:
        headers = ["Id", "OrderAt", "StoreId", "UserId"]
        order_save = csv.DictWriter(file, fieldnames=headers)
        order_save.writerows(order_list)
    return print(f"{create_number}개의 데이터가 'order.csv'파일에 저장되었습니다.")


# TEST
# print(order_date)
# print(store_data())
# print(user_data())

order_generator()
