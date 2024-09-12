# Open file for reading "r"
f = open("pandp.txt", "r", encoding="utf-8")

# Open file for writing "w"
g = open("Tsent.txt", "w")

# For every line in the file...
for line in f:

    # ..if that line begins with a T...
    if line[0] == "T":

        # ...write that line out to the file
        g.write(line.lower())

# Don't forget to close your files!
f.close()
g.close()
