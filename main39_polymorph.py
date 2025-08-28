# Polymorphism - inheritance and 'duck typing'

# inheritance

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
    def area(self):
        return (self.side_a * self.side_b) / 2
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)


shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepperoni", 22)]

for shape in shapes:
    print(f"{shape.area()} cm2")


# duck typing - if it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car:                                                          # it quacks
    alive = False
    def speak(self):
        print("Honk!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)