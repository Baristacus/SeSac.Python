"""유저 생성기

- [v] user_uuid : UUID 랜덤 생성 - xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
- [v] last_name : 성 랜덤 생성 - 홍
- [v] first_name : 이름 랜덤 생성 - 길동
- [v] gender : 성별 랜덤 생성 - 남, 여
- [v] birthday : 생일 랜럼 생성 - yyyy-mm-dd
- [v] age : 태어난 년도 기준으로 생성 - 2024-birthday(yyyy)
- [v] address1 : 시/도
- [v] address2 : 구/군
- [v] address3 : 상세주소

[v] 결과: user.csv
Id, Name, Gender, Birthday, Age, Address
"""

import os
import csv
import uuid
import random
from itertools import chain

current_file_path = os.path.abspath(__file__)
current_folder = os.path.dirname(current_file_path)

file_path = os.path.join(current_folder, "user.csv")


def create_save_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="UTF-8", newline="") as file:
            headers = ["Id", "Name", "Gender", "Birthday", "Age", "Address"]
            file_save = csv.DictWriter(file, fieldnames=headers)
            file_save.writeheader()


def user_uuid():
    return str(uuid.uuid4())


def user_name():

    # last_name : 성
    with open("random_data/last_name_data.csv", "r", encoding="UTF-8") as file:
        file_read = csv.reader(file)
        origin_names_list = [x for x in file_read]
        chain_names_list = list(chain(*origin_names_list))
        names_list = [x.strip() for x in chain_names_list]
        last_name = random.choice(names_list)

    # first_name : 이름
    with open("random_data/first_name_data.csv", "r", encoding="UTF-8") as file:
        file_read = csv.reader(file)
        origin_names_list = [x for x in file_read]
        chain_names_list = list(chain(*origin_names_list))
        names_list = [x.strip() for x in chain_names_list]
        first_name = random.choice(names_list)

    return last_name + first_name


def user_gender():
    return random.choice(["남", "여"])


def user_birthday_age():
    this_year = 2024
    year_start = 1980
    yesr_end = 2010

    year = random.randint(year_start, yesr_end)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    age = this_year - year

    return f"{year}-{month:02d}-{day:02d}, {age}"


def user_address():

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


def user_generator():
    create_save_file(file_path)
    create_number = int(input("  >>> 생성하려는 사용자 데이터의 갯수를 입력하세요: "))
    user_list = []
    for _ in range(create_number):
        birthday_age = user_birthday_age()
        birthday = birthday_age[:10]
        age = birthday_age[12:]

        user_list.append(
            {
                "Id": user_uuid(),
                "Name": user_name(),
                "Gender": user_gender(),
                "Birthday": birthday,
                "Age": int(age),
                "Address": user_address(),
            }
        )
    with open(file_path, "a", encoding="UTF-8", newline="") as file:
        headers = ["Id", "Name", "Gender", "Birthday", "Age", "Address"]
        user_save = csv.DictWriter(file, fieldnames=headers)
        user_save.writerows(user_list)

    return print(f"  {create_number}개의 데이터가 'user.csv'파일에 저장되었습니다.")
