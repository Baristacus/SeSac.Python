# 사용자 에러 클래스 만들기


class CustomError(Exception):
    # 속성 또는 함수(메소드) 추가
    pass


def check_value(value):
    if value < 0 or value > 100:
        raise CustomError("0보다 작거나 100보다 클 수 없음")
    return value


print(check_value(50))

try:
    result = check_value(1010)
except CustomError:
    print(CustomError)

print(result)
