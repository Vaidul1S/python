import sys
import random
import pygame
from itertools import combinations
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.balance = 100
        self.bet = 0
        self.setWindowTitle("Slots")
        self.setGeometry(550, 250, 850, 520)                                 
        self.setWindowIcon(QIcon("python/modules/slots.png"))        
        self.title_label = QLabel(" 🎰🎰🎰 Slots 🎰🎰🎰", self)
        self.title_label.setGeometry(0, 0, 850, 100)
        self.title_label.setObjectName("title_label")
        self.title_label.setAlignment(Qt.AlignCenter)
                                   
        self.row_label = QLabel("💰 | 💰 | 💰 | 💰 | 💰", self)
        self.row_label.setGeometry(0, 0, 600, 100)
        self.row_label.setObjectName("row_label")
        self.row_label.setGeometry((self.width()- self.row_label.width()) // 2,
                           (self.height() - self.row_label.height()) // 2, 
                           self.row_label.width(), 
                           self.row_label.height())

        self.balance_label = QLabel(f"Current balance: ${self.balance}", self)
        self.balance_label.setGeometry(0, 110, 830, 50)
        self.balance_label.setObjectName("balance_label")
        self.balance_label.setAlignment(Qt.AlignRight)

        self.bet_input = QLineEdit(self)
        self.bet_button = QPushButton("Bet", self)
        self.bet_amount = QLabel(f"Bet amount: {self.bet}", self)
        self.bet_input.setGeometry(730, 350, 100, 30)
        self.bet_button.setGeometry(730, 385, 100, 30)
        self.bet_amount.setGeometry(735, 310, 100, 50)
        self.bet_input.setObjectName("bet_input")
        self.bet_button.setObjectName("bet_button")
        self.bet_amount.setObjectName("bet_amount")
        self.spin_button = QPushButton("Spin!", self)        
        self.spin_button.setGeometry(300, 400, 200, 50)     
        self.spin_button.setObjectName("spin_button")
        self.result_label = QLabel("Good luck!", self)
        self.result_label.setGeometry(200, 300, 400, 50)
        self.result_label.setObjectName("result_label")
        self.result_label.setAlignment(Qt.AlignCenter)
        LEGEND = "Win combos:\n\n🍒🍒🍒  x2\n🍋🍋🍋  x3\n🍓🍓🍓  x3.5\n🍊🍊🍊  x4\n🍉🍉🍉  x4.5\n🔔🔔🔔  x10\n⭐⭐⭐  x20\n\n🍒🍒🍒🍒  x4\n🍋🍋🍋🍋  x6\n🍓🍓🍓🍓  x7\n🍊🍊🍊🍊  x8\n🍉🍉🍉🍉  x9\n🔔🔔🔔🔔  x20\n⭐⭐⭐⭐  x40\n\n🍒🍒🍒🍒🍒  x20\n🍋🍋🍋🍋🍋  x30\n🍓🍓🍓🍓🍓  x35\n🍊🍊🍊🍊🍊  x40\n🍉🍉🍉🍉🍉  x45\n🔔🔔🔔🔔🔔  x50\n⭐⭐⭐⭐⭐  x100\n"
        self.sound_file = "python/modules/bonus.mp3"       
        self.bet_sound = "python/modules/cash-register.mp3"       
        self.game_over = "python/modules/game-over.mp3"       
        self.legend_label = QLabel(LEGEND, self)
        self.legend_label.setGeometry(20, 110, 150, 400)
        self.legend_label.setObjectName("legend_label")
        self.setStyleSheet("""
                        QLabel#title_label{
                            font-family: Verdana;
                            font-size: 46px;
                            font-variant: small-caps;
                            letter-spacing: 16px;
                            color: white; 
                            background-color: darkred;
                            font-weight: bold;
                            }
                        QLabel#row_label{
                            font-size: 50px;
                            border: 4px solid gold;
                            border-radius: 50px;
                            color: gold;
                            padding: 0 0 13 9;
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
                        QLabel#legend_label{
                            font-family: Verdana;
                            font-size: 12px;
                            font-weight: bold;
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
        symbols = ['🍒','🍒','🍒','🍒','🍒','🍒','🍒','🍋','🍋','🍋','🍋','🍋','🍋','🍓','🍓','🍓','🍓','🍓','🍊','🍊','🍊','🍊','🍉','🍉','🍉','🔔','🔔','⭐']
        
        return [random.choice(symbols) for _ in range(5)]
        
    @staticmethod
    def get_payout(row, bet):
        MULTIPLIERS = {
            '🍒': 2,
            '🍋': 3,
            '🍓': 3.5,
            '🍊': 4,
            '🍉': 4.5,
            '🔔': 10,
            '⭐': 20
        }

        for combo in combinations(range(len(row)), 5):
            a, b, c, d, e = combo
            if row[a] == row[b] == row[c] == row[d] == row[e]:
                return bet * 10 * MULTIPLIERS.get(row[a], 0)

        for combo in combinations(range(len(row)), 4):
            a, b, c, d = combo
            if row[a] == row[b] == row[c] == row[d]:
                return bet * 2 * MULTIPLIERS.get(row[a], 0)
            
        for combo in combinations(range(len(row)), 3):
            a, b, c = combo
            if row[a] == row[b] == row[c]:
                return bet * MULTIPLIERS.get(row[a], 0)
        
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
        pygame.mixer.init()
        pygame.mixer.music.load(self.bet_sound)
        pygame.mixer.music.play()


    def on_click(self):
        if self.bet == 0:
            self.result_label.setText("Please make a bet.")
            return
        
        if self.balance - self.bet < 0:
            self.result_label.setText("Insufficient funds!")
            return           
                     
        self.balance -= self.bet
        
        row = self.spin_row()
        self.result_label.setText("Spining...")
        self.row_label.setText(str(" | ".join(row)))        
        payout = self.get_payout(row, self.bet)
            
        if payout > 0:
            pygame.mixer.init()
            pygame.mixer.music.load(self.sound_file)
            pygame.mixer.music.play()
            self.result_label.setText(f"You won ${payout}")
        else:
            self.result_label.setText("Sorry you lost, try again!")

        self.balance += payout

        self.balance_label.setText(f"Current balance: ${self.balance}")
        self.spin_button.setText("Spin again!")

        if self.balance == 0:
            self.balance_label.setText(f"Current balance: ${self.balance}")
            self.result_label.setText("Sorry you lost all your money!")
            self.spin_button.setText("Gamer over!")  
            pygame.mixer.init()
            pygame.mixer.music.load(self.game_over)
            pygame.mixer.music.play()      
            self.spin_button.setEnabled(False)
            self.bet_button.setEnabled(False)

def main():
    app = QApplication(sys.argv)                                           
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()