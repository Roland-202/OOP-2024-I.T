class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Smartphone(Device):
    def __init__(self, brand, model, storage_capacity):
        super().__init__(brand, model)
        self.storage_capacity = storage_capacity

    def show_info(self):
        super().show_info()
        print(f"Storage Capacity: {self.storage_capacity}")


smartphone = Smartphone("Apple", "iPhone 15 Pro Max", "1TB")

smartphone.show_info()