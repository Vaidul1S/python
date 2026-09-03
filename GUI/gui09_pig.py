import random
import sys
import math
import pygame
pygame.init()

# Pig is a simple dice game first described in print by John Scarne in 1945. 
# Players take turns to roll a single dice as many times as they wish, adding all roll results to a running total, 
# but losing their gained score for the turn if they roll a 1.

WIDTH, HEIGHT = 1000, 800
LABEL_FONT = pygame.font.SysFont("monospace", 24)
BAR_HEIGHT = 30
BAR_TEXT_COLOR = "white"
BackGround = "darkblue"
WIN = pygame.display.set_mode((WIDTH, HEIGHT), display=0)
pygame.display.set_caption("Pig Game")

numb_of_players = 3
players_points = []
for x in range(numb_of_players):
    players_points.append(0)

# def roll():
#     min = 1
#     max = 6
#     roll = random.randint(min, max)
#     return roll

# while True: 
#     players = input("Enter the number of players(2-4): ")
#     if players.isdigit():
#         players = int(players)
#         if 2 <= players <=4:
#             break
#         else:
#             print("Number of players must be beeen 2 - 4!")
#     else:
#         print("Invalid number of players!")

# # winning condition     
# max_score = 50
# players_scores = [0 for _ in range(players)]

# while max(players_scores) < max_score:

#     for player_i in range(players):
#         print("\nPlayer", player_i + 1, "turn to roll!")
#         print("Your total score is:", players_scores[player_i], "\n")
#         current_score = 0

#         while True:
#             should_roll = input("Would you like to roll?(Y/N): ").lower()
#             if should_roll != "y":
#                 break

#             value = roll()
#             if value == 1:
#                 print("You rolled 1! Turn done!")
#                 current_score = 0
#                 break
#             else:
#                 current_score += value
#                 print("You rolled a:", value)
            
#             print("Your score is", current_score)

#         players_scores[player_i] += current_score
#         print("Your total score is:", players_scores[player_i])

# max_score = max(players_scores)
# winner_i = players_scores.index(max_score)
# print("Player number", winner_i + 1, "is the winner with a score of:", max_score)

def main():
    
    draw(WIN)
    draw_top_bar(WIN)
    pygame.display.update()
    
    
pygame.quit()

def draw(win):
    win.fill(BackGround)

def draw_top_bar(win):
    pygame.draw.rect(win, "green", (0, 0, WIDTH, BAR_HEIGHT))

    for x in range(numb_of_players):
        player_label = LABEL_FONT.render(f"Points: {players_points[x]}", 1, BAR_TEXT_COLOR)
    
    win.blit(player_label, (100, 5))

if __name__ == "__main__":
    main()