# GUI - graphical user interface

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500,500)                                 # setGeometry(x,y, width,height)
        self.setWindowIcon(QIcon("python/modules/meovv.png"))
        self.label1 = QLabel("Hello", self)
        self.label1.setFont(QFont("Ariel", 40))
        self.label1.setGeometry(0, 0, 500, 100)
        self.label1.setStyleSheet("color: green;" 
                            "background-color: grey;"
                            "font-weight: bold;"
                            "font-style: italic;")
        
        self.label1.setAlignment(Qt.AlignCenter)                            # AlignVCenter, AlignHCenter, AlignTop, AlignBottom, AlignRight, AlignLeft, galim ir poruot per '|'
        self.label2 = QLabel(self)
        self.label2.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("python/modules/meovv.png")
        self.label2.setPixmap(pixmap)
        self.label2.setScaledContents(True)
        
        self.initUI()
        
    def initUI(self):
        central_widgit = QWidget()
        self.setCentralWidget(central_widgit)
        self.button = QPushButton("Click Me!", self)        
        self.button.setGeometry(150, 200, 200, 100)
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

        # vbox = QVBoxLayout()                                               # QVBoxLayout or QHBoxLayout
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)

        # central_widgit.setLayout(vbox)

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
    app = QApplication(sys.argv)                                            # argv - arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()