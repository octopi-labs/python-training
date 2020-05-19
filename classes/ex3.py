
# IS-A
# HAS-A


class Animal(object):

    def __init__(self, legs, tail):
        self.legs = legs
        self.tail = tail

    def bark(self):
        pass

    def is_pet(self):
        return "PET: {0}".format(False)


class Dog(Animal):

    def bark(self):
        return "Bho! Bho!"

    def is_friendly(self):
        return True


class Cat(Animal):

    def bark(self):
        return "Meon! Meon!"

    def is_thief(self):
        return True

class GermanShepherd(Dog):

    def is_strong(self):
        return True

if __name__ == "__main__":
    animal = Animal(2, 3)
    dog = Dog(4, 1)
    cat = Cat(4, 1)

    print(dog.bark())
    print(cat.bark())

    print(dog.is_friendly())
    print(cat.is_thief())

    print(animal.bark())
    print(animal.legs)
    print(dog.legs)
    print(dog.is_pet())

    gs = GermanShepherd(4, 1)
    print(gs.bark())
    print(gs.is_friendly())
    print(gs.is_strong())

