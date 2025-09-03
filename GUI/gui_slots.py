import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

def spin_row():
    symbols = ['🍒','🍋','🍓','🍊','🍉','🔔','⭐']
        
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 2
        elif row[0] == '🍋':
            return bet * 3
        elif row[0] == '🍓':
            return bet * 3.5
        elif row[0] == '🍊':
            return bet * 4
        elif row[0] == '🍉':
            return bet * 4.5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = 100    
    print("\nWelcome to Slots")
    print("🍒🍋🍓🍊🍉🔔⭐\n")

    while balance > 0:
        print(f"Current balance: ${balance}")         
        bet = input("Place your bet amount: ")
        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds!")
            continue

        if bet <= 0:
            print("Bet must be greater than zero!")
            continue

        balance -= bet
    
        row = spin_row()
        print("Spining...\n")
        print_row(row)

        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost, try again!")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ")

        if play_again.upper() != "Y":
            print("\nThank you for playing!")            
            break
        
    print(f"\nGame over! Your final balance is ${balance}.\n")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(550, 250, 800,500)                                 
        self.setWindowIcon(QIcon("python/modules/meovv.png"))
        self.label1 = QLabel("Hello", self)
        self.label1.setFont(QFont('Courier New', 40))
        self.label1.setGeometry(0, 0, 500, 100)
        self.label1.setStyleSheet("color: green;" 
                            "background-color: grey;"
                            "font-weight: bold;"
                            "font-style: italic;")
        
        self.label1.setAlignment(Qt.AlignCenter)                            
        self.label2 = QLabel(self)
        self.label2.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("python/modules/meovv.png")
        self.label2.setPixmap(pixmap)
        self.label2.setScaledContents(True)
        self.label2.setGeometry((self.width()- self.label2.width()) // 2,
                           (self.height() - self.label2.height()) // 2, 
                           self.label2.width(), 
                           self.label2.height())
        self.initUI()
        
    def initUI(self):
        central_widgit = QWidget()
        self.setCentralWidget(central_widgit)
        self.button = QPushButton("Click Me!", self)        
        self.button.setGeometry(150, 400, 200, 100)
        self.button.setStyleSheet("font-size: 30px")
        self.button.clicked.connect(self.on_click)

        label01 = QLabel("#1")
        label02 = QLabel("#2")
        label03 = QLabel("#3")
        label04 = QLabel("#4")
        label05 = QLabel("#5")

        label01.setStyleSheet("background-color: red")
        label02.setStyleSheet("background-color: blue")
        label03.setStyleSheet("background-color: green")
        label04.setStyleSheet("background-color: yellow")
        label05.setStyleSheet("background-color: purple")

        grid = QGridLayout()                                               
        grid.addWidget(label01, 0, 2)
        grid.addWidget(label02, 1, 2)
        grid.addWidget(label03, 2, 0)
        grid.addWidget(label04, 2, 1)
        grid.addWidget(label05, 2, 2)

        central_widgit.setLayout(grid)

    def on_click(self):
        print("Button clicked!")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)                                       # leis paspausti tik viena karta
        self.label1.setText("Goodbye")


def main():
    app = QApplication(sys.argv)                                           
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()