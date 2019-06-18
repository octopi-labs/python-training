import re


pattern = '^a[a-z][0-9]s$'
# pattern = '[by]*'
test_string = 'abyss'
result = re.match(pattern, test_string)
print(result)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")