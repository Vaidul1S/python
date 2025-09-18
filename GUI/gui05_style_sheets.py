# Text boxes - QLineEdit

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Style Sheets")
        self.setWindowIcon(QIcon("python/modules/meovv.png"))
                             
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        

        self.initUI()

    def initUI(self):
        central_widgit = QWidget()
        self.setCentralWidget(central_widgit)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        central_widgit.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{
                           font-size: 20px;
                           font-family: Arial;
                           padding: 15px 75px;
                           margin: 25px;
                           border: 2px solid;
                           border-radius: 15px;
                           }
            QPushButton#button1{
                           background-color: red;
                           }
            QPushButton#button2{
                           background-color: green;
                           }
            QPushButton#button3{
                           background-color: blue;
                           }
            QPushButton#button1:hover{
                           background-color: pink;
                           }
            QPushButton#button2:hover{
                           background-color: lime;
                           }
            QPushButton#button3:hover{
                           background-color: cyan;
                           }
        """)

def main():
    app = QApplication(sys.argv)                                            
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()