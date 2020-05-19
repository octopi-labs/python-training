'''
NOTE: With composition, we can add very specific functionality to your classes from 
        a specialized, simple class called a mixin
'''
class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

class VolumeMixin(object):
    def volume(self):
        return self.area() * self.height

class Cube(VolumeMixin, Square):
    def __init__(self, length):
        super(Cube, self).__init__(length)
        self.height = length

    def face_area(self):
        return super(Cube, self).area()

    def surface_area(self):
        return super(Cube, self).area() * 6


if __name__ == "__main__":
    cube = Cube(2)
    print(cube.surface_area())
    print(cube.volume())
