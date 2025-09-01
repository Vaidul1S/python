name = input("What is your name?: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to a fork and you have to choose left or right: ").lower()
if answer == 'left':
    answer = input("You come to the river, you can alk around it or swim accross?(walk/swim): ").lower()
    if answer == 'walk':
        print("You walked for hours and died from hunger.")
    elif answer == 'swim':
        print("You swan accross and got eaten by alligator")
    else:
        print("Not a valid option. You lose.")
elif answer == 'right':
    answer = input("You come to a wobbly bridge, do you want to cross or go back: ").lower()
    if answer == 'cross':
        answer = input("You cross a wobbly bridge and meet a stranger, do you talk to them (yes/no): ").lower()
        if answer == "yes":
            print("Stranger became a fairy and gives you a gold bar. You won!")
        elif answer == "no":
            print("You keep wondering and die from heatstroke. You lose.")
        else:
            print("Not a valid option. You lose.")
    elif answer == 'back':
        print("You turn around and walk back and got eaten by bear. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print("Thank you", name, "to trying this adventure!")