# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:19:55 2022

@author: Zanete Dijeva
"""

# Recursive dictionary with memorization.
def fib_efficient(n, d):
    print('d', d)
    if n in d:
        print('n', n)
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        print('ans', ans)
        return ans

d = {1:1, 2:2}
print(fib_efficient(20,d))  