# Shoping cart

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("-------Shoping Cart-------")

for f in foods:
    print(f, end = " ")

print()

for p in prices:
    print(p, end = " ")
    total += p

print()
print("-------Total Price-------")
print(f"Your total is $ {total}")