from unittest import result


def hello():
    print("hello1")
    print("hello2")
    print("hello3")


hello()


def numbers(num1):
    result = num1 + 4
    return result


num1 = numbers(3)

print(num1)

# ---------------------------
"""미션 1

덧셈을 하는 함수
숫자 두개를 입력 받아서, 해당 숫자의 합을 출력
"""


def sum(num1, num2):
    result = num1, num2, num1 + num2  # 튜플로 반환
    return result


print(sum(100, 500))


# ------------------------------
"""미션 2

+, -, *, /
숫자 두개를 입력 받아서, 결과 반환
"""


def sub(num1, num2):
    result = num1, num2, num1 - num2  # 튜플로 반환
    return result


def mul(num1, num2):
    result = num1, num2, num1 * num2  # 튜플로 반환
    return result


def div(num1, num2):
    result = num1, num2, num1 / num2  # 튜플로 반환
    return result


print(sub(5, 3))
print(mul(5, 3))
print(div(5, 3))
