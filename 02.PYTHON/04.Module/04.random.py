# 랜덤 숫자 1 ~ 100까지 생성하는 라이브러리

import random

randint = random.randint(1, 100)
print(randint)


# 주사위를 던지는 함수를 작성
def dice():
    return random.randint(1, 6)


print(dice())

# 리스트에서 랜덤으로 요소를 선택
elements = ["apple", "banana", "pineapple", "grape", "cherry"]


def rand_list():
    return random.choice(elements)


print(rand_list())


# 랜덤으로 리스트 섞기


def rand_list2(elements):
    random.shuffle(elements)
    return elements


# print(rand_list2())
# print(elements)

# -----------------------------------------------------------


char_A = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
char_a = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
per = [
    0.1,
    0.2,
    0.3,
    0.2,
    0.1,
    0.2,
    0.5,
    0.3,
    0.9,
    0.7,
    0.3,
    0.5,
    0.2,
    0.9,
    0.1,
    0.6,
    0.5,
    0.8,
    0.3,
    0.5,
    0.9,
    0.2,
    0.9,
    0.2,
    0.4,
    0.4,
]


# 램덤으로 문자열 생성 (영문 대문자 6자리)
def rand_char():
    rand_char = random.sample(char_A, 6)
    rand_join = "".join(str(x) for x in rand_char)
    return rand_join


print(f"대문자 랜덤 문자열 6개: {rand_char()}")


# 가중치를 고려한 랜덤 (대문자 6자리)
def rand_char2():
    char_A_per = random.choices(char_A, per, k=6)
    char_join = "".join(str(x) for x in char_A_per)
    return char_join


print(f"가중치를 고려한 랜덤 문자열 6개: {rand_char2()}")


# 랜덤 비밀번호 생성(대소문자, 숫자 포함 8자리)
def rand_pass():
    rand_pass1 = random.sample(char_A + char_a + num, 8)
    num_to_str_join = "".join(str(x) for x in rand_pass1)
    return num_to_str_join


print(f"랜덤 비밀번호 생성(8-1): {rand_pass()}")


# 강력한 랜덤 비밀번호 생성(대소문자, 숫자를 각각 최소 1개 이상 포함)
def rand_pass2():
    rand_pass2_list = []

    def rand_pass2_A():
        rand_pass2_A = random.sample(char_A, 1)
        return rand_pass2_list.append(rand_pass2_A)

    def rand_pass2_a():
        rand_pass2_a = random.sample(char_a, 1)
        return rand_pass2_list.append(rand_pass2_a)

    def rand_pass2_num():
        rand_pass2_num = random.sample(num, 1)
        return rand_pass2_list.append(rand_pass2_num)

    while len(rand_pass2_list) < 8:
        rand_pass2_A()
        rand_pass2_a()
        rand_pass2_num()

    random.shuffle(rand_pass2_list)
    aaa = [x for y in rand_pass2_list for x in y]
    bbb = "".join(str(x) for x in aaa)

    return bbb


print(f"랜덤 비밀번호 생성(8-2): {rand_pass2()}")


def rand_pass3(number):
    char_num = char_A + char_a + num
    ppp = [random.choice(char_A), random.choice(char_a), random.choice(num)]

    while len(ppp) < number:
        ppp.append(random.choice(char_num))

    random.shuffle(ppp)

    return "".join(str(x) for x in ppp)


print(f"랜덤 비밀번호 생성(8-2): {rand_pass3(8)}")
