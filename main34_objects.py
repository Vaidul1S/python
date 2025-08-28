# objects = bundels of atributes (vars) and methods (functions)
# class - blueprint for object

from modules.car import Car


car1 = Car("Zonda", 2015, "yellow", False)
car2 = Car("Veyron", 2020, "blue", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
print()

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
print()

car1.drive()
car1.stop()
print()

car2.drive()
car2.stop()
print()

car1.details()
car2.details()