"""
Напишите класс Logger, имеющий следующие методы:

- __init__(self, filename): конструктор, принимающий имя файла, в который будет производиться запись логов;
- __call__(self, message): магический метод, который позволяет использовать объект класса Logger как функцию,
принимающую сообщение и записывающую его в файл.
"""


class Logger:
    def __init__(self, filename, mode='w'):
        self.filename = filename
        self.mode = mode

    def __call__(self, message):
        self.message = message
        return self.message
        


# код для проверки 
logger = Logger("log.txt")
logger("This is a test message.")
