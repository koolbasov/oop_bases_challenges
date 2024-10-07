"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, name: str, description: str, price: float, weight: float):
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight


if __name__ == "__main__":
    buckwheat = Product(name="Крупа гречневая", description="Гречка в собственном соку", price=99.99, weight=0.9)
    print(f"Информация о продукте: {buckwheat.name}, {buckwheat.description}, {buckwheat.price}, {buckwheat.weight}")
