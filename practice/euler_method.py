# Euler method


#Importing external libraries
import numpy as np
from matplotlib import pyplot as plt

#Listing 2: Defining basic data
x0 = 0
y0 = 1
xf = 12
n = 101
deltax = (xf-x0)/(n-1)

#Listing 3: Defining x-values

x = np.linspace(x0, xf, n)

#Listing 4: Initializing Array for y-values

y = np.zeros([n])

#Listing 5: For loof for Euler's method

y[0] = y0
for i in range(1, n):
    y[i] = deltax * (-y[i-1] + np.sin(x[i-1])) + y[i-1]

#Listing 6: Printing the data
for i in range(n):
    print(x[i], y[i])

plt.plot(x, y, 'o')
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Approximate solution with forward Euler's Method")
plt.show()
