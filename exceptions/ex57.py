import sys

def function_1(a, b):
    print("In function 1")
    print(function_2(a, b))
    print("Exiting program")

def function_2(a, b):
    print("In function 2")
    return function_3(a, b)

def function_3(a, b):
    print("In function 3")
    if b == 0:
        raise ZeroDivisionError("Value of denominator is zero: {0}".format(b))
    return a / b


if __name__ == "__main__":
    try:
        function_3(1, 0)
    except ZeroDivisionError as ze:
        print(ze)
        print("Oops!",sys.exc_info()[0],"occured.")

