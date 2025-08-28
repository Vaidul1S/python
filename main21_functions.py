# functions

def song(name, age):
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print(f"Happy birthday dear {name}!")
    print(f"You're {age} years old bitch!")

song("Tina", 27)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"You bill of ${amount:.2f} is due: {due_date}")

display_invoice("Joe Shmow", 500, "07.01")

def add(a, b):
    c = a + b
    return c

print(add(2, 2))

