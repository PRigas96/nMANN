import numpy as np

# number of querry points
q_points = np.load(...)
# dataset
data = np.load(...)

for i in range(q_points.__len__()):
    # inside a point
    # bf with 100%

    min_dist_100 = np.inf
    min_id_100 = None
    for j in range(data.__len__()):
        dist = Linf(data[j], q_points[i]) # get 100% Linf dist
        if dist < min_dist:
            min_dist_100 = dist
            min_id_100 = None
            min_id_100 = j
        if dist = min_dist:
            min_id_100.append(j)

    # bf with simple Linf without clustering
    min_dist_simple = np.inf
    min_id_simple = None
    for j in range(data.__len__()):
        dist = Linf_(data[j], q_points[i])
        if dist < min_dist:
            min_dist_simple = dist
            min_id_simple = None
            min_id_simple = j
        if dist = min_dist:
            min_id_simple.append(j)

    # bf with simple Linf and clustering
    min_dist_m = [np.inf for _ in range(c.__len__())]
    min_id_m = [None for _ in range(c.__len__())]
    for c in range(clusters.__len__()):
        for j in range(c.__len__()):
            dist = Linf_(custers[c][j],q_points[i])
            if dist < min_dist:
                min_dist_m[c] = dist 
                min_id_m[c] = None
                min_id_m[c] = j
            if dist = min_dist:
                min_id_m[c].insert # TODO


    min_dist_t = np.inf
    min_id_t = None
    for id in min_id_m:
        dist = Linf(data[id], q_points[i])
        if dist < min_dist_t:
            min_dist_t = dist
            min_id_t = None
            min_id_t = id
        if dist = min_dist_t:
            min_id_t.append(id)

####
acc = 0
if np.all(min_id_t,min_id_100): # TODO
    acc += 1
acc /= q_points.__len__()

print("Acc is: %f \%",acc*100)


    








