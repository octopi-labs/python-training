class Test(object):

    def __init__(self, name):
        self.test = name

    def print_test(self):
        return self.test


test_obj = Test(27)
print(test_obj.print_test())
test_obj.test = 49
print("Self: ", test_obj.test)
print("Method: ", test_obj.print_test())


class Example(object):

    def __init__(self):
        self.first = None # first
        self.last = None # last

    def print_name(self):
        return "{0} {1}".format(self.first, self.last)


example_obj = Example()  # "Rahul", "Shelke")
print(example_obj.print_name())
print(example_obj.first)
print(example_obj.last)
# example_obj.middle = ""
example_obj.first = "Rahul"
example_obj.last = "Shelke"
print(example_obj.print_name())

