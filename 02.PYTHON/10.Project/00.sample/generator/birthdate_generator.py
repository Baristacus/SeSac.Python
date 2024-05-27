import random


class BirthGenerator:
    year_s = 1980
    year_e = 2010

    def generator_birthdate(self):
        year = random.randint(self.year_s, self.year_e)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f"{year}-{month:02d}-{day:02d}"
