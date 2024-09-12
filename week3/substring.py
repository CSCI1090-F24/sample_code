# Function to see whether one string is
# a substring of the other (and vice versa)

def stringInString(s1, s2):
    if s1 in s2:
        print(s1, "is a substring of", s2)
    elif s2 in s1:
        print(s2, "is a substring of", s1)

stringInString("cat", "catharsis")
stringInString("elephant", "ant")
stringInString("dog", "cat")
stringInString("cat", "cat")
