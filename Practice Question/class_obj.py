class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello my name is", self.name)

person1= Person("Moon", 22)
person1.greet()