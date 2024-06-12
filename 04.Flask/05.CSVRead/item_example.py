my_dict = {"name": "Alice", "age": "37", "location": "Seoul", "car": "BMW"}


items = my_dict.items()

items_list = list(items)

for item in items_list:
    print(item)

for k, v in sorted(my_dict.items()):
    print(f"Key: {k}, Value: {v}")


update_dict = {"name": "Bob", "age": "25", "location": "Busan", "car": "Mercedes"}


new_dict = my_dict | update_dict
print(new_dict)
