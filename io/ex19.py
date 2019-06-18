txt = open('test.txt')

print(txt.name, txt.mode)

print(txt.read())

for line in txt:
    print(line)

filename = "/home/rahul/git/github_repos/training/python/io/Transactions-2019-04-12.csv"

txt_1 = open(filename)
print(txt_1)

for line in txt_1:
    print(line)
