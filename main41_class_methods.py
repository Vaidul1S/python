# Class methods

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod                                                        # class method (cls - class), modifikuoti klases atributam, kuriem nereikia klases duomenu
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa is: {cls.total_gpa / cls.count:.2f}"

student1 = Student("Spongebob", 2.1)
student2 = Student("Larry", 3.5)
student3 = Student("Garry", 4.0)

print(Student.get_count())
print(Student.get_average_gpa())