# class Book:
#     counter = 0
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         Book.counter += 1
#
#
#     @classmethod
#     def get_count(cls):
#         return f"You have {cls.counter} books."
#
# book1 = Book("THE CODES", "KOFI EMMA")
# book2 = Book("PYTHON MADE SIMPLE", "AMA BOATENG")
# book3 = Book("THE HOLY PATH", "KWAME MENSAH")
# book4 = Book("DATA AND LOGIC", "ESI ADU")
# book5 = Book("THE POWER OF DESIGN", "KOJO BAAH")
# book6 = Book("ALGORITHMS IN ACTION", "ADWOA OWUSU")
# book7 = Book("FAITH AND PURPOSE", "YAW ASARE")
# book8 = Book("THE DIGITAL MIND", "ABENA AGYEMAN")
# book9 = Book("CREATIVE THINKING", "KWABENA OSEI")
# book10 = Book("THE ART OF TEACHING", "AKUA DANQUAH")
# book11 = Book("LEADERSHIP GUIDE", "AFRIYIE BOAKYE")
# book12 = Book("MATHS FOR LIFE", "MENSAH KWAKU")
# book13 = Book("SCIENCE AND YOU", "SERWAA ANTWI")
# book14 = Book("MODERN COMPUTING", "BOAKYE KOFI")
# book15 = Book("THE FUTURE OF AI", "NAANA DARKO")
#
# print(Book.get_count())

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b


print(Calculator.add(5,5))
print(Calculator.subtract(5,5))