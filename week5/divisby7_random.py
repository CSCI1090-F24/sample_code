# Write a function that picks random numbers
# until it picks one that is divisible by 7

# don't forget to import random
import random

def divis7():

    # get your first random integer
    thing = random.randint(1, 100)
    num_tries = 1

    # while your random integer is not divisible 7,
    # guess a new integer and increment your number of tries
    while thing % 7 != 0:
        thing = random.randint(1, 100)
        num_tries += 1

    # print out the number and how many tries it took
    print(thing, num_tries)

divis7()
