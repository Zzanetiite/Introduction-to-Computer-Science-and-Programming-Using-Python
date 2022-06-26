# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 16:21:53 2022

@author: Zanete Dijeva
"""

"""

The greatest common divisor of two positive integers is the largest integer 
that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

A clever mathematical trick (due to Euclid) makes it easy to find greatest 
common divisors. Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)

Write a function gcdRecur(a, b) that implements this idea recursively. 
This function takes in two positive integers and returns one integer.

"""

def gcd(a, b) :
   # maxNo = max(a,b)
   # b = min(a,b)
   # a = maxNo
    
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    
    This assumes neither starts as 0. Modulos from 0 is 
    'None, Division results in Infinity'
    '''
    if b == 0 : 
        return a

    else:
        return gcd(b, a % b)

print(gcd(15,10))

    
