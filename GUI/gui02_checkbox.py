# GUI - graphical user interface

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QCheckBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checkbox")
        self.setGeometry(700, 300, 500,500)                        
        self.label1 = QLabel("Checkbox", self)
        self.label1.setFont(QFont("Ariel", 40))
        self.label1.setGeometry(0, 0, 500, 100)
        self.label1.setStyleSheet("color: green;" 
                            "background-color: grey;"
                            "font-weight: bold;"
                            "font-style: italic;")
        
        self.label1.setAlignment(Qt.AlignCenter)                       
        
        self.checkbox = QCheckBox("Do you like pizza?", self)

        self.initUI()
        
    def initUI(self):        
        self.button = QPushButton("Click Me!", self)        
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px")
        self.button.clicked.connect(self.on_click)
        
        self.checkbox.setGeometry(20, 50, 500, 200)
        self.checkbox.setStyleSheet("font-size: 25px;"
                                    "font-family:  'Lucida Console', 'Courier New', monospace;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_change)
        
    def checkbox_change(self, state):
        if state == Qt.Checked:
            print("You like pizza!")
        else:
            print("You pineapple guy, right?")


    def on_click(self):
        print("Button clicked!")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)                                       
        self.label1.setText("Goodbye")


def main():
    app = QApplication(sys.argv)                                            
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()