import sys
import csv

from generator.id_generator import IdGenerator
from generator.name_generator import NameGenerator
from generator.address_generator import AdressGenerator
from generator.birthdate_generator import BirthGenerator
from generator.gender_generator import GenderGenerator


class DataGenerator:
    numbers = 1
    data = []

    def __init__(self, numbers):
        self.numbers = numbers
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator()
        self.birth_gen = BirthGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AdressGenerator()

    def generate_users(self):
        for _ in range(self.numbers):
            id = self.id_gen.generator_uuid()
            name = self.name_gen.generator_name()
            birthdate = self.birth_gen.generator_birthdate()
            gender = self.gender_gen.generator_gender()
            address = self.address_gen.generator_cities()

            self.data.append((id, name, birthdate, gender, address))


def print_to_screen(data):
    for d in data:
        print(d)


def save_to_file(data):
    with open("data_output.csv", "w", encoding="UTF-8") as file:
        write = csv.writer(file)
        for d in data:
            write.writerow(d)


# 메인함수
if __name__ == "__main__":

    if len(sys.argv) <= 1:
        num_data = input("생성 데이터 개수: ")
    else:
        num_data = sys.argv[1]

    # 데이터 형태 생성
    users = DataGenerator(int(num_data))
    users.generate_users()

    # 데이터 출력
    print_to_screen(users.data)
    save_to_file(users.data)
