import numpy as np

class Sorting:

    def __init__(self, array):
        self.array = array

    def indices(self):
        id = np.argsort((np.sum((abs(self.array))**2, axis=1))**0.5)[::-1]
        print(id)
        return self.array[id]
        
matriz = Sorting(np.array([[2,4,0,3],[10,23,1,8],[0,3,7,9]]))

print(matriz.indices())
        
    
        