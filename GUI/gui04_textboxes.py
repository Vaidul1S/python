# Text boxes - QLineEdit

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500,500)                        
        self.setWindowIcon(QIcon("python/modules/meovv.png"))
        self.label1 = QLabel("Hello", self)
        self.label1.setFont(QFont("Ariel", 40))
        self.label1.setGeometry(0, 0, 500, 100)
        self.label1.setStyleSheet("color: green;" 
                            "background-color: grey;"
                            "font-weight: bold;"
                            "font-style: italic;")
        self.label1.setAlignment(Qt.AlignCenter)                       
        
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)

        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 110, 200, 50)
        self.button.setGeometry(210, 110, 100, 50)
        self.line_edit.setStyleSheet("font-size: 18px;"
                                     "font-family: 'Lucida Console', 'Courier New', monospace;")
        self.line_edit.setPlaceholderText("Enter your name")
        self.button.setStyleSheet("font-size: 20px;"
                                     "font-family: 'Lucida Console', 'Courier New', monospace;")
        self.button.clicked.connect(self.submit)
        
    def submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}")

def main():
    app = QApplication(sys.argv)                                            
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()