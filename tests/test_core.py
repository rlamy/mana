import pytest
import numpy as np
from mana import asmatrix, Matrix

def test_asmatrix():
    M = asmatrix(np.eye(3))
    assert M == Matrix(np.eye(3))
    with pytest.raises(ValueError):
        asmatrix([1, 2, 3])


def test_basic():
    arr = np.asarray([[0, 1], [1, 0]])
    M = Matrix(arr)
    N = Matrix(2 * arr)
    I = Matrix(np.eye(2))
    assert M == M
    assert M != N

    assert M * M == I
    assert 2 * M == N
    assert M * 2 == N
    assert M + M == N
    assert N - M == M
