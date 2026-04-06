import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    x = np.asanyarray(x,dtype = float)
    return np.maximum(0,x)