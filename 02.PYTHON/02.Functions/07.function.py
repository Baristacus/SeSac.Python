# 기본 입력값
def print_gugudan(dan=2, max=9):
    for i in range(1, max + 1):
        print(f"{dan} X {i} = {dan * i}")


print_gugudan()
