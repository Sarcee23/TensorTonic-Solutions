def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    if not y_true:
        return 0.0

    tp = sum(1 for yt,yp in zip(y_true,y_pred) if yt == yp)
    n = len(y_true)
    return float(tp/n)