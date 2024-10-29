class Appliance:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

class Washing_Machine(Appliance):
    def __init__(self, brand, power, drum_size):
        super().__init__(brand, power)
        self.drum_size = drum_size

    def show_details(self):
        print(f"Brand: {self.brand}, Power: {self.power}W, Drum Size: {self.drum_size}kg")

washing_machine = Washing_Machine("Samsung", 2000, 8)

washing_machine.show_details()