# use brute force to guess a passcode
# return the number of guesses required


def guesspasscode(pc):

    # keep track of number of guesses
    guesses = 0

    # use nested for loops to generate possible passcodes
    for i in "ABCD":
        for j in "ABCD":
            for k in "ABCD":
                myguess = i + j + k
                guesses += 1

                # if the guess matches the actual passcode
                # print it out and return the number of guesses
                if myguess == mypasscode:
                    print(f"You guessed it: {myguess}")
                    return guesses

mypasscode = "ADB"
print(f"Shhh... my passcode is {mypasscode}")
print(f"It took {guesspasscode(mypasscode)} guesses to guess the passcode!")
