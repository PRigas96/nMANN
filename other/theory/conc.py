# y = (a*x+b) + s0*step(x-x0) + s1*step(x-x1))
# where step(x) = 0 if x < 0, 1 if x >= 0
# x0 and x1 are the x values where the step functions change
# s0 and s1 are the step function values at x0 and x1
# a and b are the slope and intercept of the line
# x is the independent variable
# y is the dependent variable
# import the necessary modules
import numpy as np
import matplotlib.pyplot as plt

# define parameters
a = 0.5
b = 1
s0 = 2
s1 = 2.5
x0 = 3
x1 = 6


# define a sigmoide function
def sigmoid(x):
    return 1/(1+0.4*np.exp(-2*x))

# define the function


def f(x):
    return a*x+b+s0*sigmoid(x-x0)+s1*sigmoid(x-x1)


# plot
x = np.linspace(0, 10, 100)
# put noise in y
y = f(x)+np.random.normal(0, 0.2, len(x))
plt.plot(x, y)
# add labels
plt.xlabel('x[n]')
plt.ylabel('y[n]')
plt.title('Concatinated results')
# limit axis
plt.show()
