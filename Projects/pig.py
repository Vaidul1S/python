import random

def roll():
    min = 1
    max = 6
    roll = random.randint(min, max)
    return roll

while True: 
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
            break
        else:
            print("Number of players must be beeen 2 - 4!")
    else:
        print("Invalid number of players!")
        
max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:

    for player_i in range(players):
        print("\nPlayer", player_i + 1, "turn to roll!")
        print("Your total score is:", players_scores[player_i], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll?(Y/N): ").lower()
            if should_roll != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            
            print("Your score is", current_score)

        players_scores[player_i] += current_score
        print("Your total score is:", players_scores[player_i])

max_score = max(players_scores)
winner_i = players_scores.index(max_score)
print("Player number", winner_i + 1, "is the winner with a score of:", max_score)