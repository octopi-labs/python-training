import traceback

import logs


def isfloat(value):
    try:
        float(value)
        return True
    except:
        return False

class Calculator(object):
    def add(self, a, b):
        if not (isfloat(a) and isfloat(b)):
            raise TypeError("unsupported operand type(s) for +: '{0}' and '{1}'".format(type(a), type(b)))
        return float(a) + float(b)

    def subtract(self, a, b):
        if not (isfloat(a) and isfloat(b)):
            raise TypeError("unsupported operand type(s) for +: '{0}' and '{1}'".format(type(a), type(b)))
        return float(a) - float(b)

    def multiply(self, a, b):
        if not (isfloat(a) and isfloat(b)):
            raise TypeError("unsupported operand type(s) for +: '{0}' and '{1}'".format(type(a), type(b)))
        return float(a) * float(b)

    def divide(self, a, b):
        if not (isfloat(a) and isfloat(b)):
            raise TypeError("unsupported operand type(s) for +: '{0}' and '{1}'".format(type(a), type(b)))
        return float(a) / float(b)


if __name__ == "__main__":
    calculator = Calculator()
    operations = {
        'add': '+',
        'subtract': '-',
        'multiply': '*',
        'divide': '/'
    }
    while True:
        print("Choose one of the options from operations listed below:\n1. add\n2. subtract\n3. multiply\n4. divide\n5. exit")
        try:
            op = input("Enter operation: ")
            if op == "exit":
                logs.write_to_logs("INFO", "Exiting the program")
                print("Bye Bye! \N{slightly smiling face}")
                break
            
            func = getattr(calculator, op)
            
            print("Enter two numbers to perform {0}".format(op))
            a = input("Enter number 1: ")
            b = input("Enter number 2: ")

            result = func(a, b)

            result_str = "The {op} operation between {a} and {b} is: {a} {op} {b} = {ans}"
            result_str = result_str.format(a=a, b=b, op=operations[op], ans=result)
            print("-"*50 + "\n" + result_str + "\n" + "-"*50)
            
            logs.write_to_logs("INFO", result_str)
        except Exception as exc:
            result_str = "{0} occured please verify your inputs".format(type(exc).__name__)
            print("-"*50 + "\n" + result_str + "\n" + "-"*50)
            
            # Write error with traceback in logs
            error = traceback.format_exc()
            logs.write_to_logs("{}[{}]".format("ERROR", type(exc).__name__), error)
        
