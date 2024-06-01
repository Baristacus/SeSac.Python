class Car:
    brand = ""
    model = ""
    ordometer = 0

    def get_name(self):
        print(f"{self.brand} {self.model}")

    def get_ordometer(self):
        print(f"주행거리: {self.ordometer}")

    def drive(self, mileage):
        self.ordometer += mileage
        # or self.ordometer = self.ordometer + mileage


mycar = Car()
mycar.brand = "BMW"
mycar.model = "X3"

mycar.get_name()
mycar.get_ordometer()
mycar.drive(100)
mycar.get_ordometer()
