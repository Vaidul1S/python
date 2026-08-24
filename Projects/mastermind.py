#  There is two versions of Mastermind here: terminal and GUI.
#  You can switch them at a very bottom
import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

COLORS = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple"]
TRIES = 10
CODE_LENGTH = 4

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
        self.colors = ["darkgray", "darkgray", "darkgray", "darkgray"]   

        self.setWindowTitle("Mastermind")
        self.setGeometry(700, 300, 800, 400)
        self.main_layout = QVBoxLayout()        

        self.label01 = QLabel(f"Guess the code of {CODE_LENGTH} colors.", self)
        self.label01.setAlignment(Qt.AlignCenter)
        self.label01.setFont(QFont("monospace", 12))
        self.label01.setStyleSheet("color: cyan;"                                  
                            "font-weight: bold;")
        self.main_layout.addWidget(self.label01)

        self.button1 = QPushButton("Red")
        self.button1.setStyleSheet("background-color: red;" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 5px")
        self.button2 = QPushButton("Blue")
        self.button2.setStyleSheet("background-color: blue;" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 5px")
        self.button3 = QPushButton("Green")
        self.button3.setStyleSheet("background-color: green;" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 5px")
        self.button4 = QPushButton("Yellow")
        self.button4.setStyleSheet("background-color: yellow;" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 5px")
        self.button5 = QPushButton("Orange")
        self.button5.setStyleSheet("background-color: Orange;" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 5px")
        self.button6 = QPushButton("Purple")
        self.button6.setStyleSheet("background-color: purple;" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 5px")                
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        hbox.addWidget(self.button4)
        hbox.addWidget(self.button5)
        hbox.addWidget(self.button6)
        self.main_layout.addLayout(hbox)
        
        
        self.label02 = QLabel(f"", self)
        self.label02.setAlignment(Qt.AlignCenter)
        self.label02.setFont(QFont("monospace", 14))
        self.label02.setStyleSheet("color: cyan;"                                  
                            "font-weight: bold;")
        self.main_layout.addWidget(self.label02)

        self.clear_selection = QPushButton("Clear")
        self.clear_selection.setStyleSheet("color: cyan;" "font-family: monospace;" "padding: 5px;" "margin: 5px 230px")
        self.main_layout.addWidget(self.clear_selection)

        self.pick_label = QLabel("Your pick:", self)
        self.pick_label.setAlignment(Qt.AlignCenter)
        self.pick_label.setFont(QFont("monospace", 12))
        self.pick_label.setStyleSheet("color: cyan;"                                  
                            "font-weight: bold;")
        self.main_layout.addWidget(self.pick_label)   


        self.pick1 = QPushButton("")
        self.pick1.setStyleSheet(f"background-color: {self.colors[0]};" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 15px 25px")
        self.pick2 = QPushButton("")
        self.pick2.setStyleSheet(f"background-color: {self.colors[1]};" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 15px 25px")
        self.pick3 = QPushButton("")
        self.pick3.setStyleSheet(f"background-color: {self.colors[2]};" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 15px 25px")
        self.pick4 = QPushButton("")
        self.pick4.setStyleSheet(f"background-color: {self.colors[3]};" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 15px 25px")
        pick_boxes = QHBoxLayout()
        pick_boxes.addWidget(self.pick1)
        pick_boxes.addWidget(self.pick2)
        pick_boxes.addWidget(self.pick3)
        pick_boxes.addWidget(self.pick4)
        self.main_layout.addLayout(pick_boxes)
        
        self.guess_label = QLabel(f"Your last guess was: {self.guess}", self)
        self.guess_label.setFont(QFont("monospace", 12))
        self.guess_label.setStyleSheet("color: cyan;"
                                       "font-weight: bold")
        self.guess_label.setAlignment(Qt.AlignCenter)        
        self.main_layout.addWidget(self.guess_label)        

        self.result_label = QLabel("Good luck!", self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setFont(QFont("monospace", 14))
        self.result_label.setStyleSheet("color: cyan;"                          
                           "font-weight: bold")
        self.main_layout.addWidget(self.result_label)

        self.button = QPushButton("Submit", self)        
        self.button.setStyleSheet("font-size: 24px;" 
                                  "font-family: monospace;" 
                                  "color: cyan;" 
                                  "padding: 15px;" 
                                  "margin: 15px 150px")
        self.main_layout.addWidget(self.button)
        
        self.tries_label = QLabel(f"Tries left: {self.tries}", self)
        self.tries_label.setFont(QFont("monospace", 12))
        self.tries_label.setAlignment(Qt.AlignRight)
        self.tries_label.setStyleSheet("color: cyan;"
                                       "margin: 15px;"
                                       "font-weight: bold")        
        self.main_layout.addWidget(self.tries_label)       

        self.play_again = QPushButton("Play Again", self)
        self.play_again.setStyleSheet("font-size: 18px;"
                                      "font-family: monospace;"
                                      "color: cyan;"
                                      "padding: 10px;"
                                      "margin: 10px 300px")
        self.main_layout.addWidget(self.play_again)
        

        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)       
        
        
        self.initUI()
                
    def initUI(self):
        self.button1.clicked.connect(lambda: self.add_pick("Red"))
        self.button2.clicked.connect(lambda: self.add_pick("Blue"))
        self.button3.clicked.connect(lambda: self.add_pick("Green"))
        self.button4.clicked.connect(lambda: self.add_pick("Yellow"))
        self.button5.clicked.connect(lambda: self.add_pick("Orange"))
        self.button6.clicked.connect(lambda: self.add_pick("Purple"))

        self.clear_selection.clicked.connect(self.clear_pick)
        
        self.button.clicked.connect(self.on_submit)

        self.play_again.clicked.connect(self.refresh)

    def on_submit(self):
        if len(self.guess) != 4:
            self.label02.setText(f"You must guess {CODE_LENGTH} colors!")            
            return
        
        self.label02.setText(f"")         
        self.guess_label.setText(f"Your guess before was: {self.guess}")    
        
        correct_pos, incorrect_pos = check_code(self.guess, self.code)
        self.result_label.setText(f"Correct Positions: {correct_pos} Incorect positions: {incorrect_pos}")
        
        if self.tries == 0:
            self.result_label.setText(f"YOU LOST! Code was {self.code}")
            self.setDisabled(True)
        if self.guess != self.code:
            self.tries -= 1
            self.tries_label.setText(f"Tries left: {self.tries}")
            self.guess = []
        if self.guess == self.code:
            self.result_label.setText(f"YOU WON! Code was {self.code}")
            self.setDisabled(True)

    def add_pick(self, color):                
        self.guess.append(color)
        self.pick_label.setText(f"Your pick: {self.guess}")
        for x in range(len(self.guess)):
            if x > len(self.colors) - 1:
                break
            else:
                self.colors[x] = self.guess[x]  
        self.pick1.setStyleSheet(f"background-color: {self.colors[0]};" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 15px 25px")         
        self.pick2.setStyleSheet(f"background-color: {self.colors[1]};" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 15px 25px")         
        self.pick3.setStyleSheet(f"background-color: {self.colors[2]};" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 15px 25px")         
        self.pick4.setStyleSheet(f"background-color: {self.colors[3]};" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 15px 25px")         

    def clear_pick(self):
        self.guess = []
        self.pick_label.setText(f"Your pick:")
        self.colors = ["darkgray", "darkgray", "darkgray", "darkgray"]
        self.pick1.setStyleSheet(f"background-color: {self.colors[0]};" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 15px 25px")         
        self.pick2.setStyleSheet(f"background-color: {self.colors[1]};" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 15px 25px")         
        self.pick3.setStyleSheet(f"background-color: {self.colors[2]};" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 15px 25px")         
        self.pick4.setStyleSheet(f"background-color: {self.colors[3]};" "color: black;" "border-radius: 2px;" "padding: 5px;" "margin: 15px 25px")   

    def refresh(self):
        self.main_layout.update

if __name__ == "__main__":
    # game()                    # terminal game

    # gui game
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())