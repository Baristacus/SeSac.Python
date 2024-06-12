users = [
    {"name": "Alice", "age": "37", "location": "Seoul", "car": "BMW"},
    {"name": "Alice", "age": "25", "location": "Seoul", "car": "BMW"},
    {"name": "Alice.Jr", "age": "2", "location": "Busan", "car": ""},
    {"name": "Bob", "age": "37", "location": "Busan", "car": "Mercedes"},
    {"name": "Bob", "age": "27", "location": "Busan", "car": "Mercedes"},
    {"name": "Bob.Jr", "age": "5", "location": "Busan", "car": ""},
    {"name": "Bob.Jr", "age": "7", "location": "Busan", "car": ""},
    {"name": "Charlie", "age": "35", "location": "Daegu", "car": "Audi"},
    {"name": "Charlie", "age": "40", "location": "Daegu", "car": "Audi"},
    {"name": "Charlie.Jr", "age": "10", "location": "Daegu", "car": ""},
    {"name": "Charlie.Jr", "age": "4", "location": "Daegu", "car": ""},
]

filter_user = [user for user in users if user.get("name") == "Bob"]

filter_user_age = [
    {key: value for key, value in user.items() if key == "age"}
    for user in users
    if user.get("name") == "Bob"
]


print(filter_user)

print(filter_user_age)
