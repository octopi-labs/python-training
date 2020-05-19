class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Are of Rectangle")
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    
    def area(self):
        print("Area of a square")
        # return self.length * self.length
        area = super().area()
        return area - 1

class Cube(Square):
    def surface_area(self):
        face_area = super(Cube, self).area()
        return face_area * 6

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length


if __name__ == "__main__":
    square = Square(6)
    print("Area of a square: ", square.area())
    print("Perimeter of a square: ", square.perimeter())
    
    cube = Cube(3)
    print("Area of a cube", cube.area())
    print("Surface Area of a cube: ", cube.surface_area())
    print("Volume of a cube: ", cube.volume())
    
    

"""
Create a shape class which has a property number_of_sides
Create Triangle class which inherits Shape class. Define Area of triangle
Create Rectangle class which inherits Shape class. Define Area of Rectangle
Create Square class which inherits Rectangle class. 
Create Circle class which inherits Shape class. 
Define Area and perimeter of circle.

Print number of sides, area of each object and Perimeter of Circle object
"""