# Function: how old will you be in 2026?
def agein2026(a):
    newage = a + 2
    return newage

# Get the user's current age
age = int(input("how old are you now? "))


# Get their future age
future_age = agein2026(age)
print(f"You will be {future_age} in 2026!")


# Now you can use their future age to tell them
# what they'll be able to do in 2026!
if future_age > 18:
    print("You will be able to vote!")

if future_age > 65:
    print("You will be able to collect social security!")

if future_age < 16:
    print("You will not be able to watch a rated R movie!")




