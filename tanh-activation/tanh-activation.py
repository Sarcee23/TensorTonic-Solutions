import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)
    num = np.exp(x) - np.exp(-x)
    den = np.exp(x) + np.exp(-x)
    ans = num/den
    return ans
    