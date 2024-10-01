"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def summarize(self):
        return f"Total text length: {len(self.text)}"


class AdvancedTextProcessor(TextProcessor):
    def summarize(self):
        words = self.text.split()
        return super().summarize() + f", total number of words in the text: {len(words)}"


if __name__ == "__main__":
    text = "Total text length: 67, total number of words in the text: 10"
    new_document1 = TextProcessor(text)
    print(new_document1.to_upper())
    print(new_document1.summarize())
    print()
    new_document2 = AdvancedTextProcessor(text)
    print(new_document2.to_upper())
    print(new_document2.summarize())
