# 이진 탐색


def binary_search(list, target):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2  # 소수점을 버림
        if list[mid] == target:
            return mid  # 정답을 찾음
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


my_list = [1, 8, 7, 9, 6, 3, 4, 5, 2]

target = 6

result = binary_search(my_list, target)
if result != -1:
    print("타겟 인덱스: ", result)
else:
    print("타켓없음")
