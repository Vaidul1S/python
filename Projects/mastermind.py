#  There is two versions of Mastermind here: terminal and GUI.
import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

#  You can switch versions: True for GUI and False for terminal
GUI = True

COLORS = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple"]
TRIES = 10
CODE_LENGTH = 5

def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != 4:
            print(f"You must guess {CODE_LENGTH} colors!")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again!")
                break
        else:
            break

    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():    
    print("Welcome to the Mastermind!")
    print(f"You have {TRIES} tries to guess the code of {CODE_LENGTH} colors.")
    print(f"The valid colors are", *COLORS)

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        if correct_pos == CODE_LENGTH:
            print(f"Congrats 🎉 You guessed the code {code} in {attempts} tries!")
            break
        print(f"Correct Positions: {correct_pos} | Incorect positions: {incorrect_pos}")

    else:
        print(f"You ran of tries, the correct code was", *code)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.code = generate_code()
        self.tries = 10
        self.guess = []
        self.colors = []
        for x in range(CODE_LENGTH):
            self.colors.append("darkgray")   

        self.setWindowTitle("Mastermind")
        self.setGeometry(700, 300, 800, 400)
        self.main_layout = QVBoxLayout()        

        self.label01 = QLabel(f"Guess the code of {CODE_LENGTH} colors.", self)
        self.label01.setAlignment(Qt.AlignCenter)
        self.label01.setFont(QFont("monospace", 12))
        self.label01.setStyleSheet("color: cyan;"                                  
                            "font-weight: bold;")
        self.main_layout.addWidget(self.label01)
        
        self.colors_box = QHBoxLayout()
        for x in range(len(COLORS)):
            self.color_button = QPushButton("")
            self.color_button.setStyleSheet(f"background-color: {COLORS[x]};" "color: black;" "border-radius: 2px;" "padding: 7px;" "margin: 5px")
            self.color_button.setText(f"{COLORS[x]}")
            self.colors_box.addWidget(self.color_button)
        self.main_layout.addLayout(self.colors_box)
        
        self.label02 = QLabel(f"", self)
        self.label02.setAlignment(Qt.AlignCenter)
        self.label02.setFont(QFont("monospace", 14))
        self.label02.setStyleSheet("color: cyan;"                                  
                            "font-weight: bold;")
        self.main_layout.addWidget(self.label02)

        self.clear_button = QPushButton("Clear Selection")
        self.clear_button.setStyleSheet("color: cyan;" "font-family: monospace;" "padding: 5px;" "margin: 5px 230px")
        self.main_layout.addWidget(self.clear_button)
                
        self.pick_label = QLabel("Your pick:", self)
        self.pick_label.setAlignment(Qt.AlignCenter)
        self.pick_label.setFont(QFont("monospace", 12))
        self.pick_label.setStyleSheet("color: cyan;"                                  
                            "font-weight: bold;")        
        self.main_layout.addWidget(self.pick_label)   

        self.pick_boxes = QHBoxLayout()
        for x in range(CODE_LENGTH):
            self.pick = QPushButton("")
            self.pick_boxes.addWidget(self.pick)
        self.update_pick_colors() 
        self.main_layout.addLayout(self.pick_boxes)

        self.last_pick_box = QVBoxLayout()
        self.last_color_box = QHBoxLayout()
        for x in range(CODE_LENGTH):
            self.last_pick = QPushButton("")
            self.last_color_box.addWidget(self.last_pick)           
        self.update_last_guess_colors()

        self.guess_label = QLabel(f"Your last guess was: {self.guess}", self)
        self.guess_label.setFont(QFont("monospace", 12))
        self.guess_label.setStyleSheet("color: cyan;"
                                       "font-weight: bold")
        self.guess_label.setAlignment(Qt.AlignCenter)
        self.last_pick_box.addWidget(self.guess_label)
        self.last_pick_box.addLayout(self.last_color_box)        
        self.main_layout.addLayout(self.last_pick_box)        

        self.result_label = QLabel("Good luck!", self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setFont(QFont("monospace", 14))
        self.result_label.setStyleSheet("color: cyan;"                          
                           "font-weight: bold")
        self.main_layout.addWidget(self.result_label)

        self.submit_button = QPushButton("Submit", self)        
        self.submit_button.setStyleSheet("font-size: 24px;" 
                                  "font-family: monospace;" 
                                  "color: cyan;" 
                                  "padding: 15px;" 
                                  "margin: 15px 150px")
        self.main_layout.addWidget(self.submit_button)
        
        self.tries_label = QLabel(f"Tries left: {self.tries}", self)
        self.tries_label.setFont(QFont("monospace", 12))
        self.tries_label.setAlignment(Qt.AlignRight)
        self.tries_label.setStyleSheet("color: cyan;"
                                       "margin: 15px;"
                                       "font-weight: bold")        
        self.main_layout.addWidget(self.tries_label)       

        self.play_again = QPushButton("Play Again", self)
        self.play_again.setStyleSheet("font-size: 16px;"
                                      "font-family: monospace;"
                                      "font-weight: bold;"
                                      "color: cyan;"
                                      "padding: 5px;"
                                      "margin: 10px 650px 10px 10px")
        self.main_layout.addWidget(self.play_again)

        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)       
        
        self.initUI()
                
    def initUI(self):
        for x in range(self.colors_box.count()):
            item = self.colors_box.itemAt(x).widget()
            if isinstance(item, QPushButton):
                item.clicked.connect(lambda checked, x=x: self.add_pick(f"{COLORS[x]}"))      

        self.clear_button.clicked.connect(self.clear_pick)
        self.submit_button.clicked.connect(self.on_submit)
        self.play_again.clicked.connect(self.refresh)

    def update_pick_colors(self):
        for x in range(self.pick_boxes.count()):
            item = self.pick_boxes.itemAt(x).widget()
            if isinstance(item, QPushButton):
                item.setStyleSheet(f"background-color: {self.colors[x]};" "color: black;" "border-radius: 2px;" "padding: 7px;" "margin: 15px 15px;")

    def update_last_guess_colors(self):
        for x in range(self.last_color_box.count()):
            item = self.last_color_box.itemAt(x).widget()
            if isinstance(item, QPushButton):
                item.setStyleSheet(f"background-color: {self.colors[x]};" "color: black;" "border-radius: 2px;" "padding: 7px;" "margin: 15px 15px")

    def on_submit(self):
        if len(self.guess) != CODE_LENGTH:
            self.label02.setText(f"You must guess {CODE_LENGTH} colors!")            
            return
        
        self.label02.setText(f"")         
        self.guess_label.setText(f"Your guess before was: {self.guess}")  
        
        correct_pos, incorrect_pos = check_code(self.guess, self.code)
        self.result_label.setText(f"Correct Positions: {correct_pos} Incorect positions: {incorrect_pos}")
        
        if self.tries == 0:
            self.result_label.setText(f"YOU LOST! Code was {self.code}")
            self.end_game()
        if self.guess != self.code:
            self.tries -= 1
            self.tries_label.setText(f"Tries left: {self.tries}")
            self.guess = []            
        if self.guess == self.code:
            self.result_label.setText(f"YOU WON! Code was {self.code}")
            self.end_game()

        self.update_last_guess_colors()
        self.clear_pick()

    def add_pick(self, color):                
        self.guess.append(color)
        self.pick_label.setText(f"Your pick: {self.guess}")
        for x in range(len(self.guess)):
            if x > len(self.colors) - 1:
                break
            else:
                self.colors[x] = self.guess[x]  
        self.update_pick_colors()         

    def clear_pick(self):
        self.guess = []
        self.pick_label.setText(f"Your pick:")
        self.colors = []
        for x in range(CODE_LENGTH):
            self.colors.append("darkgray")   
        self.update_pick_colors()   

    def end_game(self):
        for x in range(self.colors_box.count()):
            item = self.colors_box.itemAt(x).widget()
            if isinstance(item, QPushButton):
                item.setDisabled(True)
        self.clear_button.setDisabled(True)
        self.submit_button.setDisabled(True)

    def refresh(self):
        self.code = generate_code()
        self.tries = 10
        self.tries_label.setText(f"Tries left: {self.tries}")
        self.guess = []
        self.pick_label.setText(f"Your pick:")
        self.colors = []
        for x in range(CODE_LENGTH):
            self.colors.append("darkgray")   
        self.update_pick_colors()
        self.update_last_guess_colors()
        self.guess_label.setText("Your guess before was: """)
        self.result_label.setText("Good luck!")
        for x in range(self.colors_box.count()):
            item = self.colors_box.itemAt(x).widget()
            if isinstance(item, QPushButton):
                item.setDisabled(False)
        self.clear_button.setDisabled(False)
        self.submit_button.setDisabled(False)


if __name__ == "__main__":

    if GUI:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    else: 
        game()
    