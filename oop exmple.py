class Shapes:
    def __init__(self, name, side):
        self.name = name
        self.side = side

    def Area(self):
        print("I am a: " + self.name + "\n" +
              "I have " + self.side + "sides")

obj_shape = Shapes("shape", "so many ")
obj_shape.Area()


class Rectangle(Shapes):
    def __init__(self, len1, wid1):
        self.length = len1
        self.width = wid1

    def Area(self):
        result = self.length * self.width
        return result

obj_book = Rectangle(10, 7)
obj_screen = Rectangle(5, 7)
print("The Area of a book is " + str(obj_book.Area()))
print("The Area of screen is " + str(obj_screen.Area()))

class Circle(Shapes):
    def __init__(self, rad1):
        self.radius = rad1

    def Area(self):
        import math
        result = math.pi * self.radius * self.radius
        return result

obj_plate = Circle(12)
print("the Area of the plate is %.0f" % + obj_plate.Area())


class Triangle(Shapes):
    def __init__(self, base, high):
        self.base = base
        self.height = high

    def Area(self):
        result = 0.5 * self.base * self.height
        return result

obj_flag = Triangle(12, 4)
print("The Area of the flag is " + str(obj_flag.Area()))
