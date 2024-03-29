import random
import numpy as np
from utils import geometry as geo


def create_data(number_of_data, x0, y0, size0, rotation0):
    data = []
    cnt = 0
    # number of acceptable intersections for each square generation
    max_num_of_collisions = 0.05 * number_of_data
    num_of_collisions = 0

    while cnt != number_of_data:
        if 1000 <= cnt <= 10000 and (cnt - 1000) % 500 == 0:
            print("reached ", cnt, " squares!")
            np.save(f"./data_v2/10000sq/{cnt}sq_1_4.npy", data)

        print("creating square ", cnt, "\n")
        x = random.choice(x0)
        y = random.choice(y0)
        size = random.choice(size0)
        rotation = random.choice(rotation0)

        current_square = np.array([x, y, size, rotation])

        # check if they intersect
        # if they do not intersect add them to the data
        if not geo.check_intersection(data, current_square):
            data.append(current_square)
            cnt += 1
            num_of_collisions = 0
        else:
            num_of_collisions += 1
            print(num_of_collisions)
            if num_of_collisions == max_num_of_collisions:
                print(
                    "max number of collisions reached! dataset creation terminates!\n"
                )
                break
    return data


def rotations(mu, sigma, num):
    """
    Generate a list of rotations

    Parameters:
        mu (float): mean of the normal distribution
        sigma (float): standard deviation of the normal distribution
        num (int): number of rotations to generate

    Returns:
        list: list of rotations
    """
    r_list = []
    for i in range(num):
        for j in range(mu.__len__()):
            value = np.random.normal(mu[j], sigma[j])
            if value < 0 or value > 90:
                while value < 0 or value > 90:
                    value = np.random.normal(mu[j], sigma[j])
            r_list.append(value)
    return r_list


# generate querry points


def gen_qpoints(squares, num_pts):
    """
    Generate querry points that are not inside the squares

    Parameters:
        squares (np.array): list of squares, each square is a 1x4 array of center of mass, length, and rotation
        num_pts (int): number of points to generate

    Returns:
        list: list of points that are not inside the squares
    """
    q_pts = []
    while len(q_pts) < num_pts:
        # generate a point from x = [3,297] and y = [3,297]
        x = np.random.randint(3, 297)
        y = np.random.randint(3, 297)
        # check if the point is inside the square
        label = False
        for sq_pt in squares:
            if geo.IsPointInsidePoly([x, y], geo.create_square2(sq_pt)):
                label = True
        if not label:
            q_pts.append([x, y])
    return q_pts
