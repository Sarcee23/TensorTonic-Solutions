def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    x1a,y1a,x2a,y2a = box_a
    x1b,y1b,x2b,y2b = box_b

    area_a = max(x2a-x1a,0) * max(y2a-y1a,0)
    area_b = max(x2b-x1b,0) * max(y2b-y1b,0)
    
    xtleft=  max(x1a,x1b)
    xbright = min(x2a,x2b)
    ytleft = max(y1a,y1b)
    ybright = min(y2a,y2b)
    
    if xbright <= xtleft or ybright <= ytleft:
            area_int = 0.0
    else:
            area_int = (xbright - xtleft) * (ybright - ytleft)

    area_uni = area_a + area_b - area_int
    if area_uni == 0:
        return 0.0

    return float(area_int/area_uni)
    pass