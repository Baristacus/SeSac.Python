# 구구단 출력
dan = int(input())


def print_gugudan(dan):
    for i in range(1, 10):
        print(f"{dan} X {i} = {dan * i}")


print_gugudan(dan)
