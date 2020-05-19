people = 10
dogs = 100
cats = 25


if people > dogs:
    print("There are {} dogs".format(dogs))

if dogs > cats:
    print("There are {0} dogs and {1} cats".format(dogs, cats))


if people == cats:
    print("Both people and cats are equal in numbers.")


if people < dogs:
    print("For total {people} people there are {dogs} dogs".format(people=people, dogs=dogs))


people += 25
# people = people + 25

if people > dogs:
    print("There are {} dogs".format(dogs))

if people == cats:
    print("Both people and cats are equal in numbers.")


if people < dogs:
    print("For total {people} people there are {dogs} dogs".format(people=people, dogs=dogs))

if people < dogs and people > cats and cats < dogs:
    print("For total {people} people there are {dogs} dogs".format(people=people, dogs=dogs))

if people < dogs and (people > cats or cats < dogs):
    print("For total {people} people there are {dogs} dogs".format(people=people, dogs=dogs))

if people != dogs and not people == cats and not cats < dogs:
    print("For total {people} people there are {dogs} dogs".format(people=people, dogs=dogs))
'''
if condition1:
    if body
elif condition2:
    elif body
    ...
else:
    condition_n
'''

if people > dogs:
    print("Hello")
elif not people < cats:
    print("Okay")
elif dogs < cats:
    print("Hello")
else:
    print("This is final.")


if people < (cats + 20):
    print("Hello")
    if dogs > (people + cats):
        print("Hi")
    elif dogs < (cats + 100):
        print("Hello World")
    else:
        print("Final")
else:
    print("Nothing printing")


for item in []:
    print(item)
else:
    print("Can not execute for.")


# a = age < 13 ? "first" : "second"
age = 12
a = "first" if age < 13 else "second"
print(a)