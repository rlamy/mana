import numpy as np

class Matrix(object):
    """Represents a matrix"""

    def __init__(self, arr):
        self.array = arr

    def __mul__(self, other):
        return Matrix(np.dot(self.array, other.array))
