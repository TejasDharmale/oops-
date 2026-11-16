class vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @property
    def start_engine(self):
        print(f"{self.brand} {self.model} engine started.")

    def stop_engine(self):
        print(f"{self.brand} {self.model} engine stopped.")


class car(vehicle):
    def __init__(self, brand, model, year, num_doors, no_of_wheels):
        # super() is used to call the constructor of the parent class (vehicle) to initialize the brand, model, and year attributes.
        super().__init__(brand, model, year)
        self.num_doors = num_doors
        self.no_of_wheels = no_of_wheels


class bike(vehicle):
    def __init__(self, brand, model, year, type_of_bike):
        super().__init__(brand, model, year)
        self.type_of_bike = type_of_bike


# Creating instances of car and bike
my_car = car("Toyota", "Camry", 2022, 4, 4)
my_bike = bike("Yamaha", "R1", 2021, "Sport")

print(my_car.__dict__)
print(my_bike.__dict__)

my_car.start_engine
