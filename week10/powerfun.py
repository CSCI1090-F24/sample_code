### Functions to calculate x to the power of y

# iterative
def power_iter(x,y):
    total = 1
    for i in range(y):
        total = total * x
    return total

# recursive
# base case is when y==0 because that's always 1
def power_recur(x,y):
    print(x,y)
    if y == 0:
        return 1
    return x * power_recur(x, y-1)
    
print(power_iter(2,8))
print(power_recur(2,8))


