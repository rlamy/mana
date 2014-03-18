import numpy as np
from mana import Matrix

def test_basic():
    arr = np.asarray([[0, 1], [1, 0]])
    M = Matrix(arr)
    arr2 = (M * M).array
    assert np.all(arr2 == np.asarray([[1, 0], [0, 1]]))
    N1 = 2 * M
    N2 = M * 2
    assert np.all(N1.array == np.asarray([[0, 2], [2, 0]]))
    assert np.all(N2.array == np.asarray([[0, 2], [2, 0]]))
