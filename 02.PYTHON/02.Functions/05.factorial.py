# 팩토리얼 함수
def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result = result * i
    print(result)


factorial(5)
