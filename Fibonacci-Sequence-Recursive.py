# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 16:20:54 2022

@author: zanet
"""

# Fibonacci Sequence recursive function.
# Each number is the sum of the previous numbers.

# Writing from ground up:
# 0, 1, 1, 2, 3, 5, 8, 23, 21, 34, 55, 89 ...
# (1) == 0 -> calling this n1 (n for number)
# (2) == 1 -> calling this n2 (n for number)
# (3) == n1 + n2
# (4) == n(1+1) + n(2+1) or, in other words n(x) = n(x - 2) + n(x - 1) 
# (5) == n(2+1) + n(3+1)
# (6) == n(3+1) + n(4+1)

# I will assume that for the recursive call
# each previous n1, n2 become the new n1, n2.
# This means I won't register each No outside
# each recursive call.

def recurFibSeq(Number):
    '''
    Calculates the given Fibonacci Number.
    1(1), 1(2), 2(3), 3(4), 5(5), 8(6), 13(7), 21(8) ...
    
    Number - stands for Number in Fibonacci sequence order
    Number >= 0
       
    '''
    if Number == 0 : return 1
    if Number == 1 : return 1
    
    else:
        return (recurFibSeq(Number - 2) + recurFibSeq(Number - 1))
         

print(recurFibSeq(4))
