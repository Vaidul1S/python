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

def play_slots():
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
        self.label1 = QLabel("Slots", self)
        self.label1.setFont(QFont('Courier New', 40))
        self.label1.setGeometry(0, 0, 800, 100)
        self.label1.setStyleSheet("color: green;" 
                            "background-color: darkred;"
                            "font-weight: bold;"                           
                            "font-style: italic;")
        
        self.label1.setAlignment(Qt.AlignCenter)                            
        self.label2 = QLabel(self)
        self.label2.setGeometry(0, 0, 250, 250)

        self.label2.setScaledContents(True)
        self.label2.setGeometry((self.width()- self.label2.width()) // 2,
                           (self.height() - self.label2.height()) // 2, 
                           self.label2.width(), 
                           self.label2.height())
        self.initUI()
        
    def initUI(self):
        central_widgit = QWidget()
        self.setCentralWidget(central_widgit)
        self.button = QPushButton("Spin!", self)        
        self.button.setGeometry(300, 400, 200, 60)
        self.button.setStyleSheet("font-size: 30px;"
                                  "background-color: darkred;"
                                  "border-radius: 15px;")
        self.button.clicked.connect(self.on_click)
       
       
    def on_click(self):
        self.button.setText("Spin again!")
        self.label1.setText("Goodbye")


def main():
    app = QApplication(sys.argv)                                           
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()