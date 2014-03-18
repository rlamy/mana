import numpy as np

class Matrix(object):
    """Represents a matrix"""

    def __init__(self, arr):
        self.array = arr

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return Matrix(np.dot(self.array, other.array))
        elif np.isscalar(other):
            return Matrix(self.array * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if np.isscalar(other):
            return Matrix(other * self.array)
        else:
            return NotImplemented
