from sys import argv


filename, username = argv

prompt = '> '

print("Please enter your name")
name = input(prompt)

print("Hello {name}, I am {username}".format(username=username, name=name))
print("Hello {0}, I am {1}".format(username, name))
print("Hello " + name + ", I am " + username)
print("Hello", name, ", I am", username)

