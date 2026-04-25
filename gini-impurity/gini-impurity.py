import numpy as np
def gini(y):
    y = np.array(y)
    if(y.size == 0):
        return 0.0
    _,counts = np.unique(y,return_counts=True)
    probs = counts/counts.sum()
    return 1.0 - np.sum(probs**2)
    

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    y_left = np.array(y_left)
    y_right = np.array(y_right)
    n_left = y_left.size
    n_right = y_right.size
    n_total = n_left + n_right
    if n_total ==0:
        return 0.0
    gini_left = gini(y_left)
    gini_right = gini(y_right)
    weighted_gini = (n_left/n_total*gini_left ) +(n_right/n_total*gini_right)
    return float(weighted_gini)
