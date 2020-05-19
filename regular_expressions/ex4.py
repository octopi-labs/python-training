import re


txt = "The rain in Spain is over.n"
x = re.search("^The.*n$", txt)
if x:
    print("Found a match")
else:
    print("No match found")