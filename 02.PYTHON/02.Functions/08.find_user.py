users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Alice", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
]


# print(users[0]["name"])


# 입력받은 사용자 정보 출력
def find_user(name):
    found_user = []
    for user in users:
        if (
            user["name"].lower() == name.lower()
        ):  # if user.get("name") == name: // get함수로도 불러올 수 있음
            # print(user)
            found_user.append(user)
    return found_user


found = find_user("Alice")
print(found)
