# Function: Return a string backwards
def backwards(s1):
    s2 = ""
    for i in range(len(s1)-1, -1, -1):
        s2 = s2 + s1[i]
        #print(s1[i], end="")
    return s2


# And here's how you use it!
# We are saving what it returns to a string!
backstring = backwards("cat")
print(backstring)


# Function: Return the length of a string
# (Yes, this is a silly function!)
def lengthstring(s1):
    return(len(s1))

print(lengthstring("elephant"))


# Function: Return the average length of three strings
def avlen(s1, s2, s3):
    av = (len(s1) + len(s2) + len(s3))/3
    return av

# Example: compare the average length of one
# group of strings to another group of strings
q = avlen("dog", "elephant", "leopard")
r = avlen("a", "b", "c")

if q > r:
    print("The first list has longer words, on average")
else:
    print("The second list has longer words, on average")




