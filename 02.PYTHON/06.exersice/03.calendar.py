# import calendar

# print(calendar.month(2024, 5))

# year = int(input("연도를 입력하세요: "))
# month = int(input("월를 입력하세요: "))

# print(calendar.month(year, month))


# -------------------------------------------
""" 달력 함수를 사용하지 않고 달력 구현하기
1. 월의 마지막 날짜 계산
    - 2월 : 28일, 29일
    - 1월, 3월, 5월, 7월, 8월, 10월, 12월 : 31일
    - 4월, 6월, 9월, 11월 : 30일
2. 윤년, 평년 계산
    - 4로 나누어 떨어지면서 400으로 나누어 떨어지는 해는 윤년
    - 4로 나누어 떨어지지만 100으로 나누어 떨어지는 해는 윤년이 아님
3. 시작요일 계산
    - Zeller 공식(1월과 2월은 연도 -1 월 + 1)
        - h = (1 + (26 * (month + 1)) // 10 + year + year // 4 - year // 100 + year // 400) % 7
        - 0: 토요일, 1: 일요일, 2: 월요일, 3: 화요일, 4: 수요일, 5: 목요일, 6: 금요일
4. 년도와 월을 입력 받아 출력
"""


def last_day(year, month):
    if month == 2:
        if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
            return 29
        else:
            return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30


def day_of_week(year, month):
    if month == 1 or month == 2:
        year -= 1
        month += 12
    week = (
        1 + (26 * (month + 1)) // 10 + year + year // 4 - year // 100 + year // 400
    ) % 7
    return week


def line_print(count, line, end=""):
    print(count * line, end)


def my_cal():
    year = int(input("연도를 입력하세요: "))
    month = int(input("월를 입력하세요: "))
    start_week = day_of_week(year, month)

    line_print(30, "=")
    print(f" {year}년 {month}월 달력")
    line_print(30, "-")
    print("  일  월  화  수  목  금  토")

    padding = "    " * (start_week - 1)

    for i in range(1, last_day(year, month) + 1):
        if i == 1:
            print(padding, end="")

        print(f" {i:2d} ", end="")

        if (i + start_week - 1) % 7 == 0:
            print("")

    print("")
    line_print(30, "=")


my_cal()
