# Stopwatch

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTime, QTimer

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setGeometry(800, 400, 400, 100)
        self.setWindowIcon(QIcon("python/modules/stop.jpeg"))
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
                
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)

        
        self.setStyleSheet("""
                           QPushButton, QLabel{
                                font-family: calibri;
                                background-color: black;
                           }
                           QPushButton{
                                font-size: 25px;
                                border-radius: 15px;
                                color: red;
                           }
                           QLabel{
                                font-size: 50px;
                                color: blue;
                                border-radius: 15px;
                           }""")
        
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

        # self.timer.timeout.connect(self.update_time)
        # self.timer.start(1000)

        # self.update_time()
    
    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch_app = StopWatch()
    stopwatch_app.show()                                            
    sys.exit(app.exec_())                                   