# zip은 가장 짧은 데이터 기준으로 묶임.


list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

ziped = zip(list1, list2)

list3 = [True, False, True]

ziped = zip(list1, list2, list3)

print(list(ziped))


# ------------------------------------------


key = ["name", "age", "location", "car"]
value = ["Alice", 25, "Seoul", "BMW"]

my_dict = dict(zip(key, value))

print(my_dict)


values_list = [
    ["Alice", 25, "Seoul", "BMW"],
    ["Bob", 30, "Busan", "Audi"],
]

dictlists = [dict(zip(key, value)) for value in values_list]

print(dictlists)
