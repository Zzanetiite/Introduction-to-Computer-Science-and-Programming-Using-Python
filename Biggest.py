# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 21:35:31 2022

@author: Zanete Dijeva
"""

"""
This time, write a procedure, called biggest, which returns the key 
corresponding to the entry with the largest number of values 
associated with it. If there is more than one such entry, 
eturn any one of the matching keys.
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    Parameters
    ----------
    aDict : A disctionary
        A dictionary of animals.

    Returns
    -------
    largestVal : Integer
        The largest number of values associated to animal key.

    '''
    animalsVal = aDict.values()
    largestVal = 0
    for i in animalsVal :
        animalVal = int(len(i))
        if animalVal > largestVal :
            largestVal = animalVal
    if largestVal == 0 :
        return 0
    else:
        return largestVal

def which_of_many(aDict, largestVal):
    '''
    Parameters
    ----------
    aDict : A disctionary
        A dictionary of animals.
    largestVal : Integer
        The largest number of values associated to animal key.

    Returns
    -------
    Integer
        The key that has the largest values associated with it.

    '''
    largestValAnim = []
    for k in aDict :
        if len(aDict[k]) == largestVal :
            largestValAnim.append(k)
    if len(largestValAnim) > 0 :
        return largestValAnim[0]

def biggest(aDict):
    return which_of_many(animals, how_many(animals))

print(biggest(animals))