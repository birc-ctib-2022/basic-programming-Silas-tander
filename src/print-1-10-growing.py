
# Print the numbers described in the exercise
x = ''
for i in range (1,11):
    x += '{}'.format(i)
    print(x.strip())

# this works though
j = []
for i in range(1,11):
    j.append(i)
    print(*j)

# here i has to be a string?
j = []
for i in range(1,11):
    j.append(str(i))
    print("".join(j))