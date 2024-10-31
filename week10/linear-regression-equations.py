# Using the standard equation for simple linear regression
# with one independent variable (i.e., the situation where
# you are just getting the equation for a line).

# import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

# These are our three points from the "how many snacks
# after dinner have I eaten" example from class 10.2
x = [1, 2, 4]
y = [3, 6, 9]

# Get the means you need for the equation for a
xbar = np.mean(x)
ybar = np.mean(y)

# Get the top and bottom of the equation for a
# with a nice for loop over the points.
toptotal = 0
bottomtotal = 0

for i in range(len(x)):
    toptotal += (x[i]-xbar) * (y[i]-ybar)
    bottomtotal  += (x[i]-xbar) * (x[i]-xbar)

a = toptotal/bottomtotal

# Get b using a
b = ybar - (a * xbar)

# Print out the equation
print(f"y={a}x + {b}")


# Plot that line, plus our best fitting line
# from the ones we considered in the slides.
plt.plot(x, y, ".")
plt.plot([0, 4], [b, a*4+b])
plt.plot([0, 4], [1.5, 2*4+1.5])
plt.show()


plt.show()



