import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
    except ZeroDivisionError:
        entry = 1
        r = 1/entry
        print("Oops! denominator is 0")
        print("Next entry.")
        print()
    except TypeError:
        print("Type error occured")
        print("Next entry")
        print()
    except ValueError:
        print("Expected a number got an alphabate")
        print("Next entry")
        print()
    except Exception as e:
        print("Testing")
        
print("The reciprocal of",entry,"is",r)