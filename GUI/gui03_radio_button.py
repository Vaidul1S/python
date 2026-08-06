# GUI - graphical user interface

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QRadioButton, QButtonGroup
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio Button")
        self.setGeometry(700, 300, 500,500)                        
        self.label1 = QLabel("Choose you payment method: ", self)
        self.label1.setFont(QFont("Ariel", 20))
        self.label1.setGeometry(0, 0, 500, 100)
        self.label1.setStyleSheet("color: green;" 
                            "background-color: grey;"
                            "font-weight: bold;"
                            "font-style: italic;")
        
        self.label1.setAlignment(Qt.AlignCenter)                       
        
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("American Express", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)

        self.button_group1 = QButtonGroup()                                         # visi radio default vienoj grupej, jei nori isskirtyti sukuriam atskiras grupes
        self.button_group2 = QButtonGroup()

        self.initUI()
        
    def initUI(self):        
        self.radio1.setGeometry(10, 100, 300, 50)
        self.radio2.setGeometry(10, 150, 300, 50)
        self.radio3.setGeometry(10, 200, 300, 50)
        self.radio4.setGeometry(10, 300, 300, 50)
        self.radio5.setGeometry(10, 350, 300, 50)

        self.setStyleSheet("QRadioButton{"
                           "font-size: 25px;"
                           "font-family: 'Lucida Console', 'Courier New', monospace;"
                           "}")
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)
    
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected!")


def main():
    app = QApplication(sys.argv)                                            
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()