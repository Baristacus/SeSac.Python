#

numbers = [1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 2, 2, 3, 4, 5, 3, 2, 1]


def remove_duplicate1(lists):
    unique_list = []
    for o_list in lists:
        check = False
        for u_list in unique_list:
            if u_list == o_list:
                check = True
        if not check is False:
            unique_list.append(u_list)
        # print(unique_list)

    return unique_list


def remove_duplicate2(numbers):
    return list(set(numbers))


unique_numbers1 = remove_duplicate1(numbers)
unique_numbers2 = remove_duplicate2(numbers)

print(f"원본리스트: {numbers}")
print(f"유니크리스트1: {unique_numbers1}")
print(f"유니크리스트2: {unique_numbers2}")
