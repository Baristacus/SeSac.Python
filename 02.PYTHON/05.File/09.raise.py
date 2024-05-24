# raise: 에러를 강제로 발생시키기 위해 사용


def input_age(age):
    if age < 0:
        raise ValueError("음수입력 안됨")
    print(age)

    return age


try:
    input_age(10)
    input_age(20)
    input_age(0)
    input_age(-1)
except ValueError:
    print("입력값에 오류가 있음", ValueError)
