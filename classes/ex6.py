from ex45 import Square

class Triangle(object):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        # super().__init__()

    def tri_area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area
    
    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area


if __name__ == "__main__":
    pyramid = RightPyramid(2, 4)
    print(RightPyramid.__mro__)
    print(pyramid.area())