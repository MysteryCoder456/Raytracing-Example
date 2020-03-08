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