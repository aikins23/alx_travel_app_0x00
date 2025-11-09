# from abc import ABC, abstractmethod
#
# class shape:
#     @abstractmethod
#     def area(self):
#         pass
#
# class circle(shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14*self.radius**2
#
# class square(shape):
#     def __init__(self, side):
#         self.side = side
#     def area(self):
#         return self.side**2
#
# class triangle(shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return self.base*self.height*0.5
#
#
# shapes =[circle(5), square(6), triangle(8,5)]
#
# for shape in shapes:
#     print(f"The area is {shape.area()}cm²")

#
# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B, C):
#     pass
#
#
# print(D.mro())


class Church_members:
    count = 0
    total_age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Church_members.count += 1
        Church_members.total_age += age

    def get_info(self):
        return f"{self.name} is {self.age} years old."

    @classmethod
    def get_count(cls):
        return f"there are {cls.count} total church members"

    @classmethod
    def get_Average_age(cls):
        if cls.total_age == 0:
            return f"There are no registered chruch members."
        else:
            return f"average age of {cls.count} church members is {cls.total_age/cls.count} years old."


member1 = Church_members("Kofi", 10)
member2 = Church_members("Ama", 50)
member3 = Church_members("Kwame", 30)
member4 = Church_members("Akua", 25)
member5 = Church_members("Yaw", 40)
member6 = Church_members("Esi", 15)
member7 = Church_members("Kojo", 60)
member8 = Church_members("Adwoa", 35)
member9 = Church_members("Kwabena", 45)
member10 = Church_members("Abena", 20)
member11 = Church_members("Afriyie", 55)
member12 = Church_members("Mensah", 70)
member13 = Church_members("Serwaa", 28)
member14 = Church_members("Boakye", 33)
member15 = Church_members("Naana", 48)



print(Church_members.get_count())
print(Church_members.get_Average_age())