import numpy as np

def matrix_inverse(A):
    A = np.asanyarray(A, dtype=float)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return None
    
    n = A.shape[0]
    # create augmented matrix [A | I]
    # se np.hstack to glue an identity matrix to the right of A
    augmented = np.hstack((A, np.eye(n)))
    
    for i in range(n):
        # Partial Pivoting:find row with largest abs value in ts col
        # prevents dividing by zero and reduces rounding errors
        pivot_row = i + np.argmax(np.abs(augmented[i:, i]))
        
        # if the pivot is basically zero, the matrix is singular
        if np.abs(augmented[pivot_row, i]) < 1e-12:
            return None
        
        # swap curr row with pivot row
        augmented[[i, pivot_row]] = augmented[[pivot_row, i]]
        
        # mrmalize the pivot row (make the diagonal ele 1)
        pivot_val = augmented[i, i]
        augmented[i] = augmented[i] / pivot_val
        
        # elminate other rows (make other elements in this col 0)
        for j in range(n):
            if i != j:
                factor = augmented[j, i]
                augmented[j] = augmented[j] - factor * augmented[i]
    
    # The left half is now I, the right half is A_inv
    A_inv = augmented[:, n:]
    
    # Final sanity check 
    if not np.allclose(A @ A_inv, np.eye(n), atol=1e-7):
        return None
        
    return A_inv