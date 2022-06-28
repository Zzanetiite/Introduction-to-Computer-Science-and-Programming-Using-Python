# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 19:15:54 2022

@author: Zanete Dijeva
"""

"""
Task.
Write a procedure called oddTuples, which takes a tuple as input, 
and returns a new tuple as output, where every other element of 
the input tuple is copied, starting with the first one. So if test 
is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating 
oddTuples on this input would return the tuple ('I', 'a', 'tuple').
"""

"""
Tuple -> Tuple
Takes Tuple and returns a new Tuple made of every 
second elem of 1st Tuple.
"""
aTup = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    Tlist = []
    
    for i in range(len(aTup)) :
        if i % 2 == 1 : continue
        else:
            Tlist += aTup[i:i+1] 
    return tuple(Tlist)

            
print(oddTuples(aTup))