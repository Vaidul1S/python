import random

# Rock Paper Scissors

options = ("Rock", "Paper", "Scissors")
playing = True

while playing:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (Rock, Paper, Scissors): ").capitalize()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "Paper" and computer == "Rock":
        print("You win!")
    elif player == "Rock" and computer == "Scissors":
        print("You win!")
    elif player == "Scissors" and computer == "Paper":
        print("You win!")
    else:
        print("You lose!")

    playAgain = input("Would you like to olay again? (Y/N)").upper()

    if not playAgain == "Y":
        playing = False

print("Thanks for playing!:)")