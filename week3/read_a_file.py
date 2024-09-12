# open a file for reading with open()
# "r" is optional; it means "read this file"
# encoding="utf-8" is optional for Mac, suggested for Windows
# f is a variable that is your file handle
f = open("pandp.txt", "r", encoding="utf-8")

# read the whole file into a string variable called words
words = f.read()
print(type(words))

# then print it out
print(words)

# then close the file
f.close()



## Another thing you can do with a file object:
## read a file one line at a time

f = open("pandp.txt", "r", encoding="utf-8")

firstline = f.readline()
print("1:", firstline)
secondline = f.readline()
print("2:", secondline)

f.close()


## One more thing you can do with a file object:
## go through the file line by line with a for loop

## For fun, I'm using with/as syntax to avoid
## having to close the file:

## Notice also that I didn't use "r" and encoding="utf-8"!

with open("pandp.txt") as f:
    for line in f:
        print(line)

