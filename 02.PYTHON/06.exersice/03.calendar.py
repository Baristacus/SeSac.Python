# import calendar

# print(calendar.month(2024, 5))

# year = int(input("연도를 입력하세요: "))
# month = int(input("월를 입력하세요: "))

# print(calendar.month(year, month))


# -------------------------------------------
""" 달력 함수를 사용하지 않고 달력 구현하기
1.
"""


def my_cal(year, month):
    for i in range(1, 30):
        print(f"{i}", end="")
        if i % 7 == 0:
            print("")


my_cal(2025, 1)
