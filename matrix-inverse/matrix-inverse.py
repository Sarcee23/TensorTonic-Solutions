import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    A = np.asanyarray(A)
    if A.ndim!=2 or A.shape[0]!= A.shape[1]:
        return None

    try:
        A_inv = np.linalg.inv(A)
        ##check for tolerance
        
        n = A.shape[0]
        identity = np.eye(n)
        if not np.allclose(A@A_inv,identity,atol = 1e-7):
            return None
        return A_inv

    except np.linalg.LinAlgError:
        return None

        