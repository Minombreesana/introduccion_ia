import numpy as np

class Metrics:

    def __init__(self, array):
        self.array = array

    def metrics(self, prediction):
        TP = np.count_nonzero(np.logical_and(self.array, prediction.array))
        TN = np.count_nonzero(np.logical_and(self.array == 0, prediction.array == 0))
        FN = np.count_nonzero(np.logical_and(self.array == 1, prediction.array == 0))
        FP = np.count_nonzero(np.logical_and(self.array == 0, prediction.array == 1))
        
        precision = TP/ (TP + FP)
        recall = TP / (TP + FN)
        accuracy = (TP + TN) / (TP + TN + FN + FP)

        return precision, recall, accuracy
    
truth = Metrics(np.array([1,1,0,1,1,1,0,0,0,1]))
prediction = Metrics(np.array([1,1,1,1,0,0,1,1,0,0]))

print(truth.metrics(prediction))
    
     
