class Device:
    def info(self):
        print("Device information")

class Computer(Device):
    def info(self):
        super().info()
        print("Computer information")

class Laptop(Computer):
    def info(self):
        super().info()
        print("Laptop information")

laptop = Laptop()

laptop.info()