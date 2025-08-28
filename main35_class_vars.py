# Class Variables - shared amoung all instances of a class

class Car:
    wheels = 4                                                      # class variable

    def __init__(self, model, year):
        self.model = model
        self.year = year

class Student:

    class_year = 2025
    num_students = 0                                               # class variable

    def __init__(self, name, age):                                  # constructor
        self.name = name
        self.age = age
        Student.num_students += 1




student1 = Student("Ella", 17)
student2 = Student("Emi", 27)
student3 = Student("Cinna", 28)
student3 = Student("Bonnie", 29)

print(student1.name)
print(student1.age)
print(student1.class_year)                                          # not so good practice
print()

print(student2.name)
print(student2.age)
print()

print(Student.class_year)                                           # good practice
print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")