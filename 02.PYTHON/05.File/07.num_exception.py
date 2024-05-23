def div(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return print("0으로 나눌 수 없음")
    except TypeError:
        return print("숫자가 아닌 값으로 나눌 수 없음")
    else:
        print("오류가 없을때")
    finally:
        print("무조건 나옴")

    return result


def div2(a, b):
    try:
        result = a / b
    except Exception as e:
        print("알수없는 오류: ", e)
        return "Nan"

    return result


# print(div(2, 1))
print(div2(2, 0))


def convert_to_int(num_str):
    try:
        result = int(num_str)
    except ValueError:
        print("문자로된 숫자만 입력")
    return result


print(convert_to_int("5"))
