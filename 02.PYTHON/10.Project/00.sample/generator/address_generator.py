import random
from itertools import chain
import csv


class AdressGenerator:

    cities = []

    def generator_cities(self):
        with open("address.csv", "r", encoding="UTF-8") as file:
            csv_r = csv.reader(file)
            csv_list_addr = [n for n in csv_r]
            addr_list = list(chain(*csv_list_addr))
            self.cities = [n.strip() for n in addr_list]
        city = random.choice(self.cities)
        street = random.randint(1, 100)
        return f"{street} {city}"
