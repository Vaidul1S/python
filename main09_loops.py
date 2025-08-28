# while loop

name = input("Enter your name: ")

while name == "":
    print("Please fill a field!")    
    name = input("Enter your name: ")    
else:
    print(f"Hello, {name}")

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid!")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")

# for loop

for x in range (1,11):                                          # skaiciuojam nuo 1 iki 10
    print(x)

for x in reversed(range(1, 11)):                                # skaiciuojam nuo 10 iki 1
    print(x)
print("Happy New Year!!!")

for x in range(1, 21, 2):                                       # skaiciuojam nuo 1 iki 20 kas 2 skaicius
    print(x)

for x in range(1, 21):
    if x == 13:                                                 # skipinam 13
        continue
    else: print(x)

for x in range(1, 21):
    if x == 13:                                                 # kai pasiekiam 13 sustojam
        break
    else: print(x)

# nested loop

for x in range(10):
    for y in range (1, 10):
        print(x, end=" ")                                       # end="bet kas" printis i viena eilute ir i tarpus des "bet kas"
    print()


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
symb = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range (cols):
        print(symb, end="")   
    print()                                    

