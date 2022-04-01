import numpy as np

class Distance:

    def __init__(self, array):
        self.array = array
    
    def min_distances(self, centroids):
        centroids = centroids.array[:,None]
        distances = np.sum((centroids - self.array)**2, axis = 2)**0.5 
        min_distances = np.argmin(distances, axis = 0)

        return min_distances
    
x = Distance(np.array([(1,2,3),(4,5,6),(7,8,9)]))
centroids = Distance(np.array([(1,0,0),(0,1,1)])) 

print(f'Los centroides a los que pertenece cada vector x son:{x.min_distances(centroids)}')