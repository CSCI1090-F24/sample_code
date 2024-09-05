def larger_than_ten(n):
    if n > 10:
        print(n, "is larger than 10")
    else:
        print(n, "is not larger than 10")

larger_than_ten(5)
larger_than_ten(11)
larger_than_ten(10)


# While it's true that 10 is not larger than 10
# we might want to say that 10 is equal to 10

# Here's a better definition of this function:
def better_larger_than_ten(n):
    if n > 10:
        print(n, "is larger than 10")
    elif n < 10:
        print(n, "is smaller than 10")
    else:
        print(n, "is equal to 10")

better_larger_than_ten(5)
better_larger_than_ten(11)
better_larger_than_ten(10)
