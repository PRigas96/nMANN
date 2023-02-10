# lets create a y[n] = a*x[n] +  b*u[n-n0] + c*u[n-n1]
# x[n] = x[0] + n * w
# improts
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

# where a,b,c are constants and n0,n1 are integers
# and x[n] is the input signal and u[n] is the unit step function
# and n is the discrete time index
# we will use the following values for a,b,c,n0,n1,x[0],w
a = 0.5
b = 1.5
c = 2
n0 = 3
n1 = 6
x0 = 1
w = 1
# lets create the input signal
# get 100 samples from 0 to 1
n = np.linspace(0, 10, 100)
#n = np.arange(0, 10)
x = x0 + n * w
# lets create the unit step function
u = np.zeros(len(n))
u[n0*10:] = 1
u1 = np.zeros(len(n))
u1[n1*10:] = 1
# create the analog version
a1 = 0.3
b1 = 1
s01 = 2
s11 = 2.5
x01 = 3
x11 = 6.2


# define a sigmoide function
def sigmoid(x):
    return 1/(1+0.4*np.exp(-4*x))

# define the function


def f(x):
    return a1*x+b1+s01*sigmoid(x-x01)+s11*sigmoid(x-x11)


# lets create the output signal
# put noise to y signal
y = a*x+b*u+c*u1+np.random.normal(0, 0.2, len(x))
#y = a * x + b * u + c * u1
# lets plot the input and output signals
# plot an analog version of the input signal
# plot both y[n] and its analog version on same plot
plt.plot(n, y, label='y[n]')
# plot analog version of y[n] on same plot
# give noise to analog
y1 = f(n)+np.random.normal(0, 0.2, len(n))
# plot it
plt.plot(n, y1, label='Analog y[n]')
# plut descrete version of y[n] on same plot
plt.stem(n, y, label='Sampled y[n]')
# add labels
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Concatinated results')
# limit axis# show plot
plt.legend()
plt.show()
