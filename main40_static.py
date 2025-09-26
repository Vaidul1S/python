# Static method - priklauso klasei, o ne objektui sukurtam pagal klase

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):                                                 #instance method, kruva tokiu darem jau
        return f"{self.name} >>--> {self.position}"
    
    @staticmethod                                                       # static method
    def is_valid_position(position):
        valid_postions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_postions
    

employee1 = Employee("Spongebob", "Cook")
employee2 = Employee("Larry", "Cashier")
employee3 = Employee("Garry", "Manager")


print(Employee.is_valid_position("Cook"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())