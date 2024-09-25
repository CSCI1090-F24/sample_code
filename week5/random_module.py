import random

# Generate 5 random integers between 100 and 1000.
for i in range(5):
    print(random.randint(100, 1000))

# Generate 5 random floats between 0 and 1
for i in range(5):
    print(random.random())


# Generate 5 random floats between 1 and 99
for i in range(5):
    print(random.uniform(1, 99))


# Get a long string from the user,
longstring = input("enter a long string: ")

# then randomly pick 10 characters from that string,
# and save it to a new string.
newstring = ""
for i in range(10):
    newstring = newstring + random.choice(longstring)

print(newstring)
