import random
import numpy as np
from utils import geometry as geo
# create a number of data squares
# data will be a np array of squares
# the squares will not intersect
# number of data will be chosen by the user


def create_data(number_of_data, x0, y0 ,size0, rotation0):
    data = []
    cnt = 0
    while(cnt != number_of_data):

        x = random.choice(x0)
        y = random.choice(y0)
        size = random.choice(size0)
        rotation = random.choice(rotation0)
        

        current_square = np.array([x,y,size,rotation])
        
        # check if they intersect
        # if they do not intersect add them to the data
        if not geo.check_intersection(data, current_square):
            data.append(current_square)
            cnt += 1
    return data


def rotations(mu, sigma, num):
    r_list = []
    for i in range(num):
        for j in range(mu.__len__()):
            value = np.random.normal(mu[j], sigma[j])
            if value < 0 or value > 90:
                while value < 0 or value > 90:
                    value = np.random.normal(mu[j], sigma[j])
            r_list.append(value)
    return r_list
