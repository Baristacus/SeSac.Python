""" 사용자 입력값을 받아 계산하기
1. 사용자에게 두가지 수를 입력 받는다.
    - (exit)를 제외한 문자를 입력했다면 오류를 발생시킨다
    -> 다시 숫자를 입력을 받을 수 있도록 한다.
2. 연산자를 입력받는다.
    - (+, -, *, /)중에서 입력을 받는다.
    - 4개중에 다른값을 받았다면 오류를 발생시킨다.
    - (/)입력을 받았을때 첫번째 숫자에 0이 포함되어 있다면 오류를 발생시킨다.
    -> 다시 연산자를 받을 수 있도록 한다.
3. 1번과 2번에서 오류가 없었다면 계산값을 출력한다.
4. 계산값이 나온 후 다시 계산을 할껀지 선택한다.
    - 계속 계산을 하고 싶다면 숫자를 입력하면 되고,
    종료하고 싶다면 (exit)를 입력하도록 메세지를 출력한다.
"""


def input_num1():
    num1 = input("첫번째 숫자를 입력하세요: ")
    if num1 == "exit":
        return exit(1)
    if not num1.isdigit() or num1 == None:
        return False
    return num1


def input_num2():
    num2 = input("두번째 숫자를 입력하세요: ")
    if not num2.isdigit() or num2 == None:
        return False
    return num2


def input_oper():
    operlist = ["+", "-", "*", "/"]
    oper = input("[+, -, *, /] 중에서 계산하고 싶은 연산자를 입력하세요.")
    if not oper in operlist:
        return False
    return oper


while True:
    while True:
        if num1 := input_num1():
            break
    while True:
        if num2 := input_num2():
            break
    while True:
        if oper := input_oper():
            break

    print(num1, num2, oper)
    if oper == "+":
        result = int(num1) + int(num2)
        print(f"{num1} + {num2}의 결과값은 {result}입니다.\n")
    elif oper == "-":
        result = int(num1) - int(num2)
        print(f"{num1} - {num2}의 결과값은 {result}입니다.\n")
    elif oper == "*":
        result = int(num1) * int(num2)
        print(f"{num1} * {num2}의 결과값은 {result}입니다.\n")
    elif oper == "/":
        result = int(num1) / int(num2)
        print(f"{num1} / {num2}의 결과값은 {result}입니다.\n")


# -------------------------------------------------------
# 클래스로 계산기 만들기


class Calculator:
    mode = None

    def set_mode(self, mode):
        self.mode = mode

    def calc_sum(self, num_1, num_2):
        return num_1 + num_2

    def calc_sub(self, num_1, num_2):
        return num_1 - num_2


my_calc = Calculator("표준")
print(my_calc.calc_sum(1, 2))


class EngCalculator(Calculator):
    def calc_mul(self, num_1, num_2):
        return num_1 * num_2


my_calc2 = EngCalculator("공학")
print(my_calc2.calc_mul(2, 3))
print(my_calc1.calc_sum(2, 3))
