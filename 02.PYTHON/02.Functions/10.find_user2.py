from unittest import result


users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Alice.Jr", "age": 2, "location": "Busan", "car": ""},
    {"name": "Bob", "age": 37, "location": "Busan", "car": "Mercedes"},
    {"name": "Bob.Jr", "age": 5, "location": "Busan", "car": ""},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Charlie.Jr", "age": 10, "location": "Daegu", "car": ""},
]


# print(users[0]["name"])


# 입력받은 사용자 정보 출력
# def find_user(name):
#     found_user = []
#     for user in users:
#         if (
#             user["name"].lower() == name.lower()
#         ):  # if user.get("name") == name: // get함수로도 불러올 수 있음
#             # print(user)
#             found_user.append(user)
#     return found_user


# found = find_user("Alice")
# print(found)

# ----------------------------------------------------------

# 이름 + 나이로 사용자 정보 출력
# def find_user2(name, age):
#     found_user = []
#     for user in users:
#         # print(user)
#         if user["name"].lower() == name.lower():  # and user["age"] == age:
#             found_user.append(user)
#             if user["age"] == age or user["name"].lower() == name.lower():
#                 found_user.append(user)
#     return found_user


# found2 = find_user2("Bob", 80)
# print(found2)


# Sample --------------------------------------------------
def display_user(users):
    print("---찾은 사용자 목록---")
    if len(users) == 0:
        print("결과 없음")
    else:
        for u in users:
            print(f"이름: {u['name']}, 나이: {u['age']}")


def find_user(name=None, age=None):
    found_user = []
    if name is None and age is None:
        return users

    for user in users:
        if name is not None and age is not None:
            if user["name"].lower() == name.lower() and user["age"] == age:
                found_user.append(user)
        elif name is not None:
            if user["name"].lower() == name.lower():
                found_user.append(user)
        elif age is not None:
            if user["age"] == age:
                found_user.append(user)
    return found_user


# found = find_user("Bob")
# print(display_user(found))


# ----------------------------------------------------------


# def find_user2(search):
#     result = []

#     for user in users:
#         if (
#             (search.get("name") is None or user.get("name") == search.get("name"))
#             and (search.get("age") is None or user.get("age") == search.get("age"))
#             and (
#                 search.get("location") is None
#                 or user.get("location") == search.get("location")
#             )
#             and (search.get("car") is None or user.get("car") == search.get("car"))
#         ):
#             result.append(user)

#     return result


# search1 = {"name": "Bob"}
# search2 = {"name": "Alice", "age": 20}
# search3 = {"location": "Jeju", "car": "BMW"}

# print(find_user2(search1))


# ----------------------------------------------------------


def find_user2(search):
    result = []

    for user in users:
        if (
            (search.get("name") is None or user.get("name") == search.get("name"))
            and (search.get("age") is None or user.get("age") == search.get("age"))
            and (
                search.get("location") is None
                or user.get("location") == search.get("location")
            )
            and (search.get("car") is None or user.get("car") == search.get("car"))
            and (
                search.get("min_age") is None
                or user.get("age") >= search.get("min_age")
            )
        ):
            result.append(user)

    return result


search1 = {"name": "Bob"}
search2 = {"name": "Alice", "age": 20}
search3 = {"location": "Jeju", "car": "BMW"}
search4 = {"min_age": 30}

print(find_user2(search4))

# ----------------------------------------------------------


def find_user3(search):
    result = []

    for user in users:
        if match(user, search):
            result.append(user)


def match(user, criteria):
    for key, value in criteria.items():
        if key == "age":
            if user.get("age") != value:
                return False
        if key == "name":
            if user.get("name") != value:
                return False
        if key == "location":
            if user.get("location") != value:
                return False
        if key == "key":
            if user.get("car") != value:
                return False
    return True


print(find_user3(search1))
