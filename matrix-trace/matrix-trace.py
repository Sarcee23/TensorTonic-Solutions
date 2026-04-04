import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    m = len(A)
    n = len(A[0])
    trace = 0.0
    if m!=n :
        return None
    for i in range(m):
        trace +=A[i][i]
    return trace