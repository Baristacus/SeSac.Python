import random

last_name = []
middle_name = []
first_name = []


def create_name():
    kor_name = (
        random.choice(last_name)
        + random.choice(middle_name)
        + random.choice(first_name)
    )
    return kor_name


for _ in range(10):
    print(create_name())
