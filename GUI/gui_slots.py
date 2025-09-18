import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.balance = 100
        self.bet = 0
        self.setWindowTitle("Slots")
        self.setGeometry(550, 250, 800,500)                                 
        self.setWindowIcon(QIcon("python/modules/slots.png"))        
        self.title_label = QLabel("Slots", self)
        self.title_label.setGeometry(0, 0, 800, 100)
        self.title_label.setObjectName("title_label")
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

        self.balance_label = QLabel(f"Current balance: ${self.balance}", self)
        self.balance_label.setGeometry(0, 110, 780, 50)
        self.balance_label.setObjectName("balance_label")
        self.balance_label.setAlignment(Qt.AlignRight)

        self.bet_input = QLineEdit(self)
        self.bet_button = QPushButton("Bet", self)
        self.bet_amount = QLabel(f"Bet amount: {self.bet}", self)
        self.bet_input.setGeometry(680, 350, 100, 30)
        self.bet_button.setGeometry(680, 385, 100, 30)
        self.bet_amount.setGeometry(685, 310, 100, 50)
        self.bet_input.setObjectName("bet_input")
        self.bet_button.setObjectName("bet_button")
        self.bet_amount.setObjectName("bet_amount")
        self.spin_button = QPushButton("Spin!", self)        
        self.spin_button.setGeometry(300, 400, 200, 50)     
        self.spin_button.setObjectName("spin_button")
        self.result_label = QLabel("Good luck!", self)
        self.result_label.setGeometry(250, 300, 300, 50)
        self.result_label.setObjectName("result_label")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
                        QLabel#title_label{
                            font-family: Verdana;
                            font-size: 46px;
                            font-variant: small-caps;
                            letter-spacing: 20px;
                            color: white; 
                            background-color: darkred;
                            font-weight: bold;                          
                            }
                        QLabel#balance_label, #result_label{
                            font-family: Verdana;
                            font-size: 20px;
                            }
                        QLineEdit#bet_input{
                            font-size: 14px;
                            border-radius: 15px;
                            border: 1px solid black;
                            padding: 5px 15px; 
                            }
                        QLabel#bet_amount{
                            font-family: Verdana;
                            font-size: 12px;
                            }
                        QPushButton#bet_button{
                            font-family: Verdana;
                            font-size: 16px;
                            border-radius: 15px;
                            background-color: darkgreen;
                            color: white;
                            padding: 5px 15px; 
                            font-weight: bold;
                            }
                        QPushButton#bet_button:hover{
                            background-color: lime;
                            }
                        QPushButton#spin_button{
                            font-family: Verdana;
                            font-size: 30px;
                            background-color: darkred;
                            color: white;
                            border-radius: 15px;
                            }
                        QPushButton#spin_button:hover{
                            background-color: red;
                            }
            """)
        
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
   
    def initUI(self):
        self.bet_button.clicked.connect(self.make_a_bet)
        self.spin_button.clicked.connect(self.on_click)
        
       
    def make_a_bet(self):
        self.bet = self.bet_input.text()
        if not self.bet.isdigit():
            self.result_label.setText("Please enter a valid number")
            return
            
        self.bet = int(self.bet)

        if self.bet > self.balance:
            self.result_label.setText("Insufficient funds!")
            return

        if self.bet <= 0:
            self.result_label.setText("Bet must be greater than zero!")
            return
        self.bet_amount.setText(f"Bet amount: {self.bet}")


    def on_click(self):
        if self.bet == 0:
            self.result_label.setText("Please make a bet.")
            return
                                
        self.balance -= self.bet
        
        row = self.spin_row()
        self.result_label.setText("Spining...")
        self.row_label.setText(str(" | ".join(row)))        
        payout = self.get_payout(row, self.bet)
            
        if payout > 0:
            self.result_label.setText(f"You won ${payout}")
        else:
            self.result_label.setText("Sorry you lost, try again!")

        self.balance += payout

        self.balance_label.setText(f"Current balance: ${self.balance}")
        self.spin_button.setText("Spin again!")

        if self.balance <= 0:
            self.balance_label.setText(f"Current balance: ${self.balance}")
            self.result_label.setText("Sorry you lost all your money!")
            self.spin_button.setText("Gamer over!")        
            self.spin_button.setEnabled(False)
            self.bet_button.setEnabled(False)

def main():
    app = QApplication(sys.argv)                                           
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()