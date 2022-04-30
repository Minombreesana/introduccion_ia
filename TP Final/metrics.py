import numpy as np

class Metric(object):
    def __call__(self, truth, pred):
        return NotImplemented

class MSE(Metric):
    def __init__(self):
        Metric.__init__(self)

    def __call__(self, truth, pred):
        n = truth.size
        return np.sum((truth - pred) ** 2) / n