class Car:
 
  def __init__(self, make, model, year):

    self.make = make
    self.model = model
    self.year = year

  def __str__(self):

    return f"This car is a {self.year} {self.make} {self.model}."

car1 = Car("Toyota", "Hilux", 2023)
car2 = Car("Ford", "Ranger", 2022)
car3 = Car("Lamborghini", "urus", 2023)

print(car1)
print(car2)
print(car3)