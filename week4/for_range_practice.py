
# add up all the integers between two provided integers
# in this case, we are not including the provided integers in the sum
def addstuff(a, b):
    total = 0
    for i in range(a+1, b):
        total += i
    print(total)

# get the numbers
num1 = int(input("enter an integer: "))
num2 = int(input("enter an integer: "))

# if the first number is smaller, make it the starting point
# otherwise make the second number the starting points
if num1 < num2:
    addstuff(num1, num2)
else:
    addstuff(num2, num1)

# Start at the first number, go down by the interval of the
# second number, and stop before you get to a negative number
def stopnegative(a, b):
    for i in range(a, -1, -b):
        print(i)

# get the numbers
num1 = int(input("enter an integer: "))
num2 = int(input("enter an integer: "))

# if the first number is smaller, make the second number the starting point
# otherwise make the first number the starting point
if num1 < num2:
    stopnegative(num2, num1)
else:
    stopnegative(num1, num2)




