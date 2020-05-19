## This is an Animal class inheriting default object
class Animal(object):
    def __init__(self, name):
        self.name = name

## This is a Dog class inheriting Animal class (IS-A)
class Dog(Animal):
    def __init__(self, name):
        ## Property of the Dog class / Dog object (HAS-A)
        self.name = name

## Cat class inheriting Animal class (IS-A)
class Cat(Animal):
    def __init__(self, name):
        ## Property of the Cat class / Cat object (HAS-A)
        self.name = name

## Person class inheriting default object (IS-A)
class Person(object):
    def __init__(self, name):
        ## Property of Person object (HAS-A)
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Employee class inheriting Person class (IS-A)
class Employee(Person):
    def __init__(self, name, salary):
        ## Create an object of Parent class of Employee, i.e. 
        ## Person and call it's initializer
        super(Employee, self).__init__(name)
        ## Property of employee class
        self.salary = salary

## Fish class which inherites object
class Fish(object):
    pass

## Salmon class inheriting Fish
class Salmon(Fish):
    pass

## Halibut inheriting Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mery has-a pet satan
mary.pet = satan

print(mary.name, ' has a ', mary.pet.name)

## Frank is-a Employee
frank = Employee("Frank", 120000)

## Frank has-a pet rover
frank.pet = rover

## flipper is a Fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()