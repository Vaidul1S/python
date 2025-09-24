# Guessing game

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("\nPython Number Guessing Game\n")
print(f"Guess a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Guess a number: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("Guess is out of range!")
            print(f"The number must be between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("To low! Try again!")
        elif guess > answer:
            print("To high! Try again!")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"You took {guesses} guesses.")
            playAgain = input("Would you like to play again? (Y/N)")
            if not playAgain.upper() == "Y":
                is_running = False
            else:
                answer = random.randint(lowest_num, highest_num)
    else:
        print("Invalid guess")
        print(f"Select a number between {lowest_num} and {highest_num}")
