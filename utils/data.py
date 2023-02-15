import random
import numpy as np
from utils import geometry as geo
# create a number of data squares
# data will be a np array of squares
# the squares will not intersect
# number of data will be chosen by the user


def create_data(number_of_data, square0):
    data = []
    
    for i in range(number_of_data):

        x = random.choice(square0[0])
        y = random.choice(square0[1])
        size = random.choice(square0[2])
        rotation = random.choice(square0[3])
        

        current_square = np.array([x,y,size,rotation])
        
        # check if they intersect
        # if they do not intersect add them to the data
        if not geo.check_intersection(data, current_square):
            data.append(current_square)
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
