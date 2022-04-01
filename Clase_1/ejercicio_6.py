import numpy as np

class Distance:

    def __init__(self, array):
        self.array = array
    
    def distance_centroides(self, centroides):
        distance_x_1 = np.sum((centroides.array - self.array[0])**2, axis = 1)**0.5 
        distance_x_2 = np.sum((centroides.array - self.array[1])**2, axis = 1)**0.5 
        distance_x_3 = np.sum((centroides.array - self.array[2])**2, axis = 1)**0.5

        return distance_x_1, distance_x_2, distance_x_3

x = Distance(np.array([(1,2,3),(4,5,6),(7,8,9)]))
centroides = Distance(np.array([(1,0,0),(0,1,1)])) 

print(f'Las distancias de los vectores x a los centroides son:{x.distance_centroides(centroides)}')
