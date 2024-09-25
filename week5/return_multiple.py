# Exercise 1: return a string backwards and its length
def backwards(s1):
    s2 = ""
    for i in range(len(s1)-1, -1, -1):
        s2 = s2 + s1[i]
    return s2, len(s1)


stuff = backwards("elephant")
print(stuff[0])
print(stuff[1])


# Exercise 2: return the average length of three strings
# and the length of the longest string
def lengthstuff(s1, s2, s3):
    avlength = (len(s1)+len(s2)+len(s3)) / 3

    # start by assuming s1 is the longest
    maxlen = len(s1)

    # if s2 is longer, change the maxlen to s2's length
    if len(s2) > maxlen:
        maxlen = len(s2)

    # if s3 is longer than the current max, change
    # maxlen to s3's length
    if len(s3) > maxlen:
        maxlen = len(s3)

    # return
    return avlength, maxlen


# Exercise 2, option 2: more compact version of the above
def lengthstuff_fancy(s1, s2, s3):
    lenlist = [len(s1), len(s2), len(s3)]
    return sum(lenlist), max(lenlist)


a, b = lengthstuff("dog", "in", "house")
print(f"average={a}, max={b}")


things = lengthstuff_fancy("dog", "in", "house")
print(f"average={things[0]}, max={things[1]}")

    
# Exercise 3: return whether a is divisible by b
# and the remainder you get
def dividing(a, b):

    # start by assuming divisible is False
    divisible = False

    # if a is divisble by b, then reset divisible to True
    if a % b == 0:
        divisible = True

    # calculate the remainder
    remainder = a % b

    #return
    return divisible, remainder

d, r = dividing(10, 3)
print(d, r)

# Exercise 3, option 2: even simpler verions
def dividing_fancy(a, b):
    return a%b==0, a%b

d, r = dividing_fancy(10, 3)
print(d, r)
