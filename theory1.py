import numpy as np
import matplotlib.pyplot as plt


# load dataset from v2
#data = np.load('./data_v2/1000sq/1000sq_1_12.npy')
data = np.load('./data_v2/1000sq/1000sqv2.npy')
#data = np.load('./data_v1/1000sq/1000sq.npy')
#data = np.load('./data_v1/1000sq/5000sq.npy')
l = data[:, -2]
theta = data[:, -1]

# find holes for every l not just l=1
holes_ = []
holes_tot = []
r = .8
for i in range(1, 9):
    # find all values with l = i
    l_ = np.where(l == i)
    # get their theta values
    theta_ = theta[l_]
    # sort them
    theta_ = np.sort(theta_)
    # find holes in theta1 with radius r
    # hole is where theta[i+1] - theta[i] > r
    # we need to find all theta[i] where theta[i+1] - theta[i] > r
    holes_ind_ = np.where(theta_[1:] - theta_[:-1] > r)
    # find holes values
    holes_ = theta_[holes_ind_]
    # fill hole values with step = r
    holes_fill_ = []
    for j in range(len(holes_)):
        # arrange will have values from holes[i] to theta1 where the hole was found + r
        # step will be r
        holes_fill_.append(
            np.arange(holes_[j], theta_[holes_ind_[0][j]+1]+r, r))
    # flatten holes_fill
    holes_fill_ = np.array(holes_fill_).flatten()
    # make holes_fill into a 1d array
    hn_ = []
    for j in range(len(holes_fill_)):
        for k in range(len(holes_fill_[j])):
            hn_.append(holes_fill_[j][k])
    hn_ = np.array(hn_).flatten()
    # append to holes_tot
    holes_tot.append(hn_)

# create y axis
y_ = [(i+1)*np.ones(len(holes_tot[i])) for i in range(len(holes_tot))]
holes_flatten = [holes_tot[i][j]
                 for i in range(len(holes_tot)) for j in range(len(holes_tot[i]))]
y_flatten = [y_[i][j] for i in range(len(y_)) for j in range(len(y_[i]))]
plt.scatter(holes_flatten, y_flatten, color='red', marker='o', s=1)


# print l as function of theta
plt.scatter(theta, 1*l, color='blue', marker='o', s=2)
# do not plot values between 1 and 2 in y axis
# make intermidiate values in y,x compact
# this means that between 1 and 2 in y there will be no plot
# and between 0 and 1 in x there will be no plot

# show grid

plt.grid(color='black', linestyle=':', linewidth=1, alpha=0.5)
# plot till 12 in y axis
e = 4
plt.ylim(0-e, 8+e)
plt.xlim(0-10*e, 90+10*e)
# put latex in y and x axis
plt.xlabel(r'$\theta \sim G(\mu,\sigma)$', fontsize=20, labelpad=20)
plt.ylabel(r'$\ell\sim J(\mu,\sigma)$', fontsize=20, labelpad=50, rotation=0)
# plot holes in x,y axis

# put holes_tot in with red color,
plt.scatter(holes_flatten, y_flatten, color='red', marker='o', s=.5)
# put legend
plt.legend(['$\ell(θ)$', '$holes$'], loc='upper right')
plt.show()
