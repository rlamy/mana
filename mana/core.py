import numpy as np

def asmatrix(arg):
    """Create a matrix"""
    arr = np.asarray(arg)
    if len(arr.shape) != 2:
        raise ValueError("Matrices must be created from a rank-2 array")
    return Matrix(arr)

class Base(object):

    def __eq__(self, other):
        if type(other) is not type(self):
            return False
        return (other.array.shape == self.array.shape and
                np.all(other.array == self.array))

    def __ne__(self, other):
        return not (self == other)


class Matrix(Base):
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

def asvector(arg):
    """Create a vector"""
    arr = np.asarray(arg)
    if len(arr.shape) != 1:
        raise ValueError("Vectors must be created from one-dimensional objects")
    return Vector(arr)


class Vector(Base):
    """Represents a column vector"""

    def __init__(self, array):
        self.array = array

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.array + other.array)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.array - other.array)
        else:
            return NotImplemented
