def power_iter(x,y):
    total = 1
    for i in range(y):
        total = total * x
    return total


def power_recur(x,y):
    print(x,y)
    if y == 0:
        return 1
    return x * power_recur(x, y-1)
    
#print(power_iter(2,8))

#print(power_recur(2,8))


import numpy as np

x = [1, 2, 4]
y = [3, 6, 9]

xbar = np.mean(x)
ybar = np.mean(y)

toptotal = 0
bottomtotal = 0

for i in range(len(x)):
    toptotal += (x[i]-xbar) * (y[i]-ybar)
    bottomtotal  += (x[i]-xbar) * (x[i]-xbar)

a = toptotal/bottomtotal

b = ybar - (a * xbar)

print(f"y={a}x + {b}")

import matplotlib.pyplot as plt

plt.plot(x, y, ".")
plt.plot([0, 4], [b, a*4+b])
plt.plot([0, 4], [1.5, 2*4+1.5])
plt.show()


plt.show()


