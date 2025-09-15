import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(550, 250, 800,500)                                 
        self.setWindowIcon(QIcon("python/modules/meovv.png"))        
        self.title_label = QLabel("Slots", self)
        self.title_label.setFont(QFont("arial", 40))
        self.title_label.setGeometry(0, 0, 800, 100)
        self.title_label.setStyleSheet("color: green;" 
                            "background-color: darkred;"
                            "font-weight: bold;"                           
                            "font-style: italic;")
        
        self.title_label.setAlignment(Qt.AlignCenter)
                                   
        self.row_label = QLabel("💰 | 💰 | 💰", self)
        self.row_label.setFont(QFont("monospace", 40)) 
        self.row_label.setGeometry(0, 0, 600, 300)
        self.row_label.setScaledContents(True)
        self.row_label.setGeometry((self.width()- self.row_label.width()) // 2,
                           (self.height() - self.row_label.height()) // 2, 
                           self.row_label.width(), 
                           self.row_label.height())
        self.row_label.setAlignment(Qt.AlignCenter)

        self.balance_label = QLabel("Balance:", self)
        self.balance_label.setGeometry(0, 100, 300, 50)
        self.balance_label.setAlignment(Qt.AlignRight)


        
        self.initUI()

    @staticmethod
    def spin_row():
        symbols = ['🍒','🍋','🍓','🍊','🍉','🔔','⭐']
        
        return [random.choice(symbols) for _ in range(3)]
        
    @staticmethod
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
    
    @staticmethod
    def play_slots(self):
        balance = 100    
        print("\nWelcome to Slots")
        print("🍒🍋🍓🍊🍉🔔⭐\n")

        while balance > 0:
            self.balance_label.setText(f"Current balance: ${balance}")
                     
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
        
            row = self.spin_row()
            print("Spining...\n")
            

            payout = self.get_payout(row, bet)
            
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
        row = self.spin_row()
        self.row_label.setText(str(" | ".join(row)))
        self.button.setText("Spin again!")
        self.title_label.setText("Goodbye")


def main():
    app = QApplication(sys.argv)                                           
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()