"""주문 생성기

- [ ] order_uuid : UUID 랜덤 생성
- [ ] order_date : 2023-03-26 13:37:31 - 2023년 5월 ~ 2024년 5월
- [ ] storeid : store.csv에서 랜덤 가져오기
- [ ] userid : user.csv에서 랜덤 가져오기

[ ] 결과 : order.csv
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


order_year = random.randint(2024, 2025)
order_month = random.randint(1, 12)
order_day = random.randint(1, 28)
order_hour = random.randint(0, 23)
order_minute = random.randint(0, 59)
order_second = random.randint(0, 59)


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
        order_id = str(uuid.uuid4())
        order_date = f"{order_year}-{order_month:02d}-{order_day:02d} {order_hour:02d}:{order_minute:02d}:{order_second:02d}"
        store_id = store_data()
        user_id = user_data()

        order_list.append(
            {
                "Id": order_id,
                "OrderAt": order_date,
                "StoreId": store_id,
                "UserId": user_id,
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
