class Restaurant:
 
  def __init__(self, name, food, rating):
    
    self.name = name
    self.food = food
    self.rating = rating

  def __str__(self):

    return f"This restaurant is '{self.name}' and serves {self.food} with a rating of {self.rating}."

restaurant1 = Restaurant("cafe javas", "East African", 4.5)
restaurant2 = Restaurant("KFC", "American", 4.0)
restaurant3 = Restaurant("sheraton", "East African", 4.8)

print(restaurant1)
print(restaurant2)
print(restaurant3)