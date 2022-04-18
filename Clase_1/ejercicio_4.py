import numpy as np

class Metrics:

    def __init__(self, array, prediction):
        self.array = array
        self.prediction = prediction

    def metrics(self):
        TP = np.count_nonzero(np.logical_and(self.array, self.prediction))
        TN = np.count_nonzero(np.logical_and(self.array == 0, self.prediction == 0))
        FN = np.count_nonzero(np.logical_and(self.array == 1, self.prediction== 0))
        FP = np.count_nonzero(np.logical_and(self.array == 0, self.prediction == 1))
        
        precision = TP/ (TP + FP)
        recall = TP / (TP + FN)
        accuracy = (TP + TN) / (TP + TN + FN + FP)

        return precision, recall, accuracy

prediction = np.array([1,1,1,1,0,0,1,1,0,0])
real = np.array([1,1,0,1,1,1,0,0,0,1])

truth = Metrics(real, prediction)

print(truth.metrics())
    
     
