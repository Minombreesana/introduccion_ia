import numpy as np
import pandas as pd

class Kmeans:

    def __init__(self, data, iterations, clusters):
        self.data = data
        self.iterations = iterations
        self.clusters = clusters
    
    def kmeans(self):
        data = self.data.to_numpy()
        min_distances = np.zeros(len(data))
        indexes = np.array([x for x in range(0, len(data),1)])
        centroids = data[np.random.choice(indexes, size = (self.clusters), replace = False)]
        centroids = centroids[:,None]
        
        for i in range(self.iterations):
            distances = np.sum((data - centroids)**2, axis = 2)**0.5 
            min_distances = np.argmin(distances, axis = 0)
            for c in range(self.clusters):
                centroids[c] = np.mean(data[min_distances == c, :], axis = 0)

        distances = np.sum((data - centroids)**2, axis = 2)**0.5
        min_distances = np.argmin(distances, axis = 0)
        centroids = np.reshape(centroids, (self.clusters, data.shape[1]))

        return min_distances, centroids

data = pd.read_csv('../data/clase3v2.csv',delimiter=';',header=None)
x = Kmeans(data, 10,3)
print(x.kmeans())