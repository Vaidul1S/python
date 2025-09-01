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
        print("Invalid number of players!")
        continue

print(players)
