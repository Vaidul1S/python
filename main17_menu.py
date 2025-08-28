# Dictionary Menu exercise

menu = {"pizza": 5.99,
        "nachos": 3.99,
        "popcorn": 2.49,
        "chips": 0.99,
        "pretzel": 1.89,
        "soda": 1.49,
        "beer": 1.99
        }

cart = []
total = 0

print("----------Menu----------")
for key, value in menu.items():
    print(f"{key:10}: €{value:.2f}")

print("------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-------Your order-------")
for food in cart:
    total += menu.get(food)
    print(food, end = " ")

print()
print(f"Total is: €{total:.2f}")