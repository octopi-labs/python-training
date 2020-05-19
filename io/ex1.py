print("How old are you?")
age = input()
print(type(age))
print("How tall are you?")
height = input()
print("How much do you weigh?")
weight = input()
print("So, you're {age} old, {height} tall and {weight} heavy.".format(age=age,
                                                                       height=height,
                                                                       weight=weight))
