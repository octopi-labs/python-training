
"""
We need to do two things to fix this:

1. All methods that are called with super() need to have a call to 
    their superclass’s version of that method. 
    This means that you will need to add super().__init__() to the .__init__() methods of 
    Triangle and Rectangle.

2. Redesign all the .__init__() calls to take a keyword dictionary.
"""

class Rectangle(object):
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        print("In Rectangle class")
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length, **kwargs):
        # print(**kwargs)
        super().__init__(length=length, width=length, **kwargs)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

class Triangle(object):
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super(Square, self).__init__(base=base, **kwargs)

    def area(self):
        base_area = super().area()
        print("Base of RightPyramid:", base_area)
        perimeter = super().perimeter()
        print(perimeter)
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        print(base_area)
        triangle_area = super().tri_area()
        print(triangle_area)
        return triangle_area * 4 + base_area


if __name__ == "__main__":
    pyramid = RightPyramid(**{"base": 1, "slant_height":2})
    print(RightPyramid.__mro__)
    print(pyramid.area())
    print(pyramid.area_2())