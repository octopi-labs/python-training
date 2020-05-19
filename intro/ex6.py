my_name = 'Rahul Shelke'
my_age = 33 # not a lie
my_height = 74 # inches
my_weight = 130 # lbs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'
print("Let's talk about {}.".format(my_name))
print("He's {0} inches tall.".format(my_height))
print("He's {weight} pounds heavy.".format(weight=my_weight))
print("Actually that's not too heavy.")
print("He's got {0} eyes and {1} hair.".format(my_eyes, my_hair))
print("His teeth are usually {my_teeth} depending on the coffee.".format(my_teeth=my_teeth))
# this line is tricky, try to get it exactly right
print("If I add {age}, {height}, and {weight} I get {total}.".format(
    age=my_age, weight=my_weight, height=my_height, total=my_age + my_height + my_weight))
