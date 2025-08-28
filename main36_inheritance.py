# Inheritance - paveldimumas

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def speek(self):
        print("\tWoof")

class Cat(Animal):
    def speek(self):
        print("\tMeovv")

class Rabbit(Animal):
    def speek(self):
        print("\t...")

dog = Dog("Gucci")
cat = Cat("Mozzi")
rabbit = Rabbit("Bonnie")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speek()
print()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speek()
print()

print(rabbit.name)
print(rabbit.is_alive)
rabbit.eat()
rabbit.sleep()
rabbit.speek()
print()