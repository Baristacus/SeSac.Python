from itertools import chain
import csv
import random


class NameGenerator:
    names = []

    def __init__(self):
        with open("names.csv", "r", encoding="UTF-8") as file:
            # names = file.read().splitlines()  # .splitlines() 줄 단위로 잘라서 읽음
            csv_r = csv.reader(file)
            csv_list_name = [n for n in csv_r]
            names_list = list(chain(*csv_list_name))
            self.names = [n.strip() for n in names_list]
            print(self.names)

    def generator_name(self):
        return random.choice(self.names)
