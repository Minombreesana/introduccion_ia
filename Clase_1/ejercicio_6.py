import numpy as np

class Distance:

    def __init__(self, array):
        self.array = array
    
    def distance_centroides(self, centroids):

        centroids = centroids.array[:,None]
        distances = np.sum((centroids - self.array)**2, axis = 2)**0.5 

        return distances

x = Distance(np.array([(1,2,3),(4,5,6),(7,8,9)]))
centroids = Distance(np.array([(1,0,0),(0,1,1)])) 

print(f'Las distancias de los vectores x a los centroides son:{x.distance_centroides(centroids)}')
