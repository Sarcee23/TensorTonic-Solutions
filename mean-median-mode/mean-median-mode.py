import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x=np.array(x)
    mean = np.mean(x)
    median = np.median(x)
    vals,counts = np.unique(x, return_counts=True)
    max_idx = np.argmax(counts)
    mode = vals[max_idx]
    return (mean,median,mode)