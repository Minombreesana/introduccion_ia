import numpy as np

class Sorting:

    def __init__(self, array):
        self.array = array

    def indices(self):
        norma_l2 = np.sum((abs(self.array))**2, axis=1)**0.5
        id = np.argsort(norma_l2)[::-1]
        print("Las normas de las filas son:",norma_l2)
        print("Los indices de las normas ordenados descendente: ",id)
        return self.array[id]
        
matriz = Sorting(np.array([[2,4,0,3],[10,23,1,8],[0,3,7,9]]))

print("La matriz ordenada de norma l2 mayor a menor: \n", matriz.indices())
        
    
        