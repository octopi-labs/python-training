x = "There are {} types of people.".format(10)
binary = "binary"
do_not = "don't"
y = "Those who know {binary} and those who {do_not}.".format(binary=binary, do_not=do_not)
print(x)
print(y)
print("I said: %r." % x)
print("I also said: %s." % y)
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)
