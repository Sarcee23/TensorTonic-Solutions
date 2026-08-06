import numpy as np

def finite_difference_derivative(coefficients, x, h):
    """
    Returns: the polynomial value at x, the value at x plus h, and the forward-difference slope
    """
    coefficients = np.array(coefficients,dtype=np.float64)
    x = np.float64(x)
    h = np.float64(h)

    def evaluate(t):
        value = np.float64(0.0)
        for power,coeff in enumerate(coefficients):
            value += coeff*(t**power)
        return value

    fx = evaluate(x)
    fxh = evaluate(x+h)
    ans  = (fxh - fx)/h
    return (float(fx),float(fxh),float(ans))
            