import random
import math

mylist = []

for i in range(4):
    mylist.append(random.randint(1, 10))

myotherlist = [random.randint(1, 10) for i in range(4)]

print(mylist)
print(myotherlist)

minmaxsum = [min(mylist), max(mylist), sum(mylist)]

for e in minmaxsum:
    print(e, end=", ")

for e in mylist:
    print(math.sqrt(e))
    print(math.log(e))
    print(math.factorial(e))



                  
