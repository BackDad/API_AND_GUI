
import requests  # Импорт библиотеки requests для выполнения HTTP-запросов
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPlainTextEdit, QPushButton

class WeatherWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()  # Создание вертикального макета
        self.setLayout(self.layout)  # Установка макета для виджета

        self.result_text = QPlainTextEdit()  # Создание текстового поля для вывода результатов
        self.layout.addWidget(self.result_text)  # Добавление текстового поля в макет

        self.update_button = QPushButton("Обновить")  # Создание кнопки "Обновить"
        self.layout.addWidget(self.update_button)  # Добавление кнопки в макет
        self.update_button.clicked.connect(self.update_weather)  # Подключение обработчика события клика на кнопку

    def update_weather(self):
        api_key = 'your api key'
        city = 'Voronezh'

        # Выполняем запрос к API для получения актуального прогноза погоды
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)  # Выполнение GET-запроса по указанному URL
        data = response.json()  # Преобразование ответа в формате JSON в словарь Python

        # Обновляем текстовое поле с результатами
        self.result_text.clear()  # Очистка текстового поля
        if response.status_code == 200:  # Проверка успешности запроса (код 200 означает успешный запрос)
            self.result_text.appendPlainText(f"Город: {city}")
            self.result_text.appendPlainText(f"Температура: {data['main']['temp']}°C")
            self.result_text.appendPlainText(f"Описание: {data['weather'][0]['description']}")
        else:
            self.result_text.appendPlainText("Ошибка при получении погоды")

if __name__ == '__main__':
    app = QApplication([])  # Создание экземпляра QApplication
    widget = WeatherWidget()  # Создание экземпляра WeatherWidget
    widget.show()  # Отображение виджета на экране
    app.exec_()  # Запуск главного цикла приложения