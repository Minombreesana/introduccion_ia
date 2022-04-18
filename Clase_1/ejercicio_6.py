import numpy as np

class Distance:

    def __init__(self, array):
        self.array = array
        self.centroids = centroids
        self.norma_l2 = self.norma_l2()

    def distance_centroides(self):
        distances = self.norma_l2
        return distances

    def norma_l2(self):
        centroids = self.centroids[:,None]
        return np.sum((centroids - self.array)**2 , axis=2)**0.5


centroids = np.array([(1,0,0),(0,1,1)])
vector = np.array([(1,2,3),(4,5,6),(7,8,9)])

x = Distance(vector, centroids)

print(f'Las distancias de los vectores x a los centroides son:{x.distance_centroides()}')
