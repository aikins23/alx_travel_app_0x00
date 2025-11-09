
#creating and intializing class
class Dog():
    def __init__(self,name,bred):
        self.name = name
        self.bred = bred
    def bark(self):
        return "WOOF"
#creating objects
dog1=Dog("Peace", "Ghana Dog")
dog2=Dog("James", "German Sheperd")
#accessing properties and methods
print(f"{dog1.name} is {dog1.bred} and it says {dog1.bark()}")
print(f"{dog2.name} is {dog2.bred} and it says {dog2.bark()}")