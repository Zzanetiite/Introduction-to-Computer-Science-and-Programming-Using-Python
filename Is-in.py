# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 20:21:52 2022

@author: Zanete Dijeva
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    
    '''
    top =(len(aStr)+2)//2
    bot = (len(aStr)-1)//2
    MiddleCharacters = aStr[bot:top]
    
    if len(aStr) == 0 :
        return False
        
    if len(aStr) == 1 :
        if char == MiddleCharacters :
            return True
        else:
            return False
    if len(MiddleCharacters) == 2 :
        if char == MiddleCharacters[0] : return True
        if char == MiddleCharacters[1] : return True        
        
    #for i in MiddleCharacters :
        #if char == i :
            #return True
    
    if char < MiddleCharacters :
        aStr = aStr[0:bot]
        return isIn(char, aStr)
    else: 
        aStr = aStr[top-1:len(aStr)]
        return isIn(char, aStr)
    
aStr ='abcdefghjkl'
char = 'n'

  
print(isIn(char, aStr))       