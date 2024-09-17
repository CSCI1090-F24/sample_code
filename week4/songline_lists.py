line = input("what is a line from your favorite song: ")

# convert the string into a list of "words" (as separated by space)
words = line.split()

# print the line
print(line)

# print the list of words
print(words)

# confirm the type of these two variables
print(type(line))
print(type(words))

# print the number of words in the line
print(len(words))

# print the first letter of ecah word
for e in words:
    print(e[0])

# print the length of each word
for e in words:
    print(len(e))

# change the first word to "No"
print(words)
words[0] = "No"
print(words)
