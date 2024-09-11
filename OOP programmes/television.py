class Television:

  def __init__(self, color, size, price):
  
    self.color = color
    self.size = size
    self.price = price

  def __str__(self):

    return f"This television is {self.color}, {self.size} inches, and costs ugx {self.price}."

samsung = Television("silver",72,"2,400,000")
sony = Television("black",43,"1,500,000")
hisense = Television("black", 55, "1,400,000")

print(hisense)  
print(sony)
print(samsung)

