# 가장 큰 수 구하기
numbers = [3, 5, 4, 6, 2, 8, 9, 10, -53, 22, 1]


def find_max(numbers):
    max_num = numbers[0]

    for i in numbers[1:]:
        if i > max_num:
            max_num = i
    print(max_num)


find_max(numbers)
