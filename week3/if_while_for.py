## Tell user if their number is odd or even

num = int(input("enter an even number: "))

if num % 2 == 0:
    print("thank you for entering an even number")
else:
    print("that is not an even number")


## Keep asking a user to enter a number until
## they enter an even number

num = int(input("enter an even number: "))
while num % 2 == 1:
    print(num, "is not even!")
    num = int(input("enter an even number: "))

print("thank you for entering an even number")


## Make the user guess until they get your number:

mynum = 5
guess = int(input("guess my number: "))

while guess != mynum:
    guess = int(input("guess my number: "))

print("you guessed my number:", mynum)


## Wish the used "Happy birthday" as many
## times as they choose.

# Option 1: while loop with counter
howmany = int(input("how many times? "))

counter = 0
while howmany != counter:
    print("Happy birthday!")
    counter = counter + 1


# Option 2: for loop with range()
howmany = int(input("how many times? "))

for i in range(howmany):
    print("Happy birthday!")














