"""매장 생성기

- [v] store_uuid : UUID 랜덤 생성
- [v] store_name : 매장명 랜덤 생성
- [v] sotre_type : 서초OO호점
- [v] address1 : 시/도
- [v] address2 : 구/군
- [v] address2 : 상세주소

[v] 결과 : store.csv
Id, Name, Type, Address
"""

import os
import csv
import uuid
import random
from itertools import chain

current_file_path = os.path.abspath(__file__)
current_folder = os.path.dirname(current_file_path)

file_path = os.path.join(current_folder, "store.csv")


def create_save_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="UTF-8", newline="") as file:
            headers = ["Id", "Name", "Type", "Address"]
            file_save = csv.DictWriter(file, fieldnames=headers)
            file_save.writeheader()


def store_uuid():
    return str(uuid.uuid4())


def store_name():
    with open("random_data/store_name_data.csv", "r", encoding="UTF-8") as file:
        file_read = csv.reader(file)
        origin_store_list = [x for x in file_read]
        chain_store_list = list(chain(*origin_store_list))
        store_list = [x.strip() for x in chain_store_list]
        store = random.choice(store_list)
    return store


def store_type():
    # 지역명 생성
    with open("random_data/address2_data.csv", "r", encoding="UTF-8") as file:
        file_read = csv.reader(file)
        origin_region_list = [x for x in file_read]
        chain_region_list = list(chain(*origin_region_list))
        region_list = [x.strip() for x in chain_region_list]
        store_region = random.choice(region_list)[:-1]

    # O호점 생성
    number = random.randint(1, 5)
    store_number = f" {number}호점"
    return store_region + store_number


def store_address():

    # address1 : 시 / 도
    with open("random_data/address1_data.csv", "r", encoding="UTF-8") as file:
        file_read = csv.reader(file)
        origin_addr1_list = [x for x in file_read]
        chain_addr1_list = list(chain(*origin_addr1_list))
        addr1_list = [x.strip() for x in chain_addr1_list]
        address1 = random.choice(addr1_list)

    # address2 : 구 / 군
    with open("random_data/address2_data.csv", "r", encoding="UTF-8") as file:
        file_read = csv.reader(file)
        origin_addr2_list = [x for x in file_read]
        chain_addr2_list = list(chain(*origin_addr2_list))
        addr2_list = [x.strip() for x in chain_addr2_list]
        address2 = random.choice(addr2_list)

    # address3 : 000길/로 000
    addr3_1 = random.randint(1, 100)
    addr3_2 = random.choice(["길", "로"])
    addr3_3 = random.randint(1, 200)

    return f"{address1} {address2} {addr3_1}{addr3_2} {addr3_3}"


def store_generator():
    create_save_file(file_path)
    create_number = int(input("생성하려는 데이터의 갯수를 입력하세요: "))
    store_list = []
    for _ in range(create_number):
        store_list.append(
            {
                "Id": store_uuid(),
                "Name": store_name(),
                "Type": store_type(),
                "Address": store_address(),
            }
        )

    with open(file_path, "a", encoding="UTF-8", newline="") as file:
        headers = ["Id", "Name", "Type", "Address"]
        store_save = csv.DictWriter(file, fieldnames=headers)
        store_save.writerows(store_list)

    return print(f"{create_number}개의 데이터가 'store.csv'파일에 저장되었습니다.")


# TEST
# print(store_uuid())
# print(store_name())
# print(store_type())
# print(store_address())
# print(store_generator())

store_generator()
