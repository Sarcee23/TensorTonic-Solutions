import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n = len(v)
    v = np.asanyarray(v)
    D = np.zeros((n,n),dtype=  v.dtype)
    D.flat[::n+1] = v
    return D
