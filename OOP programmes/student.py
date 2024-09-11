class Student:
  
  def __init__(self, name, course, gpa):

    self.name = name
    self.course = course
    self.gpa = gpa

  def __str__(self):

    return f"This student is  {self.name}, majors in {self.course}, and has a GPA of {self.gpa}."

student1 = Student("Blessed", "Computer Science", 4.8)
student2 = Student("Nicholas", "information systems", 4.9)
student3 = Student("Roland", "Data science", 4.7)

print(student1)
print(student2)
print(student3)