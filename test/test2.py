class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        
    def show_details(self, age):
        print(f"Name of the student is :{self.name}")
        print(f"Rollno of the student is : {self.rollno}")
        print(f"Age of the student is :{age}")
    
s = Student("Abani", 12)
s.name = "Rahul"
s.rollno = 56
s.show_details(age=4)