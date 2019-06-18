def palindrome_num(number):
    num_str = ""
    status = True
    while status:
        num1 = number % 10
        num_str = num_str + str(int(num1))
        number = number / 10
        if number < 10:
            status = False
    num_str = num_str + str(int(number))
    return num_str

"""
1. Call palindrome_str function
2. create temporary variable, to store reverse of a string
3. Calculate length of original string
4. loop through from 0 upto length of original string
4.1. concatenate pal_str to default_str, (default_str[index] + pal_str)
5. return reverse string generated.
6. print(reverse of a string)
7. Compare original string with reversed string and check if it is a palindrome
or not.
"""
def palindrome_str(default_str):
    pal_str = ""
    length = len(default_str)
    for i in range(0, length):
        pal_str = default_str[i] + pal_str
    return pal_str

print(__name__)
if __name__ == "__main__":
    number = 909
    pal = palindrome_num(number)
    print(pal)
    print(pal == str(number))
    default_str = "malayalam"
    pal_str = palindrome_str(default_str)
    print(default_str)
    print(pal_str)
    print(pal_str == default_str)

