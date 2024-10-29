class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def start(self):
        print(f"Starting the {self.vehicle_type}...")

class Car(Vehicle):
    def __init__(self, vehicle_type, number_of_doors):
        super().__init__(vehicle_type)
        self.number_of_doors = number_of_doors

class ElectricCar(Car):
    def __init__(self, vehicle_type, number_of_doors, battery_capacity):
        super().__init__(vehicle_type, number_of_doors)
        self.battery_capacity = battery_capacity

electric_car = ElectricCar("Electric Car", 4, 90)

electric_car.start()
print(f"Number of doors: {electric_car.number_of_doors}")
print(f"Battery capacity: {electric_car.battery_capacity}")