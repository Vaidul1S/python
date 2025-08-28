# This is Python - and this is comment 

print("I like pizza!")
print("Welcome to python 101")

# variables

# Strings
first_name = "Vaidulis"
food = "pizza"

# integers
age = 40
quantity = 5

# floats
price = 5.99
distance = 7.8

# boolean
is_sleeping = False
is_day = True

print(first_name)
print(f"Hello {first_name}!")                           # f stands for format, reikalingas kai norim irasyti kintamuosius {}
print(f"{first_name} likes {food} very much.")
print(f"{first_name} is {age} years old.")
print(f"{first_name} ate {quantity} {food}s.")
print(f"{food} costs {price} euros.")
print(f"{food} place is {distance} km to drive.")

if is_day:
    print(f"{first_name} is a wake.")

if is_sleeping:
    print(f"{first_name} is sleeping.")
