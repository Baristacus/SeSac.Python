"""상세주문내역 생성기

- [v] orderitem_uuid : UUID 랜덤 생성
- [v] orderid : order.csv에서 랜덤 가져오기
- [v] itemid : item.csv에서 랜덤 가져오기

[v] 결과 : orderitem.csv
Id,OrderId,ItemId
"""

import os
import csv
import uuid
import random

current_file_path = os.path.abspath(__file__)
current_folder = os.path.dirname(current_file_path)

file_path = os.path.join(current_folder, "orderitem.csv")


def create_save_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="UTF-8", newline="") as file:
            headers = ["Id", "OrderId", "ItemId"]
            file_save = csv.DictWriter(file, fieldnames=headers)
            file_save.writeheader()


def order_data():
    order_data_list = []
    with open("order.csv", "r", encoding="UTF-8") as file:
        order_read = csv.DictReader(file)
        for order_data in order_read:
            order_data_list.append(order_data)
    return random.choice(order_data_list)["Id"]


def item_data():
    item_data_list = []
    with open("item.csv", "r", encoding="UTF-8") as file:
        item_read = csv.DictReader(file)
        for item_data in item_read:
            item_data_list.append(item_data)
    return random.choice(item_data_list)["Id"]


def orderitem_generator():
    create_save_file(file_path)
    create_number = int(
        input("  >>> 생성하려는 상세 주문내역 데이터의 갯수를 입력하세요: ")
    )

    orderitem_list = []
    for _ in range(create_number):
        orderitem_list.append(
            {
                "Id": str(uuid.uuid4()),
                "OrderId": order_data(),
                "ItemId": item_data(),
            }
        )

    with open(file_path, "a", encoding="UTF-8", newline="") as file:
        headers = ["Id", "OrderId", "ItemId"]
        orderitem_save = csv.DictWriter(file, fieldnames=headers)
        orderitem_save.writerows(orderitem_list)
    return print(
        f"  {create_number}개의 데이터가 'orderitem.csv'파일에 저장되었습니다."
    )
