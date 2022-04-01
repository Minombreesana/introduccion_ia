import numpy as np

class Distance:

    def __init__(self, array):
        self.array = array
    
    def distances(self, centroides):
        distance_x_1 = np.sum((centroides.array - self.array[0])**2, axis = 1)**0.5 
        distance_x_2 = np.sum((centroides.array - self.array[1])**2, axis = 1)**0.5 
        distance_x_3 = np.sum((centroides.array - self.array[2])**2, axis = 1)**0.5

        distances = np.array([distance_x_1, distance_x_2,distance_x_3])

        return distances

    def min_distances(self, distances):
        min_distances = np.argmin(distances, axis = 1)
        return min_distances
    

x = Distance(np.array([(1,2,3),(4,5,6),(7,8,9)]))
centroides = Distance(np.array([(1,0,0),(0,1,1)])) 
distances = x.distances(centroides)

print(f'Las distancias de los vectores x a los centroides son:{x.distances(centroides)}')
print(f'Los centroides a los que perteneces cada vector x son:{x.min_distances(distances)}')