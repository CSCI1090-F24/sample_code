# GOAL: count the frequency of each character in a string

s1 = "Four score and seven years ago our fathers brought forth on this\
    continent a new nation conceived in liberty and dedicated to the \
    proposition that all men are created equal"


chars = {}


# OPTION 1

# Go through each character and count how many
# times you see that character
for c in s1:

    # if the character is already a key in the dictionary,
    # add 1 to its value
    if c in chars:
        chars[c] = chars[c] + 1

    # otherwise, create a dictionary entry for that character,
    # and assign that key the value of 1 since you've seen it once
    else:
        chars[c] = 1


## OPTION 2
        
chars = dict()  # same as chars = {}

# For each character in the string...
for c in s1:

    # Cool function for dictionaries: get()
    # This says: "if I find the key in the dictionary, I'll return its value.
    # Otherwise, I'll return 0."
    # Then you can just reset the value for that key to whatever get()
    # returns plus 1 (for seeing it one more time).
    chars[c] = chars.get(c, 0) +1


# TWO WAYS TO LOOP THROUGH A DICTIONARY

# For each key-value tuple pair, print it out.
for k,v in chars.items():
    print(f"The character {k} appears {v} times")

# For each key, go look up its value and print it out.
for k in chars:
    print(f"The character {k} appears {chars[k]} times")
