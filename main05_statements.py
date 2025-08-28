# Statements

age = float(input("Enter your age: "))

if age >= 18:
    print("You may enter!")
elif age > 100:
    print("Consolt your doctoc first please!")
else:
    print("You must be 18+ to enter!")

online = True

if online:
    print("You are online!")


weight = float(input("Enter your weight: "))
unit = input("Kg or lbs? (K/L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs."
    print(f"Your weight is {round(weight, 2)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "kg."
    print(f"Your weight is {round(weight, 2)} {unit}")
else:
    print(f"{unit} was not valid!")


