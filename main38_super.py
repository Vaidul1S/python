# Super - super() function - paveldeto konstruktoriaus ar metodo(funkcijos) papildymui'ish

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius} cm2")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        print(f"It is a square with an area of {self.width * self.width} cm2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f"It is a triangle with an area of {(self.width * self.height)/2} cm2")
        super().describe()


circle = Circle("red", False, 7)
print(f"Circle: {circle.color} {circle.is_filled} {circle.radius}")
circle.describe()
print()

square = Square("blue", True, 9)
print(f"Square: {square.color} {square.is_filled} {square.width}")
square.describe()
print()

triangle = Triangle("green", True, 7, 15)
print(f"Triangle: {triangle.color} {triangle.is_filled} {triangle.width} {triangle.height}")
triangle.describe()