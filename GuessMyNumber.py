# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 11:17:34 2022

@author: zanet
"""

"""
Task
The program works as follows: you (the user) 
thinks of an integer between 0 (inclusive) 
and 100 (not inclusive). The computer makes guesses, 
and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's
secret number!
"""

def Instructions () :
    s2 = 'If number computer has given is higher, write "h"'
    s3 = 'If lower, write "l", if correct, write "c"'
    return print(s2), print(s3)
      
#x = input('Please enter a number between 0 to 99!')

#functions to check if input is valid
"""
I realised user only gives hints not the number :D. Makes sense.
def AllowedRange (x) :
    #is x a number? (function check only above zero)
    if x.isnumeric() == False : return False
    #is x in range?
    if 0 <= int(x) < 100 : return True
    if int(x) >= 100 : return False
    #if neither of the above it is something else - return false
    else : return False
"""
def AllowedAnswers (a) :
    #is it one of the allowed answers?
    if str(a) in 'lhc' : return True
    #if neither of the above it is something else - return false
    else : return False

def AskingTheQuestion():
    a = input('Please enter one of the letters l, h, c: ' ) 

    while AllowedAnswers (a) == False :
        print("")
        print("I have trouble reading that.")
        print("Is it a letter l,c or h?")        
        print("Please try again.")
        print("")
        a = input('Please enter one of the letters l, h, c: ' ) 
    return a

"""
#relaunch the function as many times as needed until a valid number is entered    
I realised user only gives hints not the number :D. Makes sense.
while AllowedRange(x) == False :
    print('Not in range. Please try again.')
    x = input('Please enter a number between 0 to 50!')
"""
#Start of the program
print("Computer will try to guess your number!" )
print("Please think of a whole number between 0 (inclusive) and 100 (not inclusive)" )
print("")
Instructions()
print("")

#counting the tries:
count = 0
#starting from the middle
xh = 100
xl = 0
x = 50
print("Is your secret number ", x, "?")
count += 1

print("")
a = AskingTheQuestion()

while a != "c" :
    if a == 'h' :
        xh = x
        x = int(x-((x-xl)/2))
        print("Is your secret number ", x, "?")
        count += 1
        a = AskingTheQuestion()
    if a == 'l' :
        #integers are rounded down so this is edge case
        if x == 98 :
            x = 99
        xl = x
        x = int(x+((xh-x)/2))
        print("Is your secret number ", x, "?")
        count += 1
        a = AskingTheQuestion()

print("")
print("This is the end of the game!")
print("Your secret number was: ", x)
print("")
print("It took me", count, "tries to guess.")