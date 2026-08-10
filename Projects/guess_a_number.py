import random

print("Welcome to the Number Guessing Game (lower-higher)")
top_of_range = input("Set a range between 0 and: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number greater than 0 next time!")
        quit()
else:
    print("Please type a number next time!")
    quit()

random_number = random.randint(0, top_of_range)                
guesses = 0

while True:
    guesses += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number next time!")
        continue

    if guess == random_number:
        print("Correct! You got it!")
        break
    elif guess > random_number:
        print("You were ABOVE the number!")
    else:
        print("You were BELOW the number!")        

print("You got it in", guesses, "guesses.")