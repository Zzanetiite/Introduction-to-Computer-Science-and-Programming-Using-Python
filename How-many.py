# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 21:32:51 2022

@author: Zanete Dijeva
"""


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    animalsVal = aDict.values()
    count = 0
    for i in animalsVal :
        count += len(i)
    return count

print(how_many(animals))

