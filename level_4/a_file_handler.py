"""
У нас есть класс FileHandler, который может считывать файлы, но не всегда в удобном для нас виде.
Поэтому мы создали два его наследника: CSVHandler и JSONHandler

Задания:
    1. Переопределите метод read у CSVHandler и JSONHandler
    2. Метод read у JSONHandler должен возвращать словарь. Для этого используйте модуль встроенный модуль json
    3. Метод read у CSVHandler должен возвращать список словарей. Для этого используйте модуль встроенный модуль csv
    4. Создайте экземпляры каждого из трех классов.
       С помощью экземпляра FileHandler прочитайте и распечатайте содержимое файла text.txt
       С помощью экземпляра JSONHandler прочитайте и распечатайте содержимое файла recipes.json
       С помощью экземпляра CSVHandler прочитайте и распечатайте содержимое файла user_info.csv

"""

import csv
import json


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return file.read()


class JSONHandler(FileHandler):
    def read(self):
        with open(self.filename, "r", encoding="utf-8") as json_file:
            return json.load(json_file)


class CSVHandler(FileHandler):
    def read(self):
        with open(self.filename, "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            list_of_users = []
            for row in reader:
                list_of_users.append(row)
            return list_of_users


if __name__ == "__main__":
    text_file = FileHandler("data/text.txt")
    print(text_file.read())
    print()
    recipes_file = JSONHandler("data/recipes.json")
    print(recipes_file.read())
    print()
    user_info_file = CSVHandler("data/user_info.csv")
    print(user_info_file.read())
