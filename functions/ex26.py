print("Let's practice everything.")

print('You\'d need to know \'bout escapes with \\ that do \n newlines and \ttabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("- - - - - - - - - - - - - - ")
print(poem)
print("- - - - - - - - - - - - - - ")

five = 10 - 2 + 3 - 6
print("This should be five: {0}".format(five))

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)
print("With a starting point of: {0}".format(start_point))
print("We'd have {0} beans, {1} jars, and {2} crates.".format(beans, jars, crates))
