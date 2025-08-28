# Weather App

import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(800, 300, 400, 100)
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)


        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setWindowIcon(QIcon("python/modules/sun.png"))

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                           font-family: calibri;
                           }
            QLabel#city_label{
                           font-size: 40px;
                           font-style: italic;}
            QLineEdit#city_input{
                           border-radius: 15px;
                           font-size: 40px;}
            QPushButton#get_weather_button{
                           background-color: green;
                           border-radius: 15px;
                           font-size: 30px;
                           font-weight: bold;
                           }
            QPushButton#get_weather_button:hover{
                           background-color: lime;}
            QLabel#temp_label{
                           font-size: 60px;}
            QLabel#emoji_label{
                           font-size: 70px;
                           font-family: Segoe UI emoji;}
            QLabel#description_label{
                           font-size: 50px;}
                           """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "bd5e378503939ddaee76f12ad7a97608"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("Bad requset!\nPlease check your input!")
                case 401:
                    self.display_error("Unauthorized\nInvalid API key!")
                case 403:
                    self.display_error("Forbiddeb\nAccess is denied!")
                case 404:
                    self.display_error("Not found\nCity not found!")
                case 500:
                    self.display_error("Internal Server Error\nPlease try again later!")
                case 502:
                    self.display_error("Bad Gateway\nInvalid response form the server!")
                case 503:
                    self.display_error("Servise Unavailable\nServer is dowm!")
                case 504:
                    self.display_error("Gateway Timeout\nNo response from the server!")
                case _:
                    self.display_error(f"HTTP error occored\n{response.status_code}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection error\nCheck your internet connection!")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error\nThe request timed out!")

        except requests.exceptions.TooManyRedirects:
            self.display_error("To many Redirects\nCheck the URL!")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error/n{req_error}")   

    def display_error(self, message):
        self.temp_label.setStyleSheet("font-size: 30px;")
        self.temp_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temp_label.setStyleSheet("font-size: 60px;")
        temp_K = data["main"]["temp"]
        temp_C = temp_K - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        self.description_label.setText(weather_description)
        self.emoji_label.setText(self.get_emoji(weather_id))
        self.temp_label.setText(f"{temp_C:.01f}ºC")

    @staticmethod
    def get_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "🌨️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id <= 762:
            return "🌋"
        elif weather_id <= 774:
            return "💨"
        elif weather_id <= 781:
            return "🌪️"
        elif weather_id <= 800:
            return "🌞"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()                                            
    sys.exit(app.exec_())     