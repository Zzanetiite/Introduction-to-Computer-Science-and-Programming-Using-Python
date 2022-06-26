# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 16:21:53 2022

@author: Zanete Dijeva
"""

"""

The greatest common divisor of two positive integers is the largest 
integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

Write an iterative function, gcdIter(a, b), that implements 
this idea. 

"""

# We have a Max and min number. They could also be the same.
# If a == b, largest divider is the number itself.

# Then, it is wise to start with the smallest number as a divisor
# ,because divisor cannot be larger than Min No. 
# If that comes back as remainder 0 : Min number is the answer.

# Else, if it is not one of the above. I can use prime numbers to 
# reduce my attempts. I can check if both can be divided by the same prime. 
# This is to start from prime right below Min No.
# I will use a static list of primes to 100 and work downwards.?

# For anything else I can do the long - one by one way.
"""
def PossiblePrimeDivisors(minNo) :
    # Bisectional search would be faster but this is easier to code.
    PrNoTo100 = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if minNo in PrNoTo100 : return minNo
    for No in PrNoTo100 :
        if No > minNo :
            indexOfNo = PrNoTo100.index(No)
            ListToReturn = PrNoTo100[0:indexOfNo - 1]
            return ListToReturn
        
I finished this in v2. 
I checked for multipliers.
So, if it can be divided by prime, can it be divided by another 
prime afterwards? If so, need to find that. This creates a while loop.
Maybe this while loop would be faster than one by one? Maybe not.

"""
def gcdIter(a, b) :
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    maxNo = max(a,b)
    minNo = min(a,b)
    if maxNo == minNo : return minNo
    if maxNo % minNo == 0 : return minNo
    else:
        PrNoTo100 = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        #NoToCheck = PossiblePrimeDivisors(minNo)
        #print(NoToCheck)
        divisor = minNo
        if divisor in PrNoTo100 : return 1
        while divisor > 1 :
            if maxNo % divisor == 0  and  minNo % divisor == 0 :
                return divisor  
            else:
                divisor -= 1
                print(divisor)
        return divisor
 

print('Common Divisor: ', gcdIter(15,250))

    
