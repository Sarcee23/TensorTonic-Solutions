import numpy as np

def scalar_expression_partials(a, b, c, h):
    """
    Returns: the expression value and its three numerical partial derivatives
    """
    a = np.float64(a)
    b = np.float64(b)
    c = np.float64(c)
    h = np.float64(h)

    def evaluate(a,b,c):
        value = np.float64(0.0)
        value += (a*b +c)
        return value

    d = a*b+ c
    
    dxha= evaluate(a+h,b,c)
    dxa = evaluate(a,b,c)
    ansa = (dxha-dxa)/h
    
    dxhb= evaluate(a,b+h,c)
    dxb= evaluate(a,b,c)
    ansb = (dxhb-dxb)/h
    
    dxhc= evaluate(a,b,c+h)
    dxc = evaluate(a,b,c)
    ansc = (dxhc-dxc)/h

    return (float(d),float(ansa),float(ansb),float(ansc))
