# Typecasting - converting

name = "Ella Gross"
age = 17
height = 1.58
meovv = 5
is_idol = True

age = float(age)                    # verciam i racionaluji
age = str(age)                      # verciam i stinga
age = bool(age)                     # verciam i boolean
height = int(height)                # verciam i int ir nukandam po kablelia viska

print(type(age), age)
print(type(height), height)

# input

name2 = input("What is your name?: ")       # input visada stringas
age2 = int(input("How old are you?"))       # paverciam i int

print(f"Hello {name2}!")
print(f"You are {age2} years old.")
print(type(age2), age2)

# exercise 1

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"Area is equal {area}")

# exercise 2

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} of {item}'s")
print(f"Your total is {total} €.")