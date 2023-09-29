import numpy as np
from utils import kde as kde
from utils import metrics as mt
from utils import geometry as geo

def inference(clusters, q_points, ret='var'):
    """
        Inference on the query points
        
        Parameters:
            clusters: clusters
            q_points: query points
            
        Returns:
            nn: nearest neighbor(object) of the query points
            dist: distance between the query points and the nn
    """

    nn = []
    distance = []

    for i in range(q_points.__len__()):
        m_d = np.inf
        min_dist = [np.inf for _ in range(clusters.__len__())]
        min_id = [[-1] for _ in range(clusters.__len__())]
        for c in range(clusters.__len__()):
            for j in range(clusters[c].__len__()):
                dist = mt.Linf_(geo.create_square2(clusters[c][j]), q_points[i])
                if dist < min_dist[c]:
                    min_dist[c] = dist
                    min_id[c] = [-1]
                    min_id[c][0] = j
                    continue
                if dist == min_dist[c]:
                    min_id[c].append(j)
        # now use Linf in the resulted nearest neighbors
        for c in range(clusters.__len__()):
            for j in range(min_id[c].__len__()):
                d = mt.Linf(geo.create_square2(clusters[c][min_id[c][j]]), q_points[i])[0]
                if d < m_d:
                    m_d = d
                    m_id = [min_id[c][j], c]
                
        nn.append(m_id)
        distance.append(m_d)
    
    if ret == 'None':
        for i in range(len(nn)):
            print(f'Square {clusters[nn[i][1]][nn[i][0]]} \
                is the closest to the querry point {q_points[i]}')
        return None
    
    return nn, distance
