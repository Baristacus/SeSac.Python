import time
import random

# 선형 탐색


def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i

    return -1


def random_number_list(count):
    number = [random.randint(1, count) for _ in range(count)]
    return number


my_list = [2, 3, 5, 8, 9, 4, 6, 1]
my_list2 = random_number_list(10000000)
target = 6

start_time = time.time()
result = linear_search(my_list2, target)
end_time = time.time()

diff_time = end_time - start_time
print(f"찾는데 걸린 시간은: {diff_time}초")

if result != -1:
    print("타겟을 찾음: ", result)
else:
    print("타켓이 없음")
