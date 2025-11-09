class Animal:
    alive = True
    def sleep(self, name):
        self.name = name
        print(f"this {name} is Sleeping")
    def eat(self, name):
        self.name = name
        print(f"this {name} is Eating")

class Dog(Animal):
    pass
class Cat(Animal):
    pass

print(Dog.alive)

dog = Dog()
cat = Cat()

dog.sleep("Dog")
cat.eat("cat")