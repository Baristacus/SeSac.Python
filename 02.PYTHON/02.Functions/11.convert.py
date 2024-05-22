# 문자열을 입력받아, 대소문자 변경
# 대문자 <-> 소문자


def convert_case(text):
    convert_txt = ""
    for t in text:
        if t.islower():
            convert_txt += t.upper()
        elif t.isupper():
            convert_txt += t.lower()
        else:
            convert_txt += t
    return convert_txt


print(convert_case("HELLO"))
print(convert_case("Hello"))
print(convert_case("hello"))
print(convert_case("hello World!"))
