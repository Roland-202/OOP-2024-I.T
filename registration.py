class Student:
    

    def __init__(self, registration_number, name, course, semester):
      
        self.registration_number = registration_number
        self.name = name
        self.course = course
        self.semester = semester

    def display_registration_number(self):
        
        print(f"""
        Registration Number: {self.registration_number}
        Name: {self.name}
        Course: {self.course}
        Semester: {self.semester}
        """)

student1 = Student("S23B13/066", "BLESSED ROLLAND", "BSIT", "ADVENT")
student2 = Student("M23B13/077", "MUKASA JONATHAN", "BSCS", "TRINITY")
student3 = Student("S23B13/056", "KYEMBE LUQMAN", "BSDS", "ADVENT")


student1.display_registration_number()
student2.display_registration_number()
student3.display_registration_number()