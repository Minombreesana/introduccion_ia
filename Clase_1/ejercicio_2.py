import numpy as np

class Sorting:

    def __init__(self, array):
        self.array = array
        self.norma_cero = self.norma_cero()
        self.norma_l2 = self.norma_l2()
        self.norma_inf = self.norma_inf()

    def norma_cero(self):
        return np.count_nonzero(self.array != 0, axis=1)

    def norma_l1(self):
        return np.sum(abs(self.array), axis=1)
    
    def norma_l2(self):
        return (np.sum((abs(self.array))**2, axis=1))**0.5

    def norma_inf(self):
        return np.max(abs(self.array), axis=1)

    def indices(self):
        id = np.argsort(self.norma_l2)[::-1]
        print("Las normas de las filas son:",self.norma_l2)
        print("Los indices de las normas ordenados descendente: ",id)
        return self.array[id]
        
matriz = Sorting(np.array([[2,4,0,3],[10,23,1,8],[0,3,7,9]]))

print("La matriz ordenada de norma l2 mayor a menor: \n", matriz.indices())
        
    
        