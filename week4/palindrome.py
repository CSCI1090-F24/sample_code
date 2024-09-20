# Palindrome #1
# write a function to return a string backwards
def backwards(s1):
    s2 = ""
    for i in range(len(s1)-1, -1, -1):
        s2 = s2 + s1[i]
    return s2

# use the backwards function to see if a word is a palindrome
# Note that I am using two return statements!
def palindrome1(s1):
    s2 = backwards(s1)
    if s1 == s2:
        return True
    else:
        return False


# Palindrome #2
# compare first char to last char, then keep moving
# toward the middle. If you hit a mismatch, return False.

def palindrome2(s):

    # counter to start at the end
    start = -1

    # compare the first char to the last char,
    # then keep moving toward the middle
    for c in s:

        # if you find a mismatch, you can return False!
        # it's not a palindrome, so no need to keep going
        if c != s[start]:
            return False
        start = start - 1

    # if you get all the way through, then you never found
    # a mismatch. It must be a palindrome.
    return True

    
# Palindrome #3: using cool trick with strings
# to get the backwards string
def palindrome3(s1):
    s2 = s1[::-1]
    if s1 == s2:
        return True
    else:
        return False

    
# User enters a word
word = input("enter a word: ")


# Try out each function
if palindrome1(word):
    print("palindrome!")
else:
    print("not a palindrome")

if palindrome2(word):
    print("palindrome!")
else:
    print("not a palindrome")

if palindrome3(word):
    print("palindrome!")
else:
    print("not a palindrome")


