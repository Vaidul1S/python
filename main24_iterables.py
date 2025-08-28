# Iterables

numbers = [1,2,3,4,5,6,7,8,9,10]                # can be list[], tuple(), set{}

for numb in reversed(numbers):
    print(numb, end=" ")

fruits = {"apple", "pear", "orange", "greatfruit"}

print()

for fruit in fruits:
    print(fruit, end=" ")

print()

cars = ("ford", "dodge", "chevy", "mazda")

for car in sorted(cars):
    print(car, end=" ")

print()

my_dictionary = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5,}

for key, value in my_dictionary.items():        # buildin keys(), values(), items()
    print(f"{key}: {value}")