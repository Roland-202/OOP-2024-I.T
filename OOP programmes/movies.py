class Movie:

  def __init__(self, title, Genre, release_year):
    
    self.title = title
    self.genre = Genre
    self.release_year = release_year

  def __str__(self):
   
    return f"This movie is titled '{self.title}' directed by {self.director} and released in {self.release_year}."

movie1 = Movie("DEADPOOL AND WOLVERINE", "Action", 1994)
movie2 = Movie("The Godfather", "Action", 1972)
movie3 = Movie("Abigail", "Horror", 2008)

print(movie1)
print(movie2)
print(movie3)