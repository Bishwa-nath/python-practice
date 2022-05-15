# imports math module
import math

# pi is the constant value
pi = math.acos(-1)

def polysum(n, s):
    """
    polysum is function that takes two parameters, of
    a regular polygon, n and s where n is number
    of sides and s is length of each sides.
    peri calculates the perimeter
    area calculates the area of the polygon.
    finally this function returns the sum of the area
    and square of the perimeter of the regular polygon,
    rounded to 4 decimal places.
    """
    peri = n*s
    area = (0.25 * n * s * s)/math.tan(pi/n)
    return round(peri * peri + area, 4)

