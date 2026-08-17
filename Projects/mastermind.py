import random
# lets make GUI
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

COLORS = ["R","B","G","Y","W","O"]
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

        self.setWindowTitle("Mastermind")
        self.setGeometry(700, 300, 600,400)
        self.label01 = QLabel(f"You have {TRIES} tries to guess the code of {CODE_LENGTH} colors.", self)
        self.label01.setFont(QFont("monospace", 12))
        self.label01.setGeometry(50, 10, 500, 30)
        self.label01.setStyleSheet("color: cyan;"                                  
                            "font-weight: bold;")
        
        self.label02 = QLabel(f"The valid colors are {COLORS}", self)
        self.label02.setFont(QFont("monospace", 12))
        self.label02.setGeometry(50, 40, 500, 30)
        self.label02.setStyleSheet("color: cyan;"                                  
                            "font-weight: bold;")
        
        self.guess_input = QLineEdit(self)
        self.guess_input.setGeometry(210, 90, 200, 30)

        self.result_label = QLabel("Good luck!", self)
        self.result_label.setGeometry(240, 130, 200, 30)
        self.result_label.setFont(QFont("monospace", 16))
        self.result_label.setStyleSheet("color: cyan;"                           
                           "font-weight: bold")
        self.code = generate_code()
        self.guess = self.guess_input.text()


        self.initUI()
                
    def initUI(self):
        
        self.button = QPushButton("Submit", self)        
        self.button.setGeometry(250, 200, 120, 50)
        self.button.setStyleSheet("font-size: 24px")
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        correct_pos, incorrect_pos = check_code(self.guess, self.code)
        self.result_label.setText(f"Correct Positions: {correct_pos} Incorect positions: {incorrect_pos}")


if __name__ == "__main__":
    # game()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())