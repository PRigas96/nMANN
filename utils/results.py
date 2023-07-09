import numpy as np
from utils import kde as kde
from utils import metrics as mt
from utils import geometry as geo


def accuracy_measurment(clusters, q_points, data, length=[0, 10]):
    """
    measure the accuracy of the clustering

    Parameters:
        q_points: query points
        data: data to be clustered
        length: begin and end of the query points to be used
    """
    beg = length[0]
    end = length[1]
    q_p = q_points[beg:end]
    acc1 = 0
    acc = 0
    dd_s = []
    dd_scl = []
    dt = []
    for i in range(q_p.__len__()):
        # inside a point
        # bf with 100%
        min_dist_100 = np.inf
        min_id_100 = [-1]
        dista = []
        for j in range(data.__len__()):
            dist = mt.Linf(geo.create_square2(data[j]), q_p[i])[0]  # get 100% Linf dist
            l_inf_100 = dist
            dista.append(dist)
            if dist < min_dist_100:
                min_dist_100 = dist
                min_id_100 = [-1]
                min_id_100[0] = j
                continue
            if dist == min_dist_100:
                min_id_100.append(j)
        # bf with simple Linf without clustering
        min_dist_simple = np.inf
        min_id_simple = [-1]
        distb = []
        for j in range(data.__len__()):
            dist = mt.Linf_(geo.create_square2(data[j]), q_p[i])
            distb.append(dist)
            if dist < min_dist_simple:
                min_dist_simple = dist
                min_id_simple = [-1]
                min_id_simple[0] = j
                continue
            if dist == min_dist_simple:
                min_id_simple.append(j)
        if min_id_simple[0] == min_id_100[0]:
            acc1 += 1
        # bf with simple Linf and clustering
        min_dist_m = [np.inf for _ in range(clusters.__len__())]
        min_id_m = [[-1] for _ in range(clusters.__len__())]
        for c in range(clusters.__len__()):
            for j in range(clusters[c].__len__()):
                dist = mt.Linf_(geo.create_square2(clusters[c][j]), q_p[i])
                if dist < min_dist_m[c]:
                    min_dist_m[c] = dist
                    min_id_m[c] = [-1]
                    min_id_m[c][0] = j
                    continue
                if dist == min_dist_m[c]:
                    # insert to cluster in last position
                    min_id_m[c].append(j)
        for c in range(clusters.__len__()):
            for i in range(min_id_m[c].__len__()):
                if np.all(clusters[c][min_id_m[c][i]][0:2] == data[min_id_100[0]][0:2]):
                    acc += 1
                    break
    print("L_infty^* and Clustering Accuracy: {} %".format(acc / end * 100))
    print("L_infty^* Accuracy: {} %".format(acc1 / end * 100))
