import numpy as np

class Norma:

    def __init__(self, array):
        self.array = array

    def norma_cero(self):
        return np.count_nonzero(self.array != 0, axis=1)

    def norma_l1(self):
        return np.sum(abs(self.array), axis=1)
    
    def norma_l2(self):
        return (np.sum((abs(self.array))**2, axis=1))**0.5

    def norma_inf(self):
        return np.max(abs(self.array), axis=1)

matriz = Norma(np.array([[2,4,0,3],[10,23,1,8],[0,3,7,9]]))

print("la norma cero para la matriz dada es: ", matriz.norma_cero())
print("La norma L1 para la matriz dada es: ", matriz.norma_l1())   
print("La norma L2 para la matriz dada es: ", matriz.norma_l2()) 
print("La norma infinito para la matriz dada es: ", matriz.norma_inf()) 
