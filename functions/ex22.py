"""
Syntax

def <function name>([parameter list]):
    <function body>....

"""


def first_func():
    print("Function with no parameter.")

def second_func(param="Rahul"):
    print("Function with single param: {}".format(param))

def third_func(param1, param2):
    print("Function with multiple parameters: {0}, {1}".format(param1, param2))

def fourth_func(*params):
    param1, param2, param3, param4 = params
    # param1, param2 = params
    # for item in params:
    #    print("Param: {}".format(item))
    print("Param 1: {0} and Param 2: {1}, {2}, {3}".format(param1, param2, param3, param4))


first_func()
second_func("Bhushan")
third_func("Rahul", "Shelke")
fourth_func("Rahul", "Shelke", "Here", "There")
