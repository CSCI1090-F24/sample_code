# Create three lists: 
# All ints between 1 and 20 inclusive
a = []
for i in range(1, 21):
    a.append(i)

# All even ints between 1 and 20 inclusive
b = []
for i in range(1, 21):
    if i%2 == 0:
        b.append(i)

# or...
b = []
for i in range(2, 21, 2):
    b.append(i)


# All ints divisible by 3 between 1 and 20 inclusive
c = []
for i in range(1, 21):
    if i % 3 == 0:
        c.append(i)

print(a)
print(b)
print(c)


# Put them together into one list.
d = a + b + c
print(d)

# Print out the length of the list.
print(len(d))

# Print out how many times 6 appears in the big list.
print(d.count(6))


# Sort the list and print it out.
d.sort()
print(d)

# Remove the first instance of 9 from the list.
d.remove(9)
print(d)



# Remove all numbers divisible by 7 from the list.
# Complicated approach using only what we know so far.
# 1. get a list of the indices of all the elements divisible by 7
removethese = []
for i in range(len(d)):
    if d[i] % 7 == 0:
        removethese.append(i)

# 2. remove them one by one, going backwards so you 
# don't mess up the indexing!
for i in range(len(removethese)-1, -1, -1):
    d.pop(removethese[i])

print(d)

# Alternative: let's try again butremove all elements divisible by 6
# Easy way: use list comprehension. You don't need to know this. :)
e = [x for x in d if x % 6 != 0]
print(e)
