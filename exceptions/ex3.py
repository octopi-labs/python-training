import sys
import os

filename = os.path.dirname(__file__) + os.sep + "test_1.txt"
try:
    print("In try block")
    f = open(filename, encoding = 'utf-8', mode='r')
    # perform file operations
    print(f.read())
except FileNotFoundError:
    print("{} file not found".format(filename))
    f = open(filename, encoding = 'utf-8', mode='w')
    f.write("New file created")
    f.close()
    f = open(filename, encoding = 'utf-8', mode='r')
    print(f.read())
finally:
    f.close()
