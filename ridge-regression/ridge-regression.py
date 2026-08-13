def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    X=  np.array(X)
    y = np.array(y)
    n = len(X[0])
    penalty = lam*np.identity(n)
    weight = np.linalg.inv(X.T@X +penalty)@X.T@y
    return weight