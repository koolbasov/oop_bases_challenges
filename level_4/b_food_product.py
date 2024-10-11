"""
У нас есть класс Product, который подходит для многих продуктов, но не для еды.
В пищевом продукте нам нужно хранить еще срок годности, который будет влиять и на другие методы

Задания:
    1. Переопределите частично метод __init__ у FoodProduct так, чтобы там хранилось еще свойство expiration_date.
       Используйте super() для этого.
    2. Переопределите у FoodProduct полностью метод get_full_info, чтобы он возвращал еще и информацию о сроке годности
    3. Переопределите частично метод is_available у FoodProduct, чтобы там учитывался еще и срок годности. Если он
       меньше чем текущая дата - то is_available должен возвращать False. Используйте super() для этого.
    3. Создайте экземпляры каждого из двух классов и вызовите у них все доступные методы
"""

from datetime import datetime


class Product:
    def __init__(self, title, quantity):
        self.title = title
        self.quantity = quantity

    def get_full_info(self):
        return f"Product {self.title}, {self.quantity} in stock."

    def is_available(self):
        return self.quantity > 0


class FoodProduct(Product):
    def __init__(self, title, quantity, expiration_date):
        super().__init__(title, quantity)
        self.expiration_date = expiration_date

    def get_full_info(self):
        return f"Product {self.title}, {self.quantity} in stock, expiration_date: {self.expiration_date}."

    def is_available(self):
        if self.expiration_date.date() < datetime.now().date():
            return False
        return super().is_available()


if __name__ == "__main__":
    product1 = Product('Apple MacBook Pro 14" (M3 Max 16C CPU, 40C GPU, 2023) 128 ГБ, 4 ТБ SSD, «чёрный космос»', 10)
    print(product1.get_full_info())
    print(product1.is_available())
    print()
    product2 = Product(
        'Ноутбук Apple MacBook Pro 16" (M1 Pro, 16 Gb, 512Gb SSD) Серый космос (MK183) Русифицированный', 0
    )
    print(product2.get_full_info())
    print(product2.is_available())
    print()
    food_product1 = FoodProduct("Молоко ультрапастеризованное с крышкой 3,1-3,2%, 1л", 20, datetime(2024, 10, 20))
    print(food_product1.get_full_info())
    print(food_product1.is_available())
    print()
    food_product2 = FoodProduct(
        'Яйцо куриное "Деревенские напевы" Отборное фасованное, 10шт', 20, datetime(2024, 10, 9)
    )
    print(food_product2.get_full_info())
    print(food_product2.is_available())
    print()
    food_product3 = FoodProduct('Сметана "Хуторок" 15%, 300г', 0, datetime(2024, 10, 25))
    print(food_product3.get_full_info())
    print(food_product3.is_available())
