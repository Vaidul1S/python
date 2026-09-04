import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap, QFontDatabase
from PyQt5.QtCore import Qt

# Pig is a simple dice game first described in print by John Scarne in 1945. 
# Players take turns to roll a single dice as many times as they wish, adding all roll results to a running total, 
# but losing their gained score for the turn if they roll a 1.


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
font_color = "blue"
button_color = "green"

dice_art = {
    0: ("┌─────┐\n|                       |\n|                       |\n|                       |\n└─────┘"),
    1: ("┌─────┐\n|                     |\n|         ♣         |\n|                     |\n└─────┘"),
    2: ("┌─────┐\n|     ♣             |\n|                     |\n|             ♣     |\n└─────┘"),
    3: ("┌─────┐\n|     ♣             |\n|         ♣         |\n|             ♣     |\n└─────┘"),
    4: ("┌─────┐\n|    ♣      ♣    |\n|                     |\n|    ♣      ♣    |\n└─────┘"),
    5: ("┌─────┐\n|    ♣      ♣    |\n|         ♣         |\n|    ♣      ♣    |\n└─────┘"),
    6: ("┌─────┐\n|    ♣      ♣    |\n|    ♣      ♣    |\n|    ♣      ♣    |\n└─────┘"),
}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.numb_of_players = 5
        self.players_points = []

        self.setWindowTitle("Pig Game")
        self.setGeometry(700, 300, 1000, 800)
        self.main_layout = QVBoxLayout()

        self.title_label = QLabel("Welcome to Pig Game", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("times", 14))
        self.title_label.setStyleSheet(f"color: {font_color};"                                  
                                    "font-weight: bold;")
        self.main_layout.addWidget(self.title_label)

        self.select_label = QLabel("Select number of players", self)
        self.select_label.setAlignment(Qt.AlignCenter)
        self.select_label.setFont(QFont("times", 12))
        self.select_label.setStyleSheet(f"color: {font_color};"
                                        "font-weight: bold;")
        self.main_layout.addWidget(self.select_label)

        self.select_button_box = QHBoxLayout()
        for x in range(self.numb_of_players):
            self.numb_button = QPushButton(f"{x + 1}")
            self.numb_button.setFixedWidth(80)  
            self.numb_button.setStyleSheet(f"background-color: {button_color};" f"color: {font_color};" "border-radius: 10px;" "padding: 5px;")
            self.select_button_box.addWidget(self.numb_button)
        self.main_layout.addLayout(self.select_button_box)

        self.dice_label = QLabel("Roll your dice", self)
        self.dice_label.setAlignment(Qt.AlignCenter)
        self.dice_label.setFont(QFont("times", 12))
        self.dice_label.setStyleSheet(f"color: {font_color};"
                                        "font-weight: bold;")
        self.main_layout.addWidget(self.dice_label)

        self.dice_button = QPushButton(f"{dice_art[0]}")
        self.dice_button.setFixedWidth(150)      
        self.dice_button.setFont(QFont("times", 16))
        self.dice_button.setStyleSheet(f"background-color: {button_color};" f"color: {font_color};" "border-radius: 10px;" "padding: 5px;")
        self.main_layout.addWidget(self.dice_button)

        

        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)    

        self.initUI()
                        
    def initUI(self):
        self.dice_button.clicked.connect(self.roll)

    def roll(self):
        restult = random.randint(1, 6)
        self.dice_button.setText(f"{dice_art[restult]}")


def main():
    app = QApplication(sys.argv)                                         
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()