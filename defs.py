from math import sqrt

def dist(pos1, pos2):
    """
    Find distance between two points on a 2D plane using Pythagorean Theorem
    
    Arguments:
        pos1 {tuple} -- position of first point
        pos2 {tuple} -- position of second point
    
    Returns:
        int -- distance between the points
    """
    a = pos1[0] - pos2[0]
    b = pos1[1] - pos2[1]
    c = sqrt(a ** 2 + b ** 2)
    return c


def constrain(n, low, high):
    """
    Constrain a value n between low and high
    
    Arguments:
        n {int} -- value to be contrained
        low {int} -- lowest value
        high {int} -- highest value
    
    Returns:
        int -- constrained value
    """

    return max(min(n, high), low)


def map_val(n, start1, stop1, start2, stop2, within_bounds=True):
    """
    Map a value to given range, derived from p5.js JavaScript Framework
    
    Arguments:
        n {int} -- value to be mapped
        start1 {int} -- starting of original value
        stop1 {int} -- ending of original value
        start2 {int} -- starting of mapped value
        stop2 {int]} -- ending of mapped value
        within_bounds {bool} -- whether the mapped value should be between start2 and stop2
    
    Returns:
        float -- mapped value
    """

    newval = (n - start1) / (stop1 - start1) * (stop2 - start2) + start2
    if (not within_bounds):
        return newval

    if (start2 < stop2):
        return constrain(newval, start2, stop2)
    else:
        return constrain(newval, stop2, start2)