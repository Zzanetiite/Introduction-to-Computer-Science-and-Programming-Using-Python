# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 21:33:35 2022

@author: Zanete Dijeva
"""

"""
Task:
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: 
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. 
This function should sum the area and square of the perimeter of the 
regular polygon. The function returns the sum, rounded to 4 decimal
places.
"""

import math

def polysum(n, s):
    '''
    Parameters
    ----------
    n : Integer or Float > 0
        Number of polygon sides.
    s : Integer or Float > 0
        Each polygon side length.

    Returns
    The sum = area of polygon + (perimeter of polygon)^2,
    rounded to 4 decimal places.

    '''
    area = ((0.25 * n * s * s) / (math.tan(math.pi / n)))
    perimeter = n * s
    perimSquare = perimeter * perimeter

    return round((area + perimSquare), 4)


print(polysum(9, 60)) 
