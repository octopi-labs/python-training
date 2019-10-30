# - *- coding: utf- 8 - *-
# import pprint
from pprint import pprint

# This like starts program by writing message
print("I will now count my chickens:")

# divide 30 / 6 , result 5. Add that to 25, 25 + 5 => 30
print("Hens", 25.0 + 30.0 / 6.0)
# Multiply 25 * 3 => 75, take modulo by 4 => 3, 100 - 3 => 97
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0)

# This like is again a message
print("Now I will count eggs:")

# Divide 1 / 4 => 0, 4 % 2 => 0, 3 + 2 + 1 - 5 + 0 - 0 + 6 => 7
print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

# Print what are we going to check
print("Is it true that 3 + 2 < 5 - 7?")
# 3 + 2 => 5, 5 - 7 => -2, 5 < -2 => False
print(3.0 + 2.0 < 5.0 - 7.0)

# Add 3 + 2 => 5
print(":".join(["What is 3 + 2?", str(3.0 + 2.0)]))
# Subtract 5 - 7 => -2
print("What is 5 - 7?: " + str(5.0 - 7.0))

# Message
print("oh, that's why it's False.")

# One more message
print("How about some more.")

# Check 5 > -2 => True
print("Is it greater?", 5.0 > -2.0)
# Check 5 >= -2 => True
print("Is is greater or equal?", 5.0 >= -2.0)
# Check 5 <= -2 => False
print("Is it less or equal?", 5.0 <= -2.0)

# This is with floating point numbers

a = {'ajscbdjbcal': 1, 'bsadvas': 2, 'asdvsdac': {'dsdava': 3, 'e': {'asdvdsf': 3}, 'f': 'ldvnklabjbdas'}, 'g': 'ksdnjva oc '}
pprint(a)
# pprint.pprint(a)