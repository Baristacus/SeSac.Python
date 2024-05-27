import random
import uuid


names = ["Alice", "Jane", "Tom", "Bob", "Chris"]
cities = ["New York", "Los Angeles", "Chicago", "Huston"]


def generator_uuid():
    return str(uuid.uuid4())


def generator_name():
    return random.choice(names)


def generator_birthdate():
    year = random.randint(1980, 2010)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year}-{month:02d}-{day:02d}"


def generator_gender():
    return random.choice(["Male", "Female"])


def generator_cities():
    city = random.choice(cities)
    street = random.randint(1, 100)
    return f"{street} {city}"


data = []

for _ in range(10):
    id = generator_uuid()
    name = generator_name()
    birthdate = generator_birthdate()
    gender = generator_gender()
    address = generator_cities()

    data.append((id, name, birthdate, gender, address))

for x in data:
    print(x)
