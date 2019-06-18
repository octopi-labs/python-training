# 0 1 1 2 3 5 8 13 ...
# start = 0, sum = 1
# sum = start + sum
# start = sum - start

start = 0
sum = 1
even = 0
#while True:
while sum <= 4000000:
    # If processing exceeds 4 million stop loop
    sum = start + sum
    start = sum - start
    if sum % 2 == 0:
        even += sum
#    if sum > 4000000:
#        break

# print("Total Sum:", sum)
print("Sum of even values:", even)

