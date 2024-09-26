# don't forget to import!
import random

# define function
def randomstring():

    # get user input
    longstring = input("enter a long string: ")

    # Two ways to create new string of random chars
    
    # Option 1: random.choice()
    newstring = ""
    for i in range(10):
        newstring = newstring + random.choice(longstring)
    print(newstring)

    # Option 2: random.randint() with indices
    # Remember randint(a, b) includes a and b (unlike range())!
    newstring = ""
    for i in range(10):
        randchar = random.randint(0, len(longstring)-1)
        newstring = newstring + longstring[randchar]
    print(newstring)
    return newstring


rando_string = randomstring()
print(f"Here's a random 10-character string from your word: {rando_string}")




        
