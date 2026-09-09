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
text_font = "z003"

dice_art = {
    0: ("\n\n\n\n"),
    1: ("\n\n1\n\n"),
    2: (" \n2\n\n2\n"),
    3: ("\n3\n3\n3\n"),
    4: (" \n4         4\n\n4         4\n"),
    5: (" \n5         5\n5\n5         5\n"),
    6: (" \n6         6\n6         6\n6         6\n"),
}

max_players = 5
win_condition = 50

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        db = QFontDatabase()
        families = db.families() 
        for f in families:
            print(f)

        self.numb_of_players = 1
        self.players_points = []
        self.player_id = 0

        self.setWindowTitle("Pig Game")
        self.setGeometry(700, 300, 1000, 800)
        self.main_layout = QVBoxLayout()

        self.title_label = QLabel("Welcome to Pig Game", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont(f"{text_font}", 14))
        self.title_label.setStyleSheet(f"color: {font_color};" "font-weight: bold;")
        self.main_layout.addWidget(self.title_label)

        self.select_label = QLabel("Select number of players", self)
        self.select_label.setAlignment(Qt.AlignCenter)
        self.select_label.setFont(QFont(f"{text_font}", 12))
        self.select_label.setStyleSheet(f"color: {font_color};" "font-weight: bold;")
        self.main_layout.addWidget(self.select_label)

        self.select_button_box = QHBoxLayout()
        for x in range(max_players):
            self.numb_button = QPushButton(f"{x + 1}")
            self.numb_button.setFixedWidth(80)  
            self.numb_button.setFont(QFont(f"{text_font}", 14))
            self.numb_button.setStyleSheet(f"background-color: {button_color};" 
                                           f"color: {font_color};" 
                                           "border-radius: 10px;" 
                                           "line-height: 0;"
                                           "padding: 5px;")
            self.select_button_box.addWidget(self.numb_button)
        self.main_layout.addLayout(self.select_button_box)

        self.dice_label = QLabel("Roll your dice", self)
        self.dice_label.setAlignment(Qt.AlignCenter)
        self.dice_label.setFont(QFont(f"{text_font}", 12))
        self.dice_label.setStyleSheet(f"color: {font_color};" "font-weight: bold;")
        self.main_layout.addWidget(self.dice_label)

        self.turn_label = QLabel("", self)
        self.turn_label.setAlignment(Qt.AlignCenter)
        self.turn_label.setFont(QFont(f"{text_font}", 12))
        self.turn_label.setStyleSheet(f"color: {font_color};" "font-weight: bold;")
        self.main_layout.addWidget(self.turn_label)

        self.dice_button = QPushButton(f"{dice_art[0]}")
        self.dice_button.setFont(QFont(f"{text_font}", 16))
        self.dice_button.setStyleSheet(f"background-color: {button_color};" 
                                       f"color: {font_color};" 
                                       "border-radius: 10px;" 
                                       "padding: 5px;" 
                                       "font-weight: bold;" 
                                       "margin: 0px 410px")
        self.main_layout.addWidget(self.dice_button)

        self.pass_button = QPushButton("Pass the turn", self)
        self.pass_button.setFont(QFont(f"{text_font}", 14))
        self.pass_button.setStyleSheet(f"background-color: {button_color};"
                                       f"color: {font_color};"
                                       "border-radius: 10px;" 
                                       "padding: 8px;" 
                                       "margin: 20px 380px")
        self.main_layout.addWidget(self.pass_button)

        self.points_box = QHBoxLayout()        
        self.main_layout.addLayout(self.points_box)

        self.result_label = QLabel(" ",self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setFont(QFont(f"{text_font}", 18))
        self.result_label.setStyleSheet(f"color: {font_color};" "font-weight: bold;")
        self.main_layout.addWidget(self.result_label)
        

        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)    

        self.initUI()
                        
    def initUI(self):
        for x in range(self.select_button_box.count()):
            item = self.select_button_box.itemAt(x).widget()
            if isinstance(item, QPushButton):
                item.clicked.connect(lambda checked, x=x: self.set_players_numb(x+1))  

        self.dice_button.clicked.connect(self.roll)
        self.pass_button.clicked.connect(self.pass_turn)

    def set_players_numb(self, numb):
        self.numb_of_players = numb
        self.result_label.setText(" ")
        if self.points_box.count() > 0:
            for x in range(self.points_box.count()):
                item = self.points_box.itemAt(0).widget()
                self.points_box.removeWidget(item)              
        for x in range(self.numb_of_players):
            self.players_points.append(0)
            self.points = QLabel(f"Player {x + 1} points:\n {self.players_points[x]}", self)
            self.points.setFont(QFont(f"{text_font}", 12))
            self.points.setFixedWidth(120)
            self.points.setStyleSheet(f"color: {font_color};" "font-weight: bold;")
            self.points_box.addWidget(self.points)
        self.turn_label.setText(f"Player {self.player_id + 1} turn to roll")
        
    def roll(self):
        if self.points_box.count() < 1:
            self.result_label.setText("Select number of players first, please")
        else:
            self.result_label.setText(" ")
            restult = random.randint(1, 6)
            self.dice_button.setText(f"{dice_art[restult]}")        
            item = self.points_box.itemAt(self.player_id).widget()
            if restult > 1:
                self.players_points[self.player_id] += restult
                item.setText(f"Player {self.player_id + 1} points:\n {self.players_points[self.player_id]}")
                if self.players_points[self.player_id] >= 50:
                    self.result_label.setText(f"Player {self.player_id + 1} WON!")
            else:
                self.players_points[self.player_id] = 0
                item.setText(f"Player {self.player_id + 1} points:\n {self.players_points[self.player_id]}")
                self.player_id += 1
                if self.player_id > self.numb_of_players - 1:
                    self.player_id = 0
                self.turn_label.setText(f"Player {self.player_id + 1} turn to roll")
                

    def pass_turn(self):
        self.player_id += 1
        if self.player_id > self.numb_of_players - 1:
            self.player_id = 0
        self.dice_button.setText(f"{dice_art[0]}")
        self.turn_label.setText(f"Player {self.player_id + 1} turn to roll")
        
        
        
            


def main():
    app = QApplication(sys.argv)                                         
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()