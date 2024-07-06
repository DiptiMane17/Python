class Car:
    wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    def start(self):
        print(f"The {self.make} {self.model} is starting.")

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2019)

print(f"Car1 has {car1.wheels} wheels.")
print(f"Car2 has {car2.wheels} wheels.")

car1.display_info()
car1.start()

car2.display_info()
car2.start()
