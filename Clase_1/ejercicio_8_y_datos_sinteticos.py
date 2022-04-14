import numpy as np

class Kmeans:

    def __init__(self, iterations, clusters):
        self.data = self._sintetic_data()
        self.iterations = iterations
        self.clusters = clusters
    
    def kmeans(self):
        min_distances = np.zeros(len(self.data))
        indexes = np.array([x for x in range(0, len(self.data),1)])
        centroids = self.data[np.random.choice(indexes, size = (self.clusters), replace = False)]
        centroids = centroids[:,None]
        
        for i in range(self.iterations):
            distances = np.sum((self.data - centroids)**2, axis = 2)**0.5 
            min_distances = np.argmin(distances, axis = 0)
            for c in range(self.clusters):
                centroids[c] = np.mean(self.data[min_distances == c, :], axis = 0)

        distances = np.sum((self.data - centroids)**2, axis = 2)**0.5
        min_distances = np.argmin(distances, axis = 0)
        centroids = np.reshape(centroids, (self.clusters, self.data.shape[1]))

        return min_distances, centroids
    
    def _sintetic_data(self):
        centroids = np.array([[1,0,0,0], [0,1,0,0]])
        constant = 5
        centroids = centroids * constant
        samples = np.repeat(centroids, 20/2, axis = 0)
        noise = np.random.normal(loc=0, scale=1, size=(20, 4))
        data = samples + noise
        clusters = np.array([[0],[1]])
        clusters = np.repeat(clusters, 20 / 2, axis=0)
        print('Los clusters reales:', clusters)
        return data
        
x = Kmeans(10,2)
print('Los clusters encontrados y los centroides encontrados son:',x.kmeans())