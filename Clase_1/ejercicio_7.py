import numpy as np

class Distance:

    def __init__(self, array, centroids):
        self.array = array
        self.centroids = centroids
    
    def min_distances(self):
        centroids = self.centroids[:,None]
        distances = np.sum((centroids - self.array)**2, axis = 2)**0.5 
        min_distances = np.argmin(distances, axis = 0)

        return min_distances

vector = np.array([(1,2,3),(4,5,6),(7,8,9)])
centroids = np.array([(1,0,0),(0,1,1)])

min_distance = Distance(vector, centroids)
 
print(f'Los centroides a los que pertenece cada vector x son:{x.min_distances(centroids)}')