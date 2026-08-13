import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    if len(y_pred) !=len(y_true):
        return None
    n = len(y_pred)
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    y_diff = np.array((y_true-y_pred)**2)
    summer = np.sum(y_diff)
    ans = summer/n
    return ans
    
