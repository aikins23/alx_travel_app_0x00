# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#         print("Constructor created")
#
#     def __del__(self):
#         print(f"Goodbye {self.name}")
#
# p1 = person("Emmanuel", 21)
#
#
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return (f"Book {self.title} by {self.author} with {self.pages} pages")
#
#     def __repr__(self):
#         return f"Book('{self.title}', '{self.author}', {self.pages})"
#
# book1 = Book("The Pragmatic Programmer", "Andrew Hunt", 352)
# book2 = Book("Clean Code", "Robert C. Martin", 464)
# book3 = Book("Python Crash Course", "Eric Matthes", 544)
#
#
# print(book1)
# book2
# print(repr(book3))


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age 