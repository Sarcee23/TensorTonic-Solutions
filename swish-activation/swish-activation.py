import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.array(x)
    y= np.asarray(x)
    sigmoid = 1/(1+np.exp(-x))
    return sigmoid*y
     