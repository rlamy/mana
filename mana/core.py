import numpy as np

class Matrix(object):
    """Represents a matrix"""

    def __init__(self, arr):
        self.array = arr

    def __neg__(self):
        return Matrix(-self.array)

    def __add__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self.array + other.array)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Matrix):
            return self + (-other)
        else:
            return NotImplemented

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
